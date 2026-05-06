I need a website where people can easily find and book flights for their upcoming travels. Users should be able to look up flights for one-way or round trips, whether they are traveling alone, with their family, or bringing along infants and seniors. 

They need to see all the important details before booking a trip, like baggage fees, meal options, total flight duration, and layover routes. I want them to be able to pick their preferred seats, such as exit rows or premium economy, and clearly see the price differences and total costs including all taxes. 

The platform should let travelers look for flights that fit specific budgets, exact arrival times, or even let them pay using their frequent flyer miles. It would also be great if they could narrow down options to specific aircraft types or choose flexible tickets. Once they find a flight they like, they should be able to book it right away, save it to receive notifications about price drops, or easily arrange a rental car for when they land. 

Lastly, please include a feature where users can check and track real-time flight statuses, see delays, and keep an eye on active flight locations to stay perfectly updated on their journey.

The app you build must support the following tasks:
--- Task 1 ---
Task: retrieve baggage allowance
task_info: {"origin": "Waterloo, Ontario", "destination": "Calgary, Alberta", "trip_type": "round-trip", "start_date": "May 15, 2026", "end_date": "June 20, 2026"}

--- Task 2 ---
Task: identify meal options
task_info: {"class": "premium economy", "origin": "Dallas/Fort Worth", "destination": "Singapore", "start_date": "May 23, 2026", "end_date": "June 3, 2026"}

--- Task 3 ---
Task: retrieve flight details
task_info: {"type": ["flight duration", "daily flights count"], "origin": "Rome", "destination": "Naples", "start_date": "May 23, 2026", "end_date": "June 18, 2026"}

--- Task 4 ---
Task: check seat availability
task_info: {"seat_type": "exit row", "origin": "Seattle, WA", "destination": "Honolulu, HI", "start_date": "May 29, 2026", "end_date": "June 3, 2026"}

--- Task 5 ---
Task: calculate flight cost
task_info: {"origin": "Palma de Mallorca", "destination": "Newcastle", "trip_type": "cheapest", "start_date": "May 3, 2026", "end_date": "June 23, 2026"}

--- Task 6 ---
Task: retrieve flight numbers
task_info: {"origin": "London (LHR)", "destination": "Sydney (SYD)", "connection": "Singapore (SIN)", "trip_type": "round-trip", "outbound_date": "May 2, 2026", "return_date": "June 28, 2026"}

--- Task 7 ---
Task: determine price difference
task_info: {"class_comparison": ["premium seating", "standard economy"], "origin": "Houston", "destination": "Los Angeles", "start_date": "May 5, 2026", "end_date": "June 20, 2026"}

--- Task 8 ---
Task: book flight
task_info: {"trip_type": "round-trip", "origin": "Istanbul Airport (IST)", "destination": "John F. Kennedy International Airport (JFK)", "start_date": "May 9, 2026", "duration": "two weeks"}

--- Task 9 ---
Task: book flight
task_info: {"trip_type": "round-trip", "origin": "Geneva, Switzerland", "destination": "Osaka, Japan", "outbound_date": "May 22, 2026", "return_date": "June 28, 2026"}

--- Task 10 ---
Task: book flight
task_info: {"trip_type": "round-trip", "origin": "Bhubaneswar (BBSR)", "destination": "Delhi (DEL)", "outbound_date": "May 20, 2026", "return_date": "June 3, 2026"}

--- Task 11 ---
Task: search flight and rent car
task_info: {"flight": {"trip_type": "round-trip", "origin": "Dallas (DFW)", "destination": "Miami (MIA)", "outbound_date": "May 20, 2026", "return_date": "June 25, 2026"}, "car_rental": {"pickup_location": "MIA", "pickup_time_offset": "1 hour after flight arrival", "category": "compact", "details": ["price per day", "make/model", "number of seats"]}}

--- Task 12 ---
Task: book first available flight
task_info: {"origin": "Ontario International Airport", "destination": "New York City"}

--- Task 13 ---
Task: find cheap flights
task_info: {"origin": "New Orleans, LA", "destination": "El Paso, TX"}

--- Task 14 ---
Task: book one-way flight
task_info: {"trip_type": "one-way", "origin": "Bangalore", "destination": "Goa", "date": "June 29, 2026", "time": "evening", "passengers": 2, "preferences": ["fastest", "most flexible", "direct"]}

--- Task 15 ---
Task: find flights
task_info: {"origin": "Indira Gandhi", "destination": "Los Cabos", "months": ["May 2026", "June 2026"]}

--- Task 16 ---
Task: track flight
task_info: {"flight_number": "D145", "date": "April 18, 2026"}

