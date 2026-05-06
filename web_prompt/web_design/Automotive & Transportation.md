I need a website that serves as a complete automotive marketplace where people can easily shop for vehicles and auto parts. 

For the vehicle side, users should be able to explore new, used, and certified pre-owned cars based on their location, budget, preferred colors, and mileage. Once they find cars they are interested in, they should be able to compare different models, save their favorites to a personal wishlist, calculate estimated auto loan payments, and schedule test drives directly. They also need to be able to read dealer reviews to feel confident about their purchase, and get cash offers on their current cars by providing details like the VIN, mileage, and condition. 

For the auto parts section, users need a straightforward way to find specific components—like brake rotors, radiators, custom wheels, or sensors—and verify that these parts are perfectly compatible with their exact vehicle. They should be able to compare prices and shipping options across different sellers to find the best value, and then smoothly complete their purchase. 

The main goal is to create a one-stop destination where anyone can research, compare, and buy the right car or the right parts without any hassle.

The app you build must support the following tasks:
--- Task 1 ---
Task: purchase product
task_info: {"product": "E450 parking brake rotor and brake pad kit"}

--- Task 2 ---
Task: purchase product
task_info: {"product": "radiator", "vehicle": "1995 Ford F-350 Powerstroke 7.3"}

--- Task 3 ---
Task: purchase product
task_info: {"product": "intake coolant hoses", "material": ["molded", "silicone"]}

--- Task 4 ---
Task: purchase product
task_info: {"product": "14 x 38 double bevel rims", "color": "JD yellow", "additional_item": "mount hub"}

--- Task 5 ---
Task: purchase product
task_info: {"product": "22-inch IROC wheels", "additional_item": "lug nuts"}

--- Task 6 ---
Task: compare products
task_info: {"product": "front coil spring boosters/spacers", "attributes_to_compare": ["part numbers", "prices"]}

--- Task 7 ---
Task: compare product prices
task_info: {"product": "replacement Hyundai Genesis grille", "attributes_to_specify": ["price", "part number"]}

--- Task 8 ---
Task: compare shipping options
task_info: {"product": "Pro Lift lawn mower jack", "attributes_to_compare": ["delivery times"]}

--- Task 9 ---
Task: find msrp
task_info: {"product": "GM Genuine 84440529 Side Object Sensor Module", "action": "price comparison with alternative sources"}

--- Task 10 ---
Task: find retailers
task_info: {"product": "GM part number 84440529", "retailer_info": ["prices in ascending order"]}

--- Task 11 ---
Task: compare product prices
task_info: {"product": "FRAM CV10134 TrueAir Premium cabin air filter", "vehicle": "2012 Honda Civic", "action": "identify cheaper retailer"}

--- Task 12 ---
Task: compare products
task_info: {"product": "steel water troughs", "attributes_to_compare": ["pricing", "capacity (gallons)", "value per gallon"]}

--- Task 13 ---
Task: find locations
task_info: {"dealer_type": "used car dealer", "rating": "second best", "distance_max": "5 miles", "location_reference": "New York"}

--- Task 14 ---
Task: browse car listings
task_info: {"location": "Kentwood, MI 49512"}

--- Task 15 ---
Task: browse inventory
task_info: {"vehicle_model": "Model Y", "features": ["performance all-wheel drive"]}

--- Task 16 ---
Task: find car
task_info: {"vehicle_model": "Chevrolet Silverado", "color": "black", "price_max": 30000}

--- Task 17 ---
Task: search car
task_info: {"vehicle_model": "Honda Crosstour", "year_range": [2012, 2013], "location": "ZIP code 49102", "price_max": 25000, "attribute": "lowest mileage"}

--- Task 18 ---
Task: find car and schedule test drive
task_info: {"vehicle_type": "manufacturer-certified truck", "distance_max": "10 miles", "location": "zip 42701", "test_drive_details": {"name": "James Smith", "date": "May 17, 2026", "time": "4 pm"}}

--- Task 19 ---
Task: find car
task_info: {"vehicle_type": "hatchback", "location": "Madison", "interior_color": "red", "features": ["heated seat", "premium sound system"], "attribute": "cheapest"}

--- Task 20 ---
Task: find car
task_info: {"model": "2013 135", "price_max": 4000, "attributes": ["seller info", "seller's notes"]}

--- Task 21 ---
Task: find car
task_info: {"attribute": "cheapest", "distance_max": "50 miles", "location": "ZIP 21122"}

--- Task 22 ---
Task: find car
task_info: {"attribute": "best deal", "condition": "used"}

