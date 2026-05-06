I want to build a comprehensive job discovery platform where people can easily find their next career opportunity. Users should be able to look for specific roles, whether they want to be a software engineer at an established tech company, a part-time waiter, or an entry-level finance worker. They need to be able to narrow down jobs by location, salary range, required education, and work schedules—like finding specific days to work or jobs they can start immediately.

When people browse, they should see the most recent openings clearly and be able to explore what's available across different departments. If they see a job they like, they can either save it to a personal list to review later or apply directly through the site using their personal details. I also want users to be able to set up customized alerts so they get notified whenever new roles open up in their favorite fields or cities. Lastly, it should be easy for them to keep track of their recent searches, manage their saved jobs, and track their submitted applications all in one place.

The app you build must support the following tasks:
--- Task 1 ---
Task: analyze job roles
task_info: {"department": "regulatory and quality", "criteria": ["count roles by job level", "filter most senior level", "identify salary range"]}

--- Task 2 ---
Task: search job roles
task_info: {"role": "Software Engineer", "company_type": "big-tech", "retrieve": ["company name", "year founded"]}

--- Task 3 ---
Task: list job roles
task_info: {"role": "customer support specialist", "location": "New York", "count": 3}

--- Task 4 ---
Task: find job roles
task_info: {"role": ["store manager", "assistant manager"], "location": "New York, NY", "output": "first listing location"}

--- Task 5 ---
Task: list recent jobs
task_info: {"count": 3, "return": ["locations"]}

--- Task 6 ---
Task: set job alert
task_info: {"department": "Parks", "location": "Oregon"}

--- Task 7 ---
Task: search job roles
task_info: {"level": "entry-level", "sector": "finance", "location": "San Francisco", "education_requirement": "Master's degree"}

--- Task 8 ---
Task: save job roles
task_info: {"role": ["Data Entry", "similar"], "count": 2}

--- Task 9 ---
Task: browse job roles
task_info: {"role": "solar panel installer", "filter": ["hide duplicates"]}

--- Task 10 ---
Task: search jobs
task_info: {"schedule": "regular daytime", "location": "44278", "start_timeframe": "1-2 weeks"}

--- Task 11 ---
Task: open recent search
task_info: {"action": "retrieve job search"}

--- Task 12 ---
Task: display jobs
task_info: {"categories": ["MBA", "Graduate Internships"]}

--- Task 13 ---
Task: show openings
task_info: {"scope": "all jobs"}

--- Task 14 ---
Task: browse jobs
task_info: {"role": "part-time waiter"}

--- Task 15 ---
Task: search jobs
task_info: {"role": "nurse", "location": "any"}

--- Task 16 ---
Task: find openings and apply
task_info: {"location": "Omaha", "role": "fulfillment center", "schedule": ["Thursday", "Friday", "Saturday"], "action": "apply if found"}

--- Task 17 ---
Task: search jobs
task_info: {"sector": "Retail", "location": "United States"}

--- Task 18 ---
Task: show jobs
task_info: {"scope": "all jobs"}

--- Task 19 ---
Task: find and save job
task_info: {"location": "Kohima, Nagaland", "education": "bachelor's degree", "salary_min": "25k per month", "date_posted": "last 7 days", "count": 1}

--- Task 20 ---
Task: filter job opportunities
task_info: {"keyword": "dogs", "filter": "training opportunities"}

--- Task 21 ---
Task: view and apply for jobs
task_info: {"role": "safety", "salary_min": "100k per annum", "action": ["check details", "apply"]}

--- Task 22 ---
Task: check job positions
task_info: {"group_by": "department", "location": "Downtown, Manhattan"}

--- Task 23 ---
Task: search jobs
task_info: {"location": "Miami, Florida", "sector": "Human Resources"}

--- Task 24 ---
Task: find recent job
task_info: {"role": "Accounting & Finance", "location": "Richmond, Virginia", "employment_type": "full-time", "timeframe": "most recent"}

--- Task 25 ---
Task: find career openings
task_info: {"department": "marketing"}

--- Task 26 ---
Task: search jobs and apply
task_info: {"role": "sales", "location": "San Francisco", "action": "apply if found"}

--- Task 27 ---
Task: search and apply job
task_info: {"role": "engineering", "location": "Madrid, Spain", "action": "apply", "applicant": {"name": "James Smith", "email": "buckeye.foobar@gmail.com", "reason": ["office location", "company success", "career opportunity"]}}

--- Task 28 ---
Task: find and save jobs
task_info: {"sector": "USA finance", "employment_type": "full-time", "role": "accountant", "action": "save"}

--- Task 29 ---
Task: find jobs
task_info: {"sector": "support services", "location": "Bentonville, Arkansas"}
