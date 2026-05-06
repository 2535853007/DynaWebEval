import os
import json
import re
import base64
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor  # 导入线程池


import shutil
import os
from openai import OpenAI

def cleanup_environment_errors(base_path: str):
    to_delete = []
    error_keywords = ["http://localhost:", "connection reset", "err_connection_reset"]

    for root, dirs, files in os.walk(base_path):
        # 统一检查 judge_false.json
        if "judge_false.json" in files:
            json_path = os.path.join(root, "judge_false.json")
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                reason = data.get("website_defect_reason", "").lower()
                if any(kw in reason for kw in error_keywords):
                    to_delete.append(root)
            except Exception as e:
                print(f"  ⚠️ 无法读取 {json_path}: {e}")

    for folder in list(set(to_delete)):
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"  🗑️ 已清理环境故障文件夹: {os.path.basename(folder)}")
            except Exception as e:
                print(f"  ❌ 删除失败 {folder}: {e}")


# --- 模拟辅助函数 ---
def _truncate_text(text: str, max_len: int) -> str:
    return text[:max_len] + "..." if len(text) > max_len else text


def _encode_image(img_path: str) -> str:
    try:
        with open(img_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"  ❌ 无法读取图片 {img_path}: {e}")
        return ""


# --- 核心逻辑：构建消息格式 ---
def construct_judge_messages(task: str, final_result: str, agent_steps: List[str], screenshot_paths: List[str], old_reason: str, max_images: int = 10) -> List[Dict]:
    # 系统提示词 (保持原样)
    system_prompt = f"""# You are an expert judge evaluating both browser automation agent performance AND the functional integrity of the generated website. 

    ## **CONTEXT**
    You are provided with a previous evaluation reason for a website defect: 
    "{old_reason}"

    ## **GOAL**
    Your task is to independently evaluate two things:
    1. **Task Success (verdict)**: Did the Agent fulfill the user's request based on its actions?
    2. **Old Defect Status (old_website_defect_exists)**: Does the previously reported defect (from the Context above) still exist in the current state?
    3. **New Defect Detection (new_website_defect)**: Are there any *new* functional, data, or logic bugs that were NOT mentioned in the previous context?
    4. **Error Source (error_source)**: If the task failed, was the root cause due to the **Agent** or the **Website**?
    ---

    ## **1. TASK EVALUATION (verdict)**
    - **true**: The agent successfully completed all key requirements of the user's task.
    - **false**: The agent failed to complete the task. 
    *Note: A task can be 'false' because the agent made a mistake, OR because a website defect made it impossible. A task can be 'true' even if the website has minor bugs, as long as the agent worked around them to finish the goal.*

    # **IMPORTANT EVALUATION NOTES:**
    **Action-Based Judgment**: Focus ONLY on the agent's actual actions in the browser screenshots, with the agent's self-reported success text used as supplementary reference information.
    **Evaluate Actions Only**: Do not judge the agent's final text summary. If the agent performs the correct click/input but describes it wrongly, it is still a SUCCESS.
    **Evaluate For Action** :  For each key step of the trace, double check whether the action that the agent tried to performed actually happened. If the required action did not actually occur, the verdict should be false.


    **Examples of task evaluation verdict:**
    - The agent moved on from a important step in the task without completing it
    - If task asks for 10 items and agent finds 4 items correctly: false
    - If task completed to full user requirements but with some errors to improve in the trajectory: true
    - If the trajectory is ideal and the output is perfect: true
    - If the task asks to complete an action on the page, and the agent reports that the action is completed but the screenshot or page shows the action is not actually complete: false
    - If the task asks to use a certain tool or site to complete the task but the agent completes the task without using it: false
    - If a task cannot be completed due to website issues (e.g., **Data/Information Gap**,**Missing Static Options**,**Functional Non-Responsiveness**,**Navigation Errors**, **Search Logic Mismatch**,**State Loss**,**Calculation Errors**,**Visual-Data Mismatch**,**Broken Flow**,Type C: Interactive Design Ambiguity): false

    ---

    ## **2. WEBSITE DEFECT DETECTION (website_defect)**

    ### **2.1 Old Defect Evaluation (old_website_defect_exists)**
    - Analyze the provided `Context` ("{old_reason}").
    - Check the current screenshots and agent trajectory.
    - Set `old_website_defect_exists` to **true** if the specific issue described in the context is still clearly present.
    - Set it to **false** if the issue appears to be fixed, or if the context is empty/irrelevant to the current page.

    ### **2.2 New Defect Detection (new_website_defect)**

    Set `website_defect` to "Type A", "Type B", "Type C", or a combination joined by " + " (e.g., "Type A + Type C") if the Website-Under-Test (WUT) exhibits any of the following issues. If no defect exists, set it to false.

        #### **Type A: Critical Blockers (May cause Task Failure)**
        *Requires high certainty. Do not use "likely" or "may be".*
        - **Data/Information Gap**: Required data does not exist (e.g., searching for "Red Tesla" returns 0 results on a car site).
        - **Missing Static Options**: Required dropdown values or buttons are missing from the UI.
        - **Functional Non-Responsiveness**: Clicking buttons (like "Search" or "Submit") does nothing.
        - **Navigation Errors**: Links lead to 404, blank pages, or incorrect sections.
        - **Search Logic Mismatch**: Results show "London to Miami" when agent input "Phoenix to Miami".

        #### **Type B: Business Logic & State Defects (May NOT block Task Completion)**
        *Requires high certainty. Only trigger if the data is demonstrably wrong based on common sense or previous steps.*
        - **State Loss**: 
            1.Changing "2 Passengers" to "1" reverts back automatically during checkout.
            2.User-provided search or filter inputs (e.g., destination, date, guest count) are lost when navigating back from a detail page to the results page, resetting the view to default listings instead of restoring the original context.
        - **Calculation Errors**: Adding two $1000 items shows a total of $1000.
        - **Visual-Data Mismatch**: 
            1.Text says "Red" but image shows "Blue".(Search query was for "Red Tesla", but results show photos/text for "White Tesla".)
            2.**UI elements display conflicting states for the same data across different views** (e.g., an item appears as "favorited" in the header badge and detail page, but shows as "not favorited" on the search results card).
        - **Broken Flow**: The user journey is disrupted by illogical or incomplete transitions—such as proceeding to checkout without required inputs, losing context after navigation, or triggering actions that falsely indicate completion (e.g., “Applied” status without actual submission)—preventing coherent task progression despite apparent interface affordances.
        - **Search Logic Mismatch**: The search function fails to correctly align results with user-provided criteria, manifesting in either of the following ways:
            1. Over-inclusive results: Searching for “a” returns “a, b, c” — including the target but also irrelevant items that do not match the query.
            2. Completely irrelevant results: Searching for “a” returns only “b, c” — entirely omitting relevant matches and showing only unrelated items.
        - **Insufficient Data for Comparison**: When the user’s task requires comparing multiple items to select the best option (e.g., based on price, features, ratings), but the website returns only a single item or an unreasonably limited set that prevents meaningful comparison—indicating a defect in search scope, filtering logic, or data availability.

        #### **Type C: Interactive Design Ambiguity**
        *Trigger this if the UI is confusing, poorly labeled, or causes data misinterpretation.*
        - **Unlabeled Indicators**: Numbers or icons without text labels (e.g., a "0" that could be a date, a count, or a status).
        - **Misleading Layouts**: Information placement that leads to cognitive friction or "likely" misinterpretations by users or agents.
        - **Affordance Issues**: Elements that look clickable but aren't, or vice-versa.
        - **Empty or Missing Labels/Buttons**: Buttons or labels with no visible text or icon, making their function ambiguous or completely unclear.
    ---

    ## **3. ERROR SOURCE ATTRIBUTION (error_source)**
    When `verdict` is **false**, you MUST specify the primary source of failure:
    - **"GUI_AGENT"**: The website functions correctly, but the agent made a wrong decision, clicked the wrong element, skipped a step, or misinterpreted the UI.
    - **"WEBSITE_DEFECT"**: The agent behaved reasonably, but the task failed because the website had a functional defect (Type A or B or C) that blocked progress or caused incorrect outcomes.

    > ⚠️ **Important**:  
    > - If the website has a defect **but the agent could have worked around it** and still failed due to its own mistake, the source is **GUI_AGENT**.  
    > - Only assign **"WEBSITE_DEFECT"** if the defect **directly and unavoidably caused the failure** despite reasonable agent behavior.  
    > - If `verdict` is **true**, set `error_source` to null. 

    ---

    ## **4. EVALUATION SCENARIOS**
    - **Success + No Defect**: Website works perfectly; Agent finishes task.
    - **Success + Website Defect**: The website has a bug (e.g., wrong total price displayed), but the agent still managed to reach the final page as requested.
    - **Failure + No Defect**: The website is fine; the Agent just clicked the wrong buttons or got lost.
    - **Failure + Website Defect**: The agent failed because the website was broken (e.g., the "Search" button didn't work).

    ---

    ## **5. JUDGMENT RIGOR (CRITICAL)**
    - **Certainty Requirement**: You are STRONGLY PROHIBITED from marking Type A or Type B defects based on guesses. If you use words like "likely", "probably", or "appears to be", you MUST classify it as **Type C (Design Ambiguity)** instead of a functional defect.
    - **Design vs. Bug**: If a piece of data (like "0 2026") looks like an error but could be a poorly labeled valid value (like "0 players"), it is a **Type C Design Error**, not a Type B Data Mismatch.
    - **Old vs New**: Be careful not to double-count. If a defect is exactly the same as the `Context`, mark it as `old_website_defect_exists: true` and do NOT list it in `new_website_defect`
    ---
    ## **RESPONSE FORMAT**
    Respond with EXACTLY this JSON structure:

    {{
        "reasoning": "Breakdown of the task. First, analyze if the OLD defect (from context) still exists. Second, analyze if there are any NEW defects. Finally, evaluate the agent's actions and the final verdict.",
        "verdict": true or false,
        "error_source": "If verdict is false, either \\"GUI_AGENT\\" or \\"WEBSITE_DEFECT\\". If verdict is true, use null.",
        "failure_reason": "If verdict is false, explain why in max 5 sentences. If verdict is true, use an empty string.",
        "old_website_defect_exists": true or false,
        "new_website_defect": "If no NEW defect is found, set this to false. If NEW defects are found, use the specific labels (e.g., 'Type A', 'Type B', or 'Type A + Type C').",
        "new_website_defect_reason": "If new_website_defect is true, explain the NEW bug. If false, use an empty string."
    }}
"""

    selected_screenshots = screenshot_paths[-max_images:]
    user_content = []

    user_text = "<task>\n{}\n</task>\n<agent_trajectory>\n{}\n</agent_trajectory>\n<final_result>\n{}\n</final_result>\n".format(
        task, '\n'.join(agent_steps), final_result
    )
    user_content.append({"type": "text", "text": user_text})

    for img_path in selected_screenshots:
        encoded = _encode_image(img_path)
        if encoded:
            user_content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{encoded}"}
            })

    return [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_content}]

