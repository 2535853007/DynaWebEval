# DynaWebEval

🌐 Web Agent Evaluation & Repair Framework

This repository contains the evaluation pipeline and dataset for testing and improving GUI Web Agents. It includes a collection of web design prompts, corresponding GUI agent tasks, and a multi-stage evaluation pipeline designed to assess agent performance and facilitate website self-repair.

📂 Project Structure

The repository is organized into the following directories:

.
├── web_prompt/
│   ├── task_md/            # Contains 40 GUI agent tasks (instructions for execution)
│   └── web_design/         # Contains 40 prompts used to generate the initial websites
├── eval_pipeline/
│   ├── pipeline1/          # Initial execution: Agent performs tasks on the originally generated website
│   ├── pipeline2/          # Failure handling: Agent re-runs tasks that failed but had no web defects
│   ├── pipeline3/          # Post-repair execution: Agent re-executes tasks after website fixes
│   └── judge/              # Evaluation scripts
│       ├── judge.py        # Evaluator for Pipeline 1 results
│       └── judge.edit      # Evaluator for Pipeline 3 results

📝 Data Description

Web Prompts & Tasks (web_prompt/)
This directory holds the core dataset used for the experiments:
web_design/: Contains 40 distinct prompts. These are fed into a Web Agent to generate the initial target websites.
task_md/: Contains 40 corresponding task descriptions. These define the specific actions the GUI Agent must perform on the generated websites (e.g., "Click the login button", "Fill out the contact form").

⚙️ Evaluation Pipeline

The eval_pipeline/ directory contains a three-stage workflow designed to evaluate the robustness of the agent and the quality of the generated web interface.

Initial Execution (Pipeline 1)
Goal: Baseline evaluation.
Process: The GUI Agent attempts to execute the 40 tasks on the websites generated from the initial web_design prompts.
Evaluation: Results are assessed using judge/judge.py.

Failure Analysis & Re-run (Pipeline 2)
Goal: Filter and identify fixable failures.
Process: This pipeline isolates tasks where the GUI Agent failed, specifically filtering for cases where the failure was not caused by a web defect (e.g., agent error vs. broken UI). The agent attempts to re-run these specific tasks.

Post-Repair Execution (Pipeline 3)
Goal: Verify improvements after website repair.
Process: Once the website has undergone a repair process (fixing defects identified in previous stages), the GUI Agent re-executes the tasks to verify success.
Evaluation: Final results are assessed using judge/judge.edit.