--- Task 17 ---
Task: find one-way flights
task_info: {"trip_type": "one-way", "origin": "Sacramento", "destination": "Houston IAH", "date": "June 2, 2026", "payment_method": "miles", "passengers": 1}

--- Task 18 ---
Task: find round-trip flights
task_info: {"destination": "Japan", "trip_type": "round-trip", "passengers": 1, "outbound_date": "May 16, 2026", "return_date": "June 23, 2026"}

--- Task 19 ---
Task: arrange flight
task_info: {"origin": "Belo Horizonte", "destination": "Buenos Aires", "passengers": 2, "date": "May 24, 2026", "seat_preferences": "confirmation needed"}

--- Task 20 ---
Task: search flights
task_info: {"origin": "Seattle", "destination": "New York", "date": "June 5, 2026", "filter": "allow purchases with miles"}

--- Task 21 ---
Task: search flight
task_info: {"origin": "Dublin", "destination": "Malta", "trip_type": "one-way", "passengers": 2, "date": "May 22, 2026", "next_action": "initiate seat selection for booking"}

--- Task 22 ---
Task: find flight
task_info: {"origin": "San Francisco", "destination": "San Diego", "trip_type": "one-way", "date": "June 15, 2026", "passengers": {"adults": 2, "seniors": 1}, "filter": "nonstop morning flight", "action": "view deal"}

--- Task 23 ---
Task: retrieve flight
task_info: {"origin": "Madurai", "destination": "Chennai", "date": "May 20, 2026", "filter": "lowest-cost direct flight", "action": "confirm booking"}

--- Task 24 ---
Task: book flight
task_info: {"origin": "Doha", "destination": "Durban, Africa", "passengers": {"adults": 2, "infants": 1}, "date": "May 28, 2026", "class": "economy comfort", "filter": "first available flight"}

--- Task 25 ---
Task: find flight deals
task_info: {"origin": "New York", "destination": "Honolulu", "budget": "$1300", "class": "premium economy"}

--- Task 26 ---
Task: display route map and cost
task_info: {"origin": "Los Angeles", "destination": "Miami", "date": "May 12, 2026", "extras": "layover options"}

--- Task 27 ---
Task: check flight status
task_info: {"origin": "Los Angeles area", "destination": "Boston area", "date": "June 10, 2026", "extras": ["on-schedule status", "delays"], "action": "save updates"}

--- Task 28 ---
Task: search flight
task_info: {"origin": "SFO", "destination": "EWR", "aircraft": "Boeing 787-9", "premium_seating": true}

--- Task 29 ---
Task: calculate baggage fee
task_info: {"class": "first-class", "origin": "Columbus", "destination": "New Orleans", "date": "May 9, 2026"}

--- Task 30 ---
Task: book flight
task_info: {"origin": "Santa Fe, New Mexico", "destination": "Phoenix, Arizona", "passengers": 1, "trip_type": "round-trip", "departure_date": "May 13, 2026", "return_date": "June 28, 2026"}

--- Task 31 ---
Task: search flight
task_info: {"origin": "Chicago", "destination": "Paris", "trip_type": "one-way", "departure_date": "May 17, 2026", "action_after_search": "reserve cheapest option"}

--- Task 32 ---
Task: search flight
task_info: {"origin": "New York airports", "destination": "Aruba", "passengers": 1, "trip_type": "round-trip", "departure_date": "May 1, 2026", "return_date": "June 5, 2026", "price_filter": "cheapest"}

--- Task 33 ---
Task: book flight
task_info: {"origin": "Addis Ababa", "destination": "Accra", "trip_type": "one-way", "departure_date": "June 14, 2026", "ticket_class": "economy", "price_filter": "cheaper"}

--- Task 34 ---
Task: search flight
task_info: {"origin": "Tel Aviv", "destination": "Venice", "trip_type": "round-trip", "departure_date": "May 9, 2026", "return_date": "June 16, 2026", "fare_type": "flexible"}

--- Task 35 ---
Task: retrieve flight status
task_info: {"flight_number": "#039028", "action_after_retrieve": "save to user profile"}

--- Task 36 ---
Task: locate flight status
task_info: {"origin": "Abidjan", "destination": "Accra", "status_type": "most recent updates"}

--- Task 37 ---
Task: find flight
task_info: {"trip_type": "round-trip", "origin": "Phoenix", "destination": "Miami", "maximum_budget": 2000, "departure_date": "May 10, 2026", "return_date": "June 18, 2026"}

--- Task 38 ---
Task: locate and reserve flight
task_info: {"origin": "London", "destination": "New York", "date_range": "June 2026", "arrival_time_window": {"start": "8:00 PM", "end": "11:00 PM"}, "reservation_priority": "shortest total travel time"}
