I need a website for a specialized recruitment platform where people can easily find and apply for jobs that perfectly match their unique needs. Users should be able to explore a wide variety of career opportunities, ranging from healthcare, IT, and legal roles to logistics, teaching, and hospitality. 

The main goal is to let job seekers find exactly what they are looking for based on highly specific preferences. They should be able to look for roles based on exact locations or commuting distances, specific salary ranges, required experience, education levels, and even particular work schedules or benefits like health insurance and security clearances. 

When someone finds an interesting position, they need to be able to read all the specific responsibilities, requirements, and job details clearly. It is also crucial that users can easily save, bookmark, or shortlist the jobs they like so they can keep track of them and prepare to apply later. Finally, they should be able to start the application process seamlessly when they are ready. The whole experience should make finding and applying for specialized work straightforward and highly personalized.

The app you build must support the following tasks:
--- Task 1 ---
Task: identify locations
task_info: {"job_type": "motorcoach driver", "region": "Iowa"}

--- Task 2 ---
Task: extract text
task_info: {"sentence_type": "first", "content_type": "job description", "region": "Pennsylvania", "job_id": true}

--- Task 3 ---
Task: identify responsibilities
task_info: {"job_type": "production operations", "experience_required": "3+ years", "specific_field": true}

--- Task 4 ---
Task: locate positions
task_info: {"job_type": "equipment operator", "region": "Houston", "salary_min": 50000, "experience_required": "3+ years"}

--- Task 5 ---
Task: identify requirements
task_info: {"job_type": "full-time", "region": "Atlanta, GA", "benefit": "health insurance", "attribute_type": "in-person", "schedule_hours": true}

--- Task 6 ---
Task: determine positions
task_info: {"job_type": "warehouse supervisor", "region": "Chicago area", "position_count": 3, "salary_min": 60000, "education_required": "bachelor's degree", "benefits": true, "experience_required": true}

--- Task 7 ---
Task: find job
task_info: {"industry": "logistics", "location_proximity": {"region": "New York", "zip": 11005, "distance": "20 miles"}, "salary_range": "middle-income", "education_required": "high school diploma"}

--- Task 8 ---
Task: find job
task_info: {"job_type": "customer service", "region": "Chicago", "wage_min": 20, "experience_required": "none"}

--- Task 9 ---
Task: find job
task_info: {"industry": "healthcare", "region": "Los Angeles", "education_required": "bachelor's degree", "schedule_weekends": "not required"}

--- Task 10 ---
Task: search opportunities
task_info: {"field": "Attorney"}

--- Task 11 ---
Task: find openings
task_info: {"career_field": "legal", "position_type": "summer volunteer", "industry": "law students", "region": "New York"}

--- Task 12 ---
Task: filter job
task_info: {"industry": "IT", "certification": "Security Clearance Certificate"}

--- Task 13 ---
Task: find job
task_info: {"job_type": "full-time", "provider_type": "healthcare", "update_recency": "recent"}

--- Task 14 ---
Task: search job
task_info: {"industry": "pharmaceutical"}

--- Task 15 ---
Task: find job
task_info: {"employment_type": "part-time", "proximity": {"distance": "5 miles", "region": "Moscow, Idaho"}, "industry": "hotel and food", "position": {"title": "chef and head cook", "category": "corporate only"}}

--- Task 16 ---
Task: find job
task_info: {"job_type": "sales executive", "region": "Manchester"}

--- Task 17 ---
Task: show jobs
task_info: {"field": "teaching", "region": "London"}

--- Task 18 ---
Task: search job
task_info: {"industry": "nutritionist", "region": "Ohio"}

--- Task 19 ---
Task: search job
task_info: {"employment_type": "intern", "region": "City of Industry, California, USA", "action": "bookmark"}

--- Task 20 ---
Task: search internship
task_info: {"location": "Germany", "target_audience": "recent university graduates", "update_recency": "last seven days", "action": "apply-to"}

--- Task 21 ---
Task: find job
task_info: {"industry": "customer services", "company_type": "airline", "region": "India", "job_status": {"details_viewed": true, "saved": true}}

--- Task 22 ---
Task: view job openings
task_info: {"job_type": "conductor trainee", "region": "New York", "action": "apply", "posted_order": "latest"}

--- Task 23 ---
Task: list positions
task_info: {"job_type": "Administrative and Clerical", "region": "Brooklyn", "status": "currently recruiting"}

--- Task 24 ---
Task: find job
task_info: {"job_type": "ground operations"}

--- Task 25 ---
Task: find jobs
task_info: {"region": "Texas"}

--- Task 26 ---
Task: browse positions
task_info: {"career_level": "tenured/tenure-track", "field": "Computer Sciences & Technology", "region": "California"}

--- Task 27 ---
Task: find job
task_info: {"career_field": "legal", "job_type": "full-time", "region": "San Diego County", "salary_min": 4000, "salary_unit": "month"}
