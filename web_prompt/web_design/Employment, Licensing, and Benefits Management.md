I need a website that helps people manage their employment, professional licenses, and government benefits all in one place. 

Users should be able to easily look for specific jobs—like finding a police officer position in Alaska or an economist role in Washington, D.C.—and clearly see the salary, required qualifications, closing dates, and contact information. They should also be able to submit their job applications directly through the platform.

Beyond finding jobs, the site needs to help people figure out what financial support and benefits they qualify for. Whether they are checking their eligibility for unemployment, looking into child benefits, downloading an application for the SNAP program, or exploring support for retirees, users should be able to get accurate guidance based on their personal situation. 

I also want users to have a personal profile where they can track their progress. They should be able to save interesting job postings, track the status of professional licensing applications, bookmark local job centers, and keep a list of prospective veteran benefits to review later. They also need the ability to easily withdraw applications or update their details if their circumstances change. Finally, the site should include helpful resources, like guides for hiring individuals with disabilities and visual information on regional unemployment trends.

The app you build must support the following tasks:
--- Task 1 ---
Task: identify vacancies
task_info: {"position": "Physical Scientist", "details_required": ["count", "locations"]}

--- Task 2 ---
Task: assist application
task_info: {"position": "economist", "location": "Washington, D.C.", "agencies_required": 2}

--- Task 3 ---
Task: retrieve job details
task_info: {"position": "comptroller", "details_required": ["requisition_number", "salary_range", "closing_date", "office_contact_person"]}

--- Task 4 ---
Task: apply position
task_info: {"position": "police officer", "location": "Soldotna, AK", "details_required": ["form_required", "hourly_wage"], "check_availability": true}

--- Task 5 ---
Task: list qualifications
task_info: {"position": "environmental scientist", "audience": "public", "details_required": ["qualifications", "variations_across_listings"]}

--- Task 6 ---
Task: apply position
task_info: {"position": "firefighter", "location": "Orange County, CA", "salary_min": 50000, "education_required": "Bachelor's degree", "listings_required": 3, "summarize_differences": true}

--- Task 7 ---
Task: assist application
task_info: {"position": "administrative", "location": "Minnesota", "salary_min_per_hour": 18, "education_required": "high school diploma", "listings_required": 3}

--- Task 8 ---
Task: identify procedure
task_info: {"license_type": "Hunting and Fishing Licenses"}

--- Task 9 ---
Task: find application
task_info: {"program": "SNAP", "application_type": "paper"}

--- Task 10 ---
Task: find procedure
task_info: {"benefits_type": "Veteran Benefits"}

--- Task 11 ---
Task: locate page
task_info: {"topic": "hiring individuals with disabilities"}

--- Task 12 ---
Task: find location
task_info: {"facility": "Job Center", "location": "Jefferson County"}

--- Task 13 ---
Task: find eligibility
task_info: {"program": "Jobseeker's Allowance (JSA)"}

--- Task 14 ---
Task: find eligibility
task_info: {"benefit_type": "child benefit", "details_required": ["eligibility", "how_it_works", "how_to_claim"]}

--- Task 15 ---
Task: start process
task_info: {"program": "unemployment filing"}

--- Task 16 ---
Task: find support
task_info: {"location": "England", "demographics": {"status": "single", "age_group": "state pension age", "employment_status": "unemployed", "health_conditions": false, "caretaker_status": false}}

--- Task 17 ---
Task: find procedure
task_info: {"license_type": "Athletic Trainer"}

--- Task 18 ---
Task: display comparison
task_info: {"topic": "unemployment trends", "group": "women", "locations": ["Illinois", "Michigan"]}
