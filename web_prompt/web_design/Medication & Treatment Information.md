I need a website that serves as a comprehensive guide for medications and medical treatments. Users should be able to easily identify unknown pills by describing physical features like color, shape, or any printed numbers. 

I want people to be able to look up specific drugs to learn about recommended dosages, read up on potential side effects, and see reviews from other people who have taken them. It's also really important that they can check how different medications interact with each other, or if they interact poorly with food and alcohol. Safety details, like pregnancy risk summaries for specific prescriptions, should be easily accessible.

Additionally, the platform should let users research medical conditions or input their symptoms to explore potential causes and learn about available treatments and diagnoses. Lastly, I want to help users find more affordable healthcare options by allowing them to discover alternative medications and compare drug prices across different pharmacies.

The app you build must support the following tasks:
--- Task 1 ---
Task: identify pill
task_info: {"color": "black", "shape": "round", "imprint": "123"}

--- Task 2 ---
Task: find dosage
task_info: {"type": "recommended"}

--- Task 3 ---
Task: find drug interaction report
task_info: {"entities": ["medication", "alcohol"]}

--- Task 4 ---
Task: show side effects
task_info: {"entity": "medication"}

--- Task 5 ---
Task: check drug interaction
task_info: {"entities": ["melatonin", "Folate Forte"]}

--- Task 6 ---
Task: check drug interaction
task_info: {"entities": ["Novolin N", "Novolin R"]}

--- Task 7 ---
Task: locate risk summary
task_info: {"drug": "Metformin", "context": "use in pregnancy"}

--- Task 8 ---
Task: identify alternative and compare prices
task_info: {"drug": "Valtrex", "pharmacies": "various"}

--- Task 9 ---
Task: provide side effects
task_info: {"drug": "amoxicillin"}

--- Task 10 ---
Task: display treatments
task_info: {"condition": "inflammatory bowel disease (IBD)"}

--- Task 11 ---
Task: determine drug interactions
task_info: {"drug": "CHROMIUM"}

--- Task 12 ---
Task: compare prices
task_info: {"purpose": "pain management", "entities": "two medications"}

--- Task 13 ---
Task: show user reviews
task_info: {"drug_usage": "Herpes Zoster"}

--- Task 14 ---
Task: identify pill
task_info: {"imprint": "M366"}

--- Task 15 ---
Task: display side effects page
task_info: {"type": "specific drug"}

--- Task 16 ---
Task: find alcohol/food interactions
task_info: {"entity": "drug"}

--- Task 17 ---
Task: search for drug information and side effects
task_info: {"drug": "Paracetamol"}

--- Task 18 ---
Task: find drug price and details
task_info: {"drug": "Metformin 1000mg tablet"}

--- Task 19 ---
Task: look up side effects
task_info: {"drug": "Rogaine"}

--- Task 20 ---
Task: find causes
task_info: {"symptoms": ["sharp chest pain", "anxiety"]}

--- Task 21 ---
Task: show diagnoses and treatments
task_info: {"condition": "Female infertility"}

--- Task 22 ---
Task: identify pill
task_info: {"color": "pink", "shape": "oval", "imprint": "894 5"}
