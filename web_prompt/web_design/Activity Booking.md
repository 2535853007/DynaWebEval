I need a website where travelers can discover and book amazing tours, activities, and experiences around the world. Users should be able to easily find things to do based on their destination, travel dates, and who is going, whether it's a solo trip or a family vacation with kids. 

People should be able to narrow down their choices based on what matters most to them—like finding the cheapest food tour, the highest-rated cultural experience, or activities that fit into a specific time frame or duration limit. They also need to see important details like total costs, starting times, and whether the activity offers perks like free cancellation, instant confirmation, or specific language guides. 

Once they find the perfect activity, they should be able to easily book their spot, or submit a request form to confirm availability and details. Finally, I want users to have their own personal profiles where they can save activities to a wish list or favorites list to easily keep track of ideas for their upcoming trips.

The app you build must support the following tasks:
--- Task 1 ---
Task: submit form
task_info: {"action": "book tasting tour", "location": "Maryland", "send_method": "phone", "confirmation_info": "phone number"}

--- Task 2 ---
Task: search tour
task_info: {"type": "deep-sea fishing", "location": "Moorea, Society Islands", "details_required": ["total cost", "start time"]}

--- Task 3 ---
Task: reserve ride
task_info: {"type": "airboat", "reviews_threshold": 500, "location": "Kissimmee, Florida", "date": "June 10, 2026"}

--- Task 4 ---
Task: book event
task_info: {"type": "kayaking", "location": "Winter Haven, Florida", "date": "June 18, 2026"}

--- Task 5 ---
Task: plan tour
task_info: {"type": "airboat", "location": "Lake Trafford, Florida", "date": "June 2026", "guarantee": "alligator sightings"}

--- Task 6 ---
Task: search tour
task_info: {"type": "ziplining", "location": "Bavaria, Germany"}

--- Task 7 ---
Task: determine tour
task_info: {"location": "Kentucky", "details_required": ["price", "availability"], "action_on_feasible": "book tickets"}

--- Task 8 ---
Task: book tour
task_info: {"title": "Empire Beneath the Streets", "location": "New York City, New York", "date": "May 20, 2026"}

--- Task 9 ---
Task: book tour
task_info: {"type": "ziplining", "location": "adventure park, Sevierville, TN", "date": "June 18, 2026"}

--- Task 10 ---
Task: add to wishlist
task_info: {"criteria": "highest rated activity", "location": "Amsterdam"}

--- Task 11 ---
Task: search experiences
task_info: {"type": "sports", "time": "morning", "language": "English", "group": {"adults": 1, "children": 2}, "location": "Portugal", "date": "May 2, 2026"}

--- Task 12 ---
Task: retrieve tours
task_info: {"include": "Louvre", "rating": "5 stars"}

--- Task 13 ---
Task: find tour
task_info: {"type": "rail", "duration": "shortest", "location": "Tokyo, Japan", "date_range": ["June 13, 2026", "June 18, 2026"]}

--- Task 14 ---
Task: add to favorites
task_info: {"type": "amusement park attraction", "criteria": "lowest price", "location": "Seoul"}

--- Task 15 ---
Task: locate activities
task_info: {"type": "family-friendly", "location": "Singapore", "date": "June 2, 2026", "options": "free cancellation"}

--- Task 16 ---
Task: search trip
task_info: {"type": "sightseeing", "style": "private", "duration": "longest", "location": "India", "date": "June 2026"}

--- Task 17 ---
Task: find activity
task_info: {"type": "water", "location": "Dubai", "time_range": ["5 PM", "12 AM"], "duration_max": "4 hours"}

--- Task 18 ---
Task: search tours
task_info: {"location": "Coliseum", "options": "free cancellation"}

--- Task 19 ---
Task: find activity
task_info: {"type": "skiing", "date": "June 10, 2026", "duration": "longest"}

--- Task 20 ---
Task: find vacations
task_info: {"type": "guided", "location": "Europe", "duration_min": "10 nights", "date": "July 2026"}

--- Task 21 ---
Task: find tour
task_info: {"type": "food", "location": "Paris", "criteria": "cheapest", "options": "free cancellation"}

--- Task 22 ---
Task: search tours
task_info: {"type": "cultural", "location": "New York", "date": "May 7, 2026", "rating": "5 stars", "price_max": 75}

--- Task 23 ---
Task: show experiences
task_info: {"location": "London", "duration_max": "1 hour", "rating_min": "4 stars"}

--- Task 24 ---
Task: book tour
task_info: {"type": "winery", "location": "Napa Valley", "features": ["Mediterranean cuisine", "wine tasting", "outdoor setup"], "group_size": 4, "date": "May 15, 2026", "time": "10 AM"}

--- Task 25 ---
Task: book activity
task_info: {"criteria": "cheapest", "availability": "likely to sell out", "location": "Los Angeles", "date": "June 2, 2026"}

--- Task 26 ---
Task: search activities
task_info: {"location": "Phuket, Thailand"}

--- Task 27 ---
Task: show activities
task_info: {"location": "Miami", "price": "lowest", "rating_min": "4 stars"}

--- Task 28 ---
Task: find tours
task_info: {"location": "Kyoto, Japan", "date": "May 25, 2026", "options": ["free cancellation"], "group": {"adults": 2, "infants": 1}, "action_on_available": "book"}