MAX_PATH_LEN = 25  # 建议设为 40，给外层目录留余地

def get_safe_dir_name(text: str) -> str:
    # 移除 Windows 非法字符
    safe = re.sub(r'[\\/*?:"<>|]', '', text)
    # 替换空白符
    safe = safe.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    # 截断并确保两头干净
    # 建议长度设为 40-50 左右

    return safe.strip()[:MAX_PATH_LEN].strip().rstrip('.')
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

def should_process(agent_dir: str, files: List[str], defect_map: Dict[str, str]) -> bool:
    folder_name = os.path.basename(agent_dir)
    
    # 添加这行调试
    if "Plan a trip" in folder_name:
        print(f"DEBUG: 正在扫描文件夹 {folder_name}")
        print(f"DEBUG: 是否在 Map 中: {folder_name in defect_map}")
        print(f"DEBUG: 是否有 task.txt: {'task.txt' in files}")
        print(f"DEBUG: 是否已完成: {is_task_completed(agent_dir)}")

    
    # 1. 只有在映射表里的任务才处理
    if folder_name not in defect_map:
        return False

    if "task.txt" not in files: return False
    if "judge_true.json" in files: return False

    if "judge_false.json" in files:
        json_path = os.path.join(agent_dir, "judge_false.json")
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content or content == "{}":
                    os.remove(json_path)
                    return True
                data = json.loads(content)
                if not data:
                    os.remove(json_path)
                    return True
            return False
        except:
            return True

    if is_task_completed(agent_dir):
        return True
    return False


