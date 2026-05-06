I want to build a comprehensive real estate platform where people can easily find their perfect property, whether they are looking to buy a home, rent an apartment, or invest in land and commercial spaces. 

Users should be able to search across different locations and narrow down their choices based on exactly what they need—like their budget, the number of bedrooms, specific amenities like central AC or a private pool, and neighborhood perks like being walkable or near top-rated schools. 

As they browse, people need a way to save their favorite properties to a personal wishlist, compare different options to see which is best, and remove ones they are no longer interested in. It is also important that users can deeply explore the properties through virtual tours and floor plans. 

When they are ready to take the next step, users should be able to easily find local real estate agents, directly contact property sellers, or start a rental application. I also want to include helpful tools for niche needs, like students looking for affordable housing near their school, a way to calculate rental affordability, and the ability to track properties going up for auction.

The app you build must support the following tasks:
--- Task 1 ---
Task: search property
task_info: {"type": "commercial property", "transaction_type": "sale", "location": "Alice, TX", "status": "new to market", "price_min": 300000, "price_max": 600000, "features": ["central AC"]}

--- Task 2 ---
Task: search rental
task_info: {"type": "rental property", "location": "Arcata, CA", "bedrooms_min": 2, "features": ["in-unit laundry", "walkable neighborhood"]}

--- Task 3 ---
Task: search property
task_info: {"type": "house", "transaction_type": "sale", "location": "Provo, UT", "bedrooms_min": 3, "status": "new to market", "features": ["mountain view"]}

--- Task 4 ---
Task: search property
task_info: {"type": "home", "location": "Chatham Hills, Westfield", "bedrooms_min": 4, "year_built_min": 2000, "features": ["near top-rated schools"]}

--- Task 5 ---
Task: search property
task_info: {"type": "home", "location": "Pittsburgh, PA", "bedrooms_min": 3, "bathrooms_min": 2, "status": "built after May 10, 2026", "features": ["river view", "walkable neighborhood"]}

--- Task 6 ---
Task: search property
task_info: {"type": "new homes", "transaction_type": "sale", "location": "Heath, TX", "bedrooms_min": 4, "status": ["new listings", "built after May 15, 2026"], "features": ["pool", "large lots"]}

--- Task 7 ---
Task: search property
task_info: {"type": "mobile home", "transaction_type": "buy", "location": "Houston, TX", "price_max": 500000, "bedrooms_min": 3, "bathrooms_min": 2, "availability_date": "June 22, 2026", "status": "move-in ready"}

--- Task 8 ---
Task: search property
task_info: {"type": "land", "transaction_type": "sale", "location": "Gun Barrel City, TX", "acreage_min": 0.5, "price_max": 500000, "availability_date": "after May 18, 2026"}

--- Task 9 ---
Task: search property
task_info: {"type": "townhome", "transaction_type": "sale", "location": "Bolingbrook, Illinois", "bedrooms_min": 3, "bathrooms_min": 2, "price_max": 400000, "status": "new to market by June 12, 2026"}

--- Task 10 ---
Task: search property
task_info: {"type": "house", "transaction_type": "sale", "location": "Bossier City, LA", "price_max": 300000, "bedrooms": 3, "bathrooms_min": 2, "availability_date": "June 25, 2026", "status": "small house"}

--- Task 11 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Denton", "bedrooms": 3, "bathrooms_min": 2, "status": "active listings", "features": ["2-car garage"], "availability_date": "June 14, 2026"}

--- Task 12 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Highland, MI", "bedrooms_min": 3, "bathrooms_min": 2, "lot_type": "large lot", "status": "listed after May 20, 2026"}

--- Task 13 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Staten Island, NY", "bedrooms_min": 4, "lot_type": "large lot", "features": ["near top-rated schools"], "availability_date": "June 21, 2026"}

--- Task 14 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Columbus, GA", "bedrooms_min": 4, "bathrooms_min": 2, "price_max": 400000, "features": ["central AC"], "status": "listed before June 18, 2026"}

--- Task 15 ---
Task: search property
task_info: {"type": "house", "transaction_type": "sale", "location": "Montesano, WA", "bedrooms_min": 3, "bathrooms_min": 2, "acreage_min": 0.5, "status": "new to market by June 8, 2026"}

--- Task 16 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Jenks, Oklahoma", "bedrooms_min": 3, "features": ["central AC", "large lot"], "availability_date": "June 13, 2026"}

--- Task 17 ---
Task: search rental
task_info: {"type": "house", "transaction_type": "rent", "location": "Morrow Rd area, Nashville, TN", "bedrooms": 3, "features": ["pet-friendly", "central AC"], "availability_date": "after May 22, 2026"}

--- Task 18 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Equinox Loop, Aiken, SC", "bedrooms_min": 4, "bathrooms_min": 2.5, "lot_type": "large lot", "features": ["central AC"], "availability_date": "June 18, 2026"}

