import asyncio
import gc
import os
import sys
import re
import argparse
import traceback
import shutil
import json  # 新增：用于解析JSON
from typing import Optional

import nest_asyncio

if sys.platform == 'win32':
    if not isinstance(asyncio.get_event_loop_policy(), asyncio.WindowsProactorEventLoopPolicy):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

nest_asyncio.apply()

from browser_use import Agent, Browser
from browser_use.llm.openai.chat import ChatOpenAI_ovearsea

use_vision = False
vision_only = False
judge_model_name = 'gemini-3-pro-preview'

def get_safe_dir_name(text: str) -> str:
    safe = re.sub(r'[\\/*?:"<>|]', '', text)
    return safe.strip()[:50]
def count_agent_errors(root_dir):
    """
    遍历目录并统计符合条件的任务文件夹数量：
    1. 存在 judge_false 开头的 JSON 文件
    2. JSON 内容满足 error_source == "GUI_AGENT" 且 website_defect == False
    3. 文件夹中不存在 re_run_count.txt
    """
    count = 0
    matched_tasks = []

    # 遍历 root_dir 下的所有目录
    for root, dirs, files in os.walk(root_dir):
        # 增加条件判断：当前目录下不能有 re_run_count.txt
        if "re_run_count.txt" in files:
            continue

        for file in files:
            # 匹配结果文件，通常是 judge_false 开头的 json
            if file.startswith("judge_false") and file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                        # 判断逻辑
                        is_gui_agent = data.get("error_source") == "GUI_AGENT"
                        no_website_defect = data.get("website_defect") == False
                        
                        # 只有当符合 JSON 条件且没有重跑记录时才统计
                        if is_gui_agent and no_website_defect:
                            count += 1
                            # 获取文件夹名称作为任务名
                            task_name = os.path.basename(root)
                            matched_tasks.append(task_name)
                except Exception as e:
                    print(f"读取文件失败 {file_path}: {e}")

    return count, matched_tasks

def parse_args():
    parser = argparse.ArgumentParser(description="Batch Run Browser-Use Tasks")
    parser.add_argument("--subdomain", type=str, required=True, help="子领域名称")
    parser.add_argument("--model_name", type=str, required=True, help="模型名称 (gpt-5.4等)")
    parser.add_argument("--gen_model", type=str, required=True, help="生成任务时使用的模型标识")
    parser.add_argument("--target_url", type=str, required=True, help="基础目标URL")
    parser.add_argument("--task_n", type=int, default=10, help="运行的任务数量")
    parser.add_argument("--max_concurrent", type=int, default=3, help="最大并发数")
    parser.add_argument("--md_path", type=str, help="任务Markdown文件路径")
    return parser.parse_args()

# --- 核心执行函数 ---

async def run_single_task(goal: str, args, vision_only: bool = True, base_agent_dir: str = "agent_data"):
    """
    执行单个 Agent 任务
    """
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

    run_count_file = os.path.join(agent_dir, "run_count.txt")
    re_run_count_file = os.path.join(agent_dir, "re_run_count.txt")
    current_count = 0  # 默认为 0
    if os.path.exists(agent_dir):
        # 1. 如果文件存在，读取当前的次数
        if os.path.exists(run_count_file):
            try:
                with open(run_count_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content.isdigit():
                        current_count = int(content)
            except Exception as e:
                print(f"⚠️ 读取运行次数失败: {e}")

        shutil.rmtree(agent_dir)

    if os.path.exists(agent_dir):
        shutil.rmtree(agent_dir)
    # 确保目录存在
    os.makedirs(agent_dir, exist_ok=True)

    new_count = current_count + 1
    try:
        with open(re_run_count_file, 'w', encoding='utf-8') as f:
            f.write(str(new_count))
        print(f"📝 运行次数已更新为: {new_count}")
    except Exception as e:
        print(f"⚠️ 写入文件失败: {e}")

    # 5. 写入任务文件
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
        minimum_wait_page_load_time=3.0,
        wait_for_network_idle_page_load_time=10.0,
        wait_between_actions=2.0,
        disable_security=True
    )

    # 初始化 LLM
    llm = ChatOpenAI_ovearsea(model="gemini-3.1-flash-lite-preview")
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
        llm_timeout=300,
        browser=browser,
        task=task_input,
        llm=llm,
        judge_llm=judge_llm,
        use_vision=use_vision,
        calculate_cost=True,
        use_thinking=True,
        use_judge=True,
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