def process_single_folder(root: str, old_reason: str):
    try:
        files = os.listdir(root)
        print(f"\n🚀 正在处理: {os.path.basename(root)}")

        # --- 1. 读取基础数据 ---
        with open(os.path.join(root, "task.txt"), 'r', encoding='utf-8') as f:
            task_content = f.read()

        step_files = [f for f in files if f.startswith("step_") and f.endswith(".json")]
        step_files.sort(key=lambda x: int(re.search(r'step_(\d+)_', x).group(1)))

        agent_steps_desc = []
        final_result = ""
        for i, step_file in enumerate(step_files):
            with open(os.path.join(root, step_file), 'r', encoding='utf-8') as f:
                data = json.load(f)
                action = data.get("action", [])
                agent_steps_desc.append(f"Step {i+1}: {json.dumps(action, ensure_ascii=False)}")
                if i == len(step_files) - 1:
                    actions_list = action if isinstance(action, list) else [action]
                    for act in actions_list:
                        if isinstance(act, dict) and "done" in act:
                            final_result = act["done"].get("text", "")

        screenshot_dir = os.path.join(root, "screenshots")
        screenshot_paths = []
        if os.path.exists(screenshot_dir):
            shot_files = [f for f in os.listdir(screenshot_dir) if f.endswith("raw.png")]
            shot_files.sort(key=lambda x: int(re.search(r'step_(\d+)_', x).group(1)))
            screenshot_paths = [os.path.join(screenshot_dir, f) for f in shot_files]





        # --- 2. 请求 AI ---
        messages = construct_judge_messages(task_content, final_result, agent_steps_desc, screenshot_paths, old_reason)
        print(f"  🧠 请求 AI 判定中...")
        try:
            completion = client.chat.completions.create(
                model="qwen3.6-plus",  # 根据你提供的示例修改模型名
                messages=messages
            )
            # 提取文本内容
            raw_output = completion.choices[0].message.content
        except Exception as e:
            print(f"  ❌ API 请求失败: {e}")
            return

        if not raw_output:
            print(f"  ⚠️ 模型返回为空，取消保存。")
            return
        
        # --- 3. 解析 JSON ---
        if isinstance(raw_output, str):
            raw_output = raw_output.strip()
            match = re.search(r'```(?:json)?\s*({.*?})\s*```', raw_output, re.DOTALL)
            json_str = match.group(1) if match else raw_output
            try:
                response_json = json.loads(json_str)
            except json.JSONDecodeError:
                print(f"  ❌ JSON 解析失败，取消保存。内容预览: {raw_output[:100]}")
                return # 解析失败直接退出，不走下面的保存逻辑
        else:
            response_json = raw_output

        # --- 4. 最终校验并保存 ---
        if not response_json: # 检查是否为空字典
            print(f"  ⚠️ 解析结果为空字典，取消保存。")
            return

        verdict = response_json.get("verdict", False)
        filename = "judge_true.json" if verdict else "judge_false.json"
        save_file = os.path.join(root, filename)
        
        with open(save_file, 'w', encoding='utf-8') as f:
            json.dump(response_json, f, ensure_ascii=False, indent=2)
            
        print(f"  ✅ 评估完成: {filename}")

    except Exception as e:
        # 这里的异常会捕获文件 IO、网络请求等所有错误
        print(f"  ❌ 处理失败 {root}: {e}")
        # 不在这里写文件，保证了安全性

