I need a website where people can easily find and book the right medical professionals, hospitals, pharmacies, and nursing homes. Users should be able to look up doctors based on their specific needs, like treating a particular condition, speaking a certain language, accepting specific insurance like Medicare, or offering virtual appointments. It's important that they can narrow down their options by location, whether that's looking within a certain distance of their zip code or searching for care in a specific city.

When people find a provider or a facility, they need to see all the important details to make an informed decision. This includes checking the doctor's credentials, reading and organizing patient reviews, looking at overall ratings, and exploring top hospital rankings. 

Once they choose the best specialist for their needs, the user should be able to easily schedule a consultation for a specific date and time. They also need a simple way to manage their healthcare journey, which means they should be able to cancel an appointment if plans change, save favorite doctors or top-rated hospitals to revisit later, and get directions to their chosen clinic or pharmacy.

The app you build must support the following tasks:
--- Task 1 ---
Task: search specialists
task_info: {"specialty": "psychiatrist", "features": ["virtual appointments", "experience treating neurodevelopmental disorders", "accepting new patients"]}

--- Task 2 ---
Task: search hospitals and specialists
task_info: {"location": "Portland, Oregon", "hospital_ranking": true, "best_hospital_by_patients": true, "hospital_physicians": true, "specialist_search": {"field": "child neurology", "criteria": "best-rated"}}

--- Task 3 ---
Task: search specialists
task_info: {"specialty": "pediatric dentist", "location": "Delaware"}

--- Task 4 ---
Task: search nursing homes
task_info: {"location_radius": {"center": "96817", "radius_miles": 25}, "features": ["accepts Medicare"]}

--- Task 5 ---
Task: search specialists
task_info: {"specialty": "doctor for back pain", "location": "Rochester"}

--- Task 6 ---
Task: review healthcare facilities
task_info: {"facility_name": "Children's Hospital"}

--- Task 7 ---
Task: search hospitals
task_info: {"specialty": "diabetes treatment", "location": "Phoenix"}

--- Task 8 ---
Task: search specialists
task_info: {"specialty": "thoracic surgeon", "location": "Omaha, Nebraska"}

--- Task 9 ---
Task: search hospital rankings
task_info: {"specialty": "cancer treatment"}

--- Task 10 ---
Task: search specialists
task_info: {"specialty": "primary care physician", "location_radius": {"center": "city center of Chicago", "radius_miles": 1}}

--- Task 11 ---
Task: search specialists
task_info: {"specialty": "dermatologist", "location": "Columbus, OH", "features": ["speaks Spanish"], "availability": {"date": "June 10, 2026"}}

--- Task 12 ---
Task: search specialists
task_info: {"specialty": "neurologist", "location": "New York", "criteria": "highest rating"}

--- Task 13 ---
Task: search specialists
task_info: {"specialty": "dermatologist", "location": "10001", "features": ["female"]}

--- Task 14 ---
Task: search specialists
task_info: {"specialty": "doctor for stomach pain", "location": "San Antonio"}

--- Task 15 ---
Task: search and book specialist appointment
task_info: {"specialty": "dentist", "location_radius": {"center": "Texas City, Texas", "radius_miles": 50}, "appointment_details": {"date": "June 30, 2026", "time": "2:30 pm"}}

--- Task 16 ---
Task: sign up for service
task_info: {"service": "virtual healthcare visit"}

--- Task 17 ---
Task: locate pharmacies
task_info: {"location": "45201", "services": ["hair loss evaluation and treatment"], "criteria": "nearest"}

--- Task 18 ---
Task: locate healthcare services
task_info: {"service": "Hair Loss Evaluation and Treatment", "location": "10018", "direction_request": true}

--- Task 19 ---
Task: search specialists
task_info: {"specialty": "audiologist", "location_radius": {"center": "New York, NY", "radius_miles": 50}, "criteria": {"minimum_rating": 4}}

--- Task 20 ---
Task: search specialists
task_info: {"specialty": "optometrist", "location": "Columbus, OH", "features": ["telehealth services"]}

--- Task 21 ---
Task: search specialists
task_info: {"specialty": "cardiologist", "location": "Jacksonville, Florida", "features": ["female"]}