--- Task 19 ---
Task: search rental
task_info: {"type": "commercial lots", "transaction_type": "rent", "location": "Brodheadsville, PA", "price_max": 500000, "acreage_min": 0.5, "status": "new to market by June 15, 2026"}

--- Task 20 ---
Task: search property
task_info: {"type": "home", "location": "Oviedo, Florida", "bedrooms": 3, "bathrooms_min": 2, "features": ["near top-rated schools"], "availability_date": "May 19, 2026"}

--- Task 21 ---
Task: search property
task_info: {"type": "home", "status": "new listings", "location": "Williamstown, NJ", "bedrooms_min": 4, "availability_date": "June 22, 2026"}

--- Task 22 ---
Task: search property
task_info: {"type": "home", "transaction_type": "sale", "location": "Omaha, NE", "bedrooms_min": 4, "lot_type": "large lot", "features": ["near top-rated schools"], "availability_date": "June 17, 2026"}

--- Task 23 ---
Task: search property
task_info: {"type": "farm", "transaction_type": "sale", "location": "Minnesota", "acreage_min": 0.5, "features": ["central AC", "price recently reduced"], "status": "move-in ready by June 10, 2026"}

--- Task 24 ---
Task: search property
task_info: {"type": "oceanfront property", "price_max": 500000, "bedrooms_min": 4, "features": ["water view", "new construction"], "availability_date": "June 16, 2026"}

--- Task 25 ---
Task: search property
task_info: {"type": "home", "location": "SW area of North Carolina", "bedrooms_min": 3, "bathrooms_min": 2, "year_built_min": 2000}

--- Task 26 ---
Task: manage favorites
task_info: {"action": "add to favorites", "location": "Chicago, IL", "features": ["virtual tour"]}

--- Task 27 ---
Task: search property
task_info: {"type": "houses", "transaction_type": "sale", "location": "Maryland", "price_max": 60000}

--- Task 28 ---
Task: search property
task_info: {"type": "farm land", "location": "Wilkes County, NC", "price_type": "lowest price"}

--- Task 29 ---
Task: search rental
task_info: {"type": "home", "transaction_type": "rent", "location": "Anchorage, Alaska", "price_max": 800, "price_unit": "$/month"}

--- Task 30 ---
Task: search property
task_info: {"type": "newly constructed home", "transaction_type": "sale", "radius_miles": 10, "location": "zip 11001", "price_min": 350000, "price_max": 550000, "type_category": "single family", "bedrooms": 1, "bathrooms": 1}

--- Task 31 ---
Task: manage wishlist
task_info: {"action": "save", "properties_quantity": 2, "location": "San Diego", "criteria": "lowest price"}

--- Task 32 ---
Task: filter property
task_info: {"type": "2-bedroom single-family home", "price_max": 700000, "sort_criteria": "cheapest"}

--- Task 33 ---
Task: search agents
task_info: {"location": "Fresno, California"}

--- Task 34 ---
Task: search property
task_info: {"type": "houses", "transaction_type": "sale", "location": "zip code 85747", "features": ["private pool"]}

--- Task 35 ---
Task: search property
task_info: {"type": "property", "location": "London", "features": ["bike storage", "gym facilities"], "criteria": "lowest price"}

--- Task 36 ---
Task: search property
task_info: {"type": "land", "transaction_type": "sale", "location": "Nashville, Tennessee"}

--- Task 37 ---
Task: search property
task_info: {"type": "homesite land", "transaction_type": "sale", "location": "New Mexico, Luna County", "status": "owner-financing", "listing_date": "listed in last 30 days as of June 15, 2026", "criteria": "cheapest land per acre", "contact_details": "seller"}

--- Task 38 ---
Task: search property
task_info: {"contact_details": "seller", "location": "land near Rocksprings, TX"}

--- Task 39 ---
Task: manage preferences
task_info: {"action": "favorite", "type": "3-bedroom homes", "features": ["pool"]}

--- Task 40 ---
Task: manage preferences
task_info: {"action": "save", "status": ["auction", "smallest area"], "type": "home", "location": "Oklahoma"}

--- Task 41 ---
Task: search property
task_info: {"contact_details": "seller", "type_property": "hunting land", "criteria": "cheapest", "location": "Georgia"}

--- Task 42 ---
Task: manage wishlist
task_info: {"action": "add to wishlist", "criteria": "lowest price near university"}

--- Task 43 ---
Task: search rental
task_info: {"type": "entire place for rent", "availability_exclusive": "students", "proximity": "closest to a language school"}

--- Task 44 ---
Task: search rental
task_info: {"type": "single-family house for rent", "location": "Houston, TX", "bedrooms": 1}

--- Task 45 ---
Task: search property
task_info: {"type": "apartment", "criteria": ["cheapest", "student-specific"], "location": "Detroit"}