def run_evaluation_parallel(base_path: str, defect_map: Dict[str, str], max_workers: int = 10):
    tasks_to_process = [] # 存储元组 (path, reason)

    for root, dirs, files in os.walk(base_path):
        if should_process(root, files, defect_map):
            folder_name = os.path.basename(root)
            reason = defect_map.get(get_safe_dir_name(folder_name), "")
            tasks_to_process.append((root, reason))

    if not tasks_to_process:
        return

    print(f"🧵 启动线程池，处理 {len(tasks_to_process)} 个有效任务...")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用 lambda 或 starmap 传递多个参数
        for path, reason in tasks_to_process:
            executor.submit(process_single_folder, path, reason)

import time

if __name__ == "__main__":
    model_name = 'lovable_edit'  # 替换为你的模型名称
    # 初始化 LLM


    client = OpenAI(
            api_key=,
            base_url="",
        )
    json_path = rf"D:\dyad\run\agent_data\{model_name}\defect_tasks.json"
    PARENT_PATH = f"D:\\dyad\\run\\agent_data\\{model_name}\\TEXT"

    print(f"📡 脚本已启动，正在监控: {PARENT_PATH}")

    while True:
        try:
            # 1. 实时读取最新的 JSON 映射文件
            if not os.path.exists(json_path):
                print(f"⚠️ 找不到映射文件: {json_path}，等待中...")
                time.sleep(10)
                continue
            
            with open(json_path, 'r', encoding='utf-8') as f:
                defect_map = json.load(f)
                defect_map = {get_safe_dir_name(k): v for k, v in defect_map.items()}         
            print(f"\n--- 🕒 轮询开始: {time.strftime('%Y-%m-%d %H:%M:%S')} (任务库: {len(defect_map)}个) ---")

            if os.path.exists(PARENT_PATH):
                subfolders = [f for f in os.listdir(PARENT_PATH) if os.path.isdir(os.path.join(PARENT_PATH, f))]
                for folder in subfolders:
                    # 只有当 folder 在 json 中时才进入扫描逻辑

                    current_base_path = os.path.join(PARENT_PATH, folder)
                    run_evaluation_parallel(current_base_path, defect_map, max_workers=25)

            print(f"--- 😴 轮询结束，休眠 60s ---")
            time.sleep(60)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"⚠️ 循环异常: {e}")
            time.sleep(10)