async def main():
    global vision_only, judge_model_name
    args = parse_args()

    md_path = args.md_path 
    if not os.path.exists(md_path):
        print(f"❌ 找不到任务文件: {md_path}")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    task_goals = re.findall(r"(?:\*\*)*Task(?:\*\*)*:\s*([\s\S]*?)(?=\n--- Task|\Z)", content)
    
    tasks_to_run = []  # 存储结构: (goal, failure_reason)
    mode_dir = "VISION" if vision_only else "TEXT"

    for goal in task_goals:
        goal = goal.strip()
        if not goal:
            continue
        
        safe_goal = get_safe_dir_name(goal)
        # task_dir = os.path.join(
        #     "agent_data", args.model_name, mode_dir, 
        #     f"{args.subdomain}_{args.gen_model}", safe_goal
        # )
        base_agent_dir =
        task_dir = os.path.join(
            base_agent_dir, 
            args.model_name, 
            mode_dir, 
            f"{args.subdomain}_{args.gen_model}", 
            safe_goal
        )

        true_file = os.path.join(task_dir, f"judge_true_{judge_model_name}.json")
        # 检查两种可能的失败文件名
        false_files = [
            os.path.join(task_dir, f"judge_false_{judge_model_name}.json"),
            os.path.join(task_dir, "judge_false.json")
        ]

        # 1. 如果任务成功，跳过
        if os.path.exists(true_file):
            print(f"⏩ 跳过 (已成功): {safe_goal[:20]}...")
            continue

        run_count = 0
        run_count_file = os.path.join(task_dir, "run_count.txt")
        
        if os.path.exists(run_count_file):
            try:
                with open(run_count_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content.isdigit():
                        run_count = int(content)
            except Exception as e:
                print(f"⚠️ 读取运行次数失败 {safe_goal[:10]}: {e}")

        if run_count >= 2:
            continue

        # 2. 检查失败文件
        failure_reason = None
        should_retry = False
        
        for f_path in false_files:
            if os.path.exists(f_path):
                try:
                    with open(f_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if data.get("error_source") == "GUI_AGENT" and data.get("website_defect") == False:
                            failure_reason = data.get("reasoning", "Unknown reasoning")
                            should_retry = True
                            break  # 找到匹配的错误源，准备重跑
                except Exception as e:
                    print(f"⚠️ 读取JSON失败 {f_path}: {e}")

        # 3. 决定是否加入运行列表
        if should_retry:
            print(f"🔄 发现 GUI_AGENT 错误，加入重试队列: {safe_goal[:20]}...")
            tasks_to_run.append((goal, failure_reason))
        elif not any(os.path.exists(p) for p in false_files):
            # 如果既没有成功文件也没有失败文件，说明是新任务
            tasks_to_run.append((goal, None))
        else:
            print(f"⏩ 跳过 (非 Agent 错误): {safe_goal[:20]}...")

    if not tasks_to_run:
        print("✅ 没有需要运行或重试的任务。")
        return

    sem = asyncio.Semaphore(args.task_n)
    base_agent_dir = 
    # 推荐写法
    async def sem_task(task_item):
        # 解构元组，拿到 goal
        goal, reason = task_item
        async with sem:
            await run_single_task(goal, args, vision_only=vision_only,base_agent_dir=base_agent_dir)

    # 调用处改为
    await asyncio.gather(*(sem_task(item) for item in tasks_to_run))

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
