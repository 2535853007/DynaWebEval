I want to build a platform where people can easily discover and interact with local businesses in their area. Users should be able to search for anything from a nearby deli with great menu options, to a shipping center where they can drop off a package or find a notary. 

The site needs to let users narrow down their choices based on exactly what they are looking for. For example, they might want to find an affordable Kosher restaurant, a dog-friendly coffee shop with Wi-Fi, or a local storage facility with climate control. When viewing a business, users should be able to see everything it offers—like browsing a restaurant's menu to find the cheapest or most popular dish, checking store hours, or reading customer reviews. 

Once they find the perfect place, users should be able to take action directly. They need the ability to order food for delivery, reserve a table for a group, get driving directions, or save their favorite spots to a shortlist so they can easily compare them later. Ultimately, I want it to be a simple, all-in-one destination for finding and connecting with neighborhood stores and services.

The app you build must support the following tasks:
--- Task 1 ---
Task: search deli
task_info: {"location": "Downtown Denver", "menu_focus": "most meat-filled option"}

--- Task 2 ---
Task: search menu
task_info: {"menu_focus": "vegetarian item", "location": "Bainbridge"}

--- Task 3 ---
Task: search menu
task_info: {"menu_focus": "famous pancake options", "location": "Hyde Park"}

--- Task 4 ---
Task: search dishes
task_info: {"menu_type": ["meat-based", "rice", "noodle"], "price_focus": "cheapest", "location": "McKinney, TX"}

--- Task 5 ---
Task: search specials
task_info: {"location": "Henderson Harbor, NY"}

--- Task 6 ---
Task: search menu
task_info: {"menu_focus": "most expensive dish", "location": "Morristown, NJ"}

--- Task 7 ---
Task: search menu
task_info: {"menu_categories": ["chicken wings", "drinks"], "location": "Lake George"}

--- Task 8 ---
Task: search menu
task_info: {"menu_focus": "most popular dish", "location": "Fleet Street, London"}

--- Task 9 ---
Task: search store
task_info: {"services": ["notary public", "packaging supplies"], "radius_miles": 10, "location": "zip code 60504"}

--- Task 10 ---
Task: search location
task_info: {"task_focus": "return package", "location": "near zip code 10019", "staffed": true}

--- Task 11 ---
Task: search location
task_info: {"location": "Anchorage, Alaska", "requirements": ["small storage units", "climate-controlled"]}

--- Task 12 ---
Task: retrieve drop-off time
task_info: {"location": "near zip code 49103"}

--- Task 13 ---
Task: manage store
task_info: {"location": "Tempe, Arizona", "actions": ["set as my store", "visit store page", "view in-store events"]}

--- Task 14 ---
Task: search location
task_info: {"location_type": "in-store", "radius_miles": 50, "location": "21122"}

--- Task 15 ---
Task: search restaurant
task_info: {"cuisine": "Italian", "location": "New York City near Central Park"}

--- Task 16 ---
Task: search restaurant
task_info: {"location": "Big Sur, CA", "seating_type": "outdoor seating"}

--- Task 17 ---
Task: search restaurant
task_info: {"cuisine": "Kosher", "requirements": ["high rating"], "location": "San Francisco"}

--- Task 18 ---
Task: search restaurant
task_info: {"cuisine": "pizza", "capacity": 6, "location": "near current location"}

--- Task 19 ---
Task: search cafe
task_info: {"amenities": ["wifi"]}

--- Task 20 ---
Task: search restaurant
task_info: {"location": "Greenville, SC"}

--- Task 21 ---
Task: search restaurant
task_info: {"cuisine": "Thai", "actions": ["takeout"], "requirements": ["fully vaccinated staff", "accepts contactless payment"], "rating_focus": "best-rated", "location": "Westminster, California"}

--- Task 22 ---
Task: search restaurant
task_info: {"cuisine": "pasta", "location": "Sydney", "actions": ["save information"]}

--- Task 23 ---
Task: show map
task_info: {"map_focus": "Cleveland's animal shelters"}

--- Task 24 ---
Task: search restaurant
task_info: {"cuisine": "pizza", "location": "near Atlanta"}

--- Task 25 ---
Task: search restaurant
task_info: {"menu_focus": "burgers", "location": "zip code 44012", "sort_order": "highest ratings"}

--- Task 26 ---
Task: search bookstore
task_info: {"location": "Chelsea area"}

--- Task 27 ---
Task: search restaurant
task_info: {"cuisine": "African", "location": "East Village", "price_max": 30}

--- Task 28 ---
Task: search store
task_info: {"location": "near Cincinnati, Ohio", "services": ["coffee shop"]}

--- Task 29 ---
Task: search store
task_info: {"store_size": "large", "products": ["kids'", "maternity"], "location": "Washington"}

--- Task 30 ---
Task: search store
task_info: {"location": "Spring, Texas"}

--- Task 31 ---
Task: browse cafe
task_info: {"seating_type": "outdoor seating", "features": ["dog friendly"]}

--- Task 32 ---
Task: search restaurant
task_info: {"menu_focus": "Hot Dogs", "location": "Oakland, CA", "delivery": true}

--- Task 33 ---
Task: search store
task_info: {"location": "zip code 90028"}

--- Task 34 ---
Task: search farmers market
task_info: {"actions": ["choose two fruits", "choose one sauce"], "deal_focus": true}

--- Task 35 ---
Task: search store
task_info: {"location": "Chicago, IL"}

--- Task 36 ---
Task: search location
task_info: {"post_office_box_size": 4, "location": "zip code 54620"}

--- Task 37 ---
Task: search gas station
task_info: {"location": "Manhattan, NY", "rating_min": 4.0, "sort_criteria": "user reviews by lowest rating"}
