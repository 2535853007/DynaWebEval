I need a website for public transportation and navigation where users can easily plan their trips from start to finish. People should be able to get directions between any two locations, whether they are crossing the country entirely by train or just finding the fastest subway ride across town. 

The platform needs to support specific travel preferences, like needing to arrive by an exact time, minimizing walking distance, or ensuring the route is fully accessible. Users should be able to look up transit schedules for future dates, see upcoming departures for specific stations, and figure out exactly how much their trip will cost based on the time of day and passenger type. 

It is also really important that people can track their buses or trains in real-time. They need to know the exact current location of their ride, get walking directions right to their transit stop, and check for any live delays, route changes, or service disruptions. Finally, users should be able to create a personal profile where they can bookmark their closest stops, save their favorite routes for quick reference, and set up notifications so they know exactly when their ride is approaching.

The app you build must support the following tasks:
--- Task 1 ---
Task: plan itinerary
task_info: {"start_location": "Central Park, Manhattan", "end_location": "Miami", "transportation_mode": "train only"}

--- Task 2 ---
Task: plan trip
task_info: {"start_location": "Central Park", "end_location": "airport", "arrival_time": "11:00 AM", "date": "June 12, 2026"}

--- Task 3 ---
Task: show schedule
task_info: {"route": "unspecified", "day": "Wednesday"}

--- Task 4 ---
Task: track bus
task_info: {"start_location": "Abbotsford", "service_number": "unspecified"}

--- Task 5 ---
Task: view schedule
task_info: {"start_location": "South Station", "end_location": "City Point", "route": "Otis St @ Summer St", "date": "June 10, 2026"}

--- Task 6 ---
Task: show departures
task_info: {"station": "Oak Grove Station", "direction": "southbound"}

--- Task 7 ---
Task: locate train
task_info: {"start_station": "Queensboro Plaza Station, Long Island, NY", "end_station": "Grand Central Station, NY", "transportation_mode": "subway"}

--- Task 8 ---
Task: plan trip
task_info: {"start_location": "Greenport", "end_location": "Oyster Bay Branch", "transportation_modes": ["train", "bus"], "max_walk_distance": "less than half-mile"}

--- Task 9 ---
Task: retrieve schedule
task_info: {"start_location": "Bay Shore", "end_location": "Breakneck Ridge", "route_types": ["rail", "metro"], "date": "Thursday, March 23, 2026", "time": "8:37 AM"}

--- Task 10 ---
Task: get trip details
task_info: {"start_location": "52nd Street, Brooklyn", "end_location": "74th Street, Brooklyn", "departure_time": "now", "priority": "fastest accessible"}

--- Task 11 ---
Task: track bus
task_info: {"service_number": "unspecified"}

--- Task 12 ---
Task: view fares
task_info: {"destination": "Stoney Brook", "time": "after 10:00 PM", "traveler_type": "adult"}

--- Task 13 ---
Task: plan trip
task_info: {"start_location": "Central Park Zoo", "end_location": "Broadway Theater", "priority": "least walking"}

--- Task 14 ---
Task: show bus stop location
task_info: {"location": "unspecified"}

--- Task 15 ---
Task: find bus stops
task_info: {"location": "Alanson, MI"}

--- Task 16 ---
Task: plan trip
task_info: {"start_location": "Brooklyn, NY", "end_location": "Staten Island, NY", "date": "May 25, 2026", "arrival_time": "9:45 AM", "transportation_modes": ["bus", "subway terminals"]}

--- Task 17 ---
Task: calculate fares
task_info: {"start_location": "South Station", "end_location": "North Station"}

--- Task 18 ---
Task: check bus status
task_info: {"service_number": "S92", "issue_check": "disruptions"}