--- Task 23 ---
Task: find car
task_info: {"model": "Model S", "condition": "used", "color": "red"}

--- Task 24 ---
Task: find car
task_info: {"model": "RX350", "condition": "certified pre-owned", "color": "white", "year": 2026, "location": "ZIP code 90012", "attribute": "lowest price"}

--- Task 25 ---
Task: search car
task_info: {"drive_type": "front-wheel drive", "certification": "third-party certified", "year_range": [null, 2026], "condition": "white", "location": "Tampa, Florida", "features": ["online paperwork", "no accidents"], "attribute": "cheapest", "action": "confirm availability"}

--- Task 26 ---
Task: find car
task_info: {"condition": "new", "fuel_type": "electric", "attribute": "cheapest", "action": "highest EV mile range per charge"}

--- Task 27 ---
Task: compare mileage
task_info: {"vehicle_type": "used crossovers", "comparison_targets": ["first two cars"]}

--- Task 28 ---
Task: compare listings
task_info: {"vehicle_type": "sports car", "color": "grey", "fuel_type": "gas", "drive_type": "automatic", "year_range": [2026, 2026], "price_attribute": "lowest", "features": ["free shipping"], "action": "compare photos of top results"}

--- Task 29 ---
Task: find car
task_info: {"model": ["Series 1", "Series 2"], "location": "store nearest to postal code 07055"}

--- Task 30 ---
Task: browse car listings
task_info: {"type": "convertible", "price_max": 20000}

--- Task 31 ---
Task: browse car listings
task_info: {"model": "2006 Civic", "condition": "used"}

--- Task 32 ---
Task: find and add to cart
task_info: {"product": "spare parts", "part_number": 105307, "quantity": 2}

--- Task 33 ---
Task: find car
task_info: {"attribute": "lowest mileage", "location": "ZIP code 08817", "shipping_cost_max": 99, "price_range": [20000, 30000]}

--- Task 34 ---
Task: browse car listings
task_info: {"location": "near ZIP 10019", "sort_by": "cheapest"}

--- Task 35 ---
Task: search car
task_info: {"distance_max": "250 miles", "location": "ZIP code 26807"}

--- Task 36 ---
Task: review product
task_info: {"product": "2026 Audi A6"}

--- Task 37 ---
Task: find car
task_info: {"model": "specific model", "condition": "certified pre-owned", "drive_type": "front-wheel drive", "ownership": "single owner", "attribute": "lowest mileage", "distance_max": "500 miles", "location": "ZIP code 59316"}

--- Task 38 ---
Task: search car
task_info: {"model": "Jaguar XF", "color_excluded": "black", "action": "save search with daily notification"}

--- Task 39 ---
Task: schedule test drive
task_info: {"action": "open scheduling page"}

--- Task 40 ---
Task: browse accessories
task_info: {"attribute": "best seller", "vehicle_model": "specific model"}

--- Task 41 ---
Task: schedule demo drive
task_info: {"person": {"name": "Roy Adams", "phone": "123-999-0000", "email": "RA@gmail.com"}, "location": {"zip_code": "90001", "country": "United States"}}

--- Task 42 ---
Task: find car offer
task_info: {"model": "Honda", "color": "black", "VIN": "1HGCM66543A064159", "mileage": 155000, "location": "near 49102", "condition_criteria": ["good condition", "no damage", "2+ keys", "paid off"]}

--- Task 43 ---
Task: find review
task_info: {"product": "electric SUV", "rating": "1-star", "action": "mark helpful"}

--- Task 44 ---
Task: find and save car
task_info: {"model": "Mustang", "attribute": "lowest price"}

--- Task 45 ---
Task: find dealer
task_info: {"brand": "Cadillac", "rating_min": 4, "distance_max": "20 miles", "location": "ZIP code 60606"}

--- Task 46 ---
Task: compare vehicles
task_info: {"models": ["Acura CL 2003", "Acura ILX 2026"]}

--- Task 47 ---
Task: calculate loan and find car
task_info: {"price": 15000, "down_payment": 2000, "loan_terms": {"months": 48, "credit_type": "average"}, "location": "ZIP 65215", "action": "shop for lowest-priced car"}

--- Task 48 ---
Task: compare vehicles
task_info: {"year": 2026, "action": "omit similarities"}

--- Task 49 ---
Task: find car
task_info: {"model": "Porsche 911", "condition": "certified pre-owned", "year_min": 2026, "distance_max": "200 miles", "location": "ZIP code 97007", "price_attribute": "cheapest"}

--- Task 50 ---
Task: find car
task_info: {"vehicle_type": "large van", "year_min": 2026, "mileage_max": 10000}
