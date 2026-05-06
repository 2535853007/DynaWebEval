
import asyncio
import gc
import os
import sys
import re
import argparse
import traceback
import shutil
from typing import Optional

import nest_asyncio
# 1. 立即修复 Windows 事件循环
if sys.platform == 'win32':
    if not isinstance(asyncio.get_event_loop_policy(), asyncio.WindowsProactorEventLoopPolicy):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

nest_asyncio.apply()

# 2. 导入组件
from browser_use import Agent, Browser

from browser_use.llm.openai.chat import ChatOpenAI_ovearsea
use_vision = False
vision_only = False
judge_model_name = 'gemini-3-pro-preview'

import json

def is_task_completed(task_dir: str) -> bool:
    """
    检查任务目录下最大步数的文件中是否包含 'done' 操作
    """
    if not os.path.exists(task_dir):
        return False

    files = os.listdir(task_dir)
    # 1. 优化正则：去掉末尾必须有的下划线，适应更多命名格式
    step_files = [f for f in files if f.startswith("step_") and f.endswith(".json")]
    
    if not step_files:
        return False

    try:
        # 2. 提取所有步数，并找到最大的步数数字
        step_nums = []
        for f in step_files:
            match = re.search(r'step_(\d+)', f)
            if match:
                step_nums.append(int(match.group(1)))
        
        if not step_nums:
            return False
            
        max_step = max(step_nums)
        
        # 3. 找出所有属于最大步数的文件
        # 这样做可以防止漏掉包含 action 的那个文件
        last_step_files = [
            f for f in step_files 
            if re.search(r'step_(\d+)', f) and int(re.search(r'step_(\d+)', f).group(1)) == max_step
        ]

        for file_name in last_step_files:
            with open(os.path.join(task_dir, file_name), 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 检查是否是字典格式，因为有些 JSON 可能是列表或其他
                if not isinstance(data, dict):
                    continue
                    
                actions = data.get("action", [])
                
                # 如果 action 不是列表，转换成列表方便统一遍历
                if not isinstance(actions, list):
                    actions = [actions]

                for act in actions:
                    # 情况 A: act 是字典，检查 "done" 键
                    if isinstance(act, dict):
                        if "done" in act:
                            return True
                    # 情况 B: act 是字符串
                    elif isinstance(act, str):
                        if "done" in act.lower():
                            return True
                        
    except Exception as e:
        print(f"⚠️ 解析任务状态失败 {task_dir}: {e}")
        
    return False

def get_safe_dir_name(text: str) -> str:
    """将任务目标转换为安全的文件名"""
    # 移除非法字符，限制长度
    safe = re.sub(r'[\\/*?:"<>|]', '', text)
    return safe.strip()[:50]

def parse_args():
    parser = argparse.ArgumentParser(description="Batch Run Browser-Use Tasks")
    parser.add_argument("--subdomain", type=str, required=True, help="子领域名称")
    parser.add_argument("--model_name", type=str, required=True, help="模型名称 (gpt-5.4等)")
    parser.add_argument("--gen_model", type=str, required=True, help="生成任务时使用的模型标识")
    parser.add_argument("--target_url", type=str, required=True, help="基础目标URL")
    parser.add_argument("--task_n", type=int, default=10, help="运行的任务数量")
    parser.add_argument("--md_path", type=str, help="任务Markdown文件路径")
    return parser.parse_args()

# --- 核心执行函数 ---

async def run_single_task(goal: str, args, vision_only: bool = True, base_agent_dir: str = "agent_data"):
    """
    执行单个 Agent 任务
    """
    import urllib.request
    try:
        # 只需要请求一次根路径即可触发 Vite 编译
        urllib.request.urlopen(args.target_url, timeout=10)
    except Exception as e:
        print(f"⚠️ 预热阶段警告 (可能是服务还没起稳): {e}")

    # 动态生成目录结构
    vision_suffix = "vision" if vision_only else "text"
    safe_goal = get_safe_dir_name(goal)

    # agent_data / 模型名 / 视觉模式 / 领域+生成模型 / 任务名
    agent_dir = os.path.join(
        base_agent_dir, 
        args.model_name, 
        vision_suffix.upper(), 
        f"{args.subdomain}_{args.gen_model}", 
        safe_goal
    )
    if os.path.exists(agent_dir):
        shutil.rmtree(agent_dir)
    # 确保目录存在
    os.makedirs(agent_dir, exist_ok=True)

    task_file_path = os.path.join(agent_dir, "task.txt")
    with open(task_file_path, 'w', encoding='utf-8') as f:
        f.write(goal)

    # 初始化浏览器 (每个任务一个实例，确保环境隔离)
    my_viewport = {'width': 1920, 'height': 1080}
    browser = Browser(
        chromium_sandbox=False,
        is_local=True,
        use_cloud=False,
        headless=True,  # 批量跑建议开启 headless
        viewport=my_viewport,
        timeout=240,
        minimum_wait_page_load_time=30.0,
        wait_for_network_idle_page_load_time=30.0,
        wait_between_actions=5.0,
        disable_security=True,
    )

    # 初始化 LLM
    llm = ChatOpenAI_ovearsea(model='gpt-5-mini')


    # llm = ChatOpenAI_ovearsea(model='gpt-5')
    llm.text_overcome = False
    llm.vision_only = vision_only
    llm.agent_directory = agent_dir

    judge_llm = ChatOpenAI_ovearsea(model=judge_model_name)

    # 构造任务文本 (根据你的本地服务端口调整)
    task_input = f"Open {args.target_url} and complete the task: {goal}"

    extend_system_message = """
    Strictly limit your available actions. You are ONLY allowed to use:
    click, input, write_file, replace file, dropdown selection, done.
    DO NOT use extract, down, Maps, open_new_tab, scroll,  or switch_tab.
    """

    agent = Agent(
        local=True,
        llm_timeout=120,
        browser=browser,
        task=task_input,
        llm=llm,
        judge_llm=judge_llm,
        use_vision=use_vision,
        calculate_cost=True,
        use_thinking=True,
        use_judge=False,
        vision_detail_level='high',
        generate_gif=False,
        agent_directory=agent_dir,
        save_conversation_path=agent_dir,
        max_steps=20,
        extend_system_message=extend_system_message
    )
    # generate_gif=os.path.join(agent_dir, "eval_track.gif"),
    print(f"执行任务: {safe_goal[:30]}...")
    try:
        history = await agent.run()
        print(f"任务完成: {safe_goal[:30]}")
        return history
    except Exception as e:
        await agent.close()
        print(f"任务失败 [{safe_goal[:30]}]: {e}")
        return None
    finally:
        # 彻底清理资源
        try:
            await agent.close()
            if hasattr(browser, 'playwright'):
                await browser.playwright.stop()
        except:
            pass
        del agent, browser, llm
        gc.collect()

# --- 主控逻辑 ---

# --- 修改后的 run.py 主控逻辑 ---

async def main():
    # 确保这些全局变量在函数内可用
    global vision_only, judge_model_name
    args = parse_args()
    # args = argparse.Namespace(
    #     subdomain="Accommodation Booking",
    #     model_name="bolt",
    #     gen_model="_bolt",
    #     target_url="http://localhost:10000",
    #     task_n=1,  
    #     md_path=None 
    # )
    base_agent_dir = 
    os.makedirs( , exist_ok=True)
    # 1. 检查文件路径
    md_path = args.md_path 
    print(f"🔍 正在检查任务文件: {md_path}")
    

    if not os.path.exists(md_path):
        print(f"❌ 找不到任务文件: {md_path}")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. 检查正则匹配结果
    # 提示：确保你的 Markdown 中每个任务之间确实有 "--- Task" 且换行
    task_goals = re.findall(r"(?:\*\*)*Task(?:\*\*)*:\s*([\s\S]*?)(?=\n--- Task|\Z)", content)
    print(f"📊 从文件中成功匹配到 {len(task_goals)} 个任务目标")
    
    tasks_to_run = []
    mode_dir = "VISION" if vision_only else "TEXT"

    for goal in task_goals:
        goal = goal.strip()
        if not goal: continue
        
        safe_goal = get_safe_dir_name(goal)
        task_dir = os.path.join(
            base_agent_dir, 
            args.model_name, 
            mode_dir, 
            f"{args.subdomain}_{args.gen_model}", 
            safe_goal
        )

        if not is_task_completed(task_dir):
            tasks_to_run.append(goal)
        else:
            print(f"⏩ 跳过 (任务已完成/包含Done): {safe_goal[:20]}...")

    if not tasks_to_run:
        print("✅ 待运行任务列表为空。请检查 Markdown 格式或是否所有任务已跑完。")
        return

    # 并发控制
    sem = asyncio.Semaphore(args.task_n)

    async def sem_task(goal):
        async with sem:
            await run_single_task(goal, args, vision_only=vision_only, base_agent_dir=base_agent_dir)

    print(f"🚀 开始执行所有任务 (并发限制: {args.task_n}, 总计: {len(tasks_to_run)} 个)")
    
    await asyncio.gather(*(sem_task(g) for g in tasks_to_run))
    print("🏁 全部批量任务处理完毕。")

# --- 程序入口 ---
if __name__ == "__main__":
    try:
        # 核心修复：确保 main() 被异步运行
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 用户手动停止了程序。")
    except Exception as e:
        print(f"\n❌ 程序发生异常: {e}")
        traceback.print_exc()  # 打印堆栈帮助定位具体报错


