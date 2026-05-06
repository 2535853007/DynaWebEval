import asyncio
import json
import os

# --- 配置部分 ---
GEN_MODEL = "bolt2"
# 新增的 JSON 路径参数

json_file_path = f"/mnt/data2/xxx/web/app_status/app_status_{GEN_MODEL}.json"

MAX_CONCURRENT_TASKS = 10
task_n = 10
START_DELAY = 5

def load_configs(file_path):
    if not os.path.exists(file_path):
        print(f"❌ 错误：找不到文件 {file_path}")
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    configs = []
    for item in data.get("apps", []):

        configs.append({
                    "subdomain": item["app"],
                    "model_name": f"{GEN_MODEL}",
                    "gen_model": f"_{GEN_MODEL}",
                    "target_url": item["url"],
                    "task_n": task_n,
                    # 补全 md_path，参考 run.py 默认逻辑
                    "md_path": f"/mnt/data2/xxx/web/task_md/{item['app']}_tasks.md"
                })

    return configs

tasks_configs = load_configs(json_file_path)

async def run_pipeline(config):
    """
    针对每一组参数，按顺序执行脚本
    """
    sub = config["subdomain"]
    model = config["model_name"]
    gen = config["gen_model"]
    url = config["target_url"]
    task_n = config["task_n"]
    md_path = config["md_path"] # 获取路径

    scripts = [
        "/mnt/data2/xxx/pipeline/run/2_rerun.py",
    ]

    print(f"🚀 启动流水线: {sub}")

    for script in scripts:
        # 在 cmd 列表中加入 --md_path 参数
        cmd = [
            "python", script, 
            "--subdomain", sub, 
            "--model_name", model, 
            "--gen_model", gen, 
            "--target_url", url, 
            "--task_n", str(task_n),
            "--md_path", md_path  # 传递新参数
        ]
        
        # process = await asyncio.create_subprocess_exec(*cmd)
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=None, # 直接输出到终端
            stderr=None
        )
        await process.wait()

        if process.returncode != 0:
            print(f"❌ 任务失败: {sub} 在执行 {script} 时出错")
            return

    print(f"✅ 流水线完成: {sub}")

async def main():
    if not tasks_configs:
        print("没有可执行的任务。")
        return

    sem = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

    async def sem_run_pipeline(conf):
        async with sem:
            await run_pipeline(conf)

    print(f"⚡ 开始流水线，最大并发: {MAX_CONCURRENT_TASKS}，启动间隔: {START_DELAY}s")
    
    running_tasks = []
    for i, conf in enumerate(tasks_configs):
        task = asyncio.create_task(sem_run_pipeline(conf))
        running_tasks.append(task)
        
        if i < len(tasks_configs) - 1:
            print(f"⏱️ 等待 {START_DELAY} 秒后启动下一个任务...")
            await asyncio.sleep(START_DELAY)

    await asyncio.gather(*running_tasks)

if __name__ == "__main__":
    asyncio.run(main())