I need a comprehensive food and dining platform where people can seamlessly handle everything from grocery shopping to restaurant reservations. 

For grocery shopping and takeout, users should be able to browse everyday items—like fresh produce, snacks, baking supplies, and prepared takeout meals—add them to a shopping cart, and securely check out. They should also be able to compare product prices across different stores to find the best deals, check stock availability by zip code, and schedule a convenient same-day delivery or pickup time.

On the dining side, users need to discover restaurants based on location, cuisine, or atmosphere. They should be able to look through menus to spot specific dishes or dietary options, such as vegetarian meals or allergy-safe foods. I want them to easily book tables for specific dates, times, and party sizes, or even get notified when a table opens up at a popular spot.

Finally, the platform needs user profiles where people can save their favorite wines, groceries, or meals, bookmark restaurants they want to try, track their order history, and manage their budgets. The entire experience of finding food, ordering, and paying should feel incredibly smooth from start to finish.

The app you build must support the following tasks:
--- Task 1 ---
Task: order product
task_info: {"quantity": 20, "product": "disposable plastic bowls"}

--- Task 2 ---
Task: purchase product
task_info: {"quantity": 12, "product": "Snack Pack sugar-free pudding", "unit": "cups"}

--- Task 3 ---
Task: purchase product
task_info: {"quantity": 4, "product": "lemonade", "unit": "bottles"}

--- Task 4 ---
Task: ensure delivery
task_info: {"product": "Heinz Apple Cider Vinegar", "zip_code": "32204", "store": "default"}

--- Task 5 ---
Task: book reservation
task_info: {"location": "Kenosha", "date": "June 10, 2026"}

--- Task 6 ---
Task: search dishes
task_info: {"food_type": ["spicy beef", "spicy chicken"], "availability": "takeout", "location": "Secaucus, NJ"}

--- Task 7 ---
Task: book reservation
task_info: {"location": "Tallahassee, FL", "date_range": "next three weekends", "time_range": "5:30 PM to 8 PM", "seating": "outdoor", "allergy": "peanut"}

--- Task 8 ---
Task: book reservation
task_info: {"type": "sports bar", "location": "Phoenix area", "date": "June 2, 2026", "time": "next free slot"}

--- Task 9 ---
Task: find menu item
task_info: {"food_type": "vegetarian", "menu_detail": "item and prices", "location": "Washington, DC"}

--- Task 10 ---
Task: list menu items
task_info: {"food_type": "lasagna", "location": "Downey, CA", "meal_time": "lunchtime"}

--- Task 11 ---
Task: list menu items
task_info: {"food_type": "chicken", "restaurant_type": "Indian bistro and bar", "location": "Colorado Springs"}

--- Task 12 ---
Task: book reservation
task_info: {"location": "Queens, NY", "passengers": 4, "date_options": ["Friday, May 15, 2026", "Saturday, May 16, 2026"]}

--- Task 13 ---
Task: list menu items
task_info: {"menu_detail": ["special drinks", "cuisine"], "location": "bar in Rockaway, NY"}

--- Task 14 ---
Task: list menu items
task_info: {"food_type": "American breakfast foods", "location": "Indio", "meal_time": ["breakfast", "lunchtime"]}

--- Task 15 ---
Task: confirm menu item
task_info: {"food_type": "duck", "location": "Carew St, Springfield, MA"}

--- Task 16 ---
Task: book reservation
task_info: {"location": "Fairmount Park, IL", "passengers": 6, "date": "Saturday, May 22, 2026", "time": "7:00 PM"}

--- Task 17 ---
Task: order cakes
task_info: {"quantity": 2, "occasion": "birthday", "location": "bakery in Quincy, MA", "budget_max": "100 USD"}

--- Task 18 ---
Task: find menu item
task_info: {"food_type": "vegetarian", "menu_detail": "item only", "location": "Cocoa Beach"}

--- Task 19 ---
Task: confirm venue type
task_info: {"type": "romantic restaurant", "location": "Saugatuck, MI", "reservation_details": {"passengers": 2, "date": "May 18, 2026", "time": "7:00 PM"}}

--- Task 20 ---
Task: book reservation
task_info: {"location": "Gaithersburg, MD", "date": "Sunday, May 10, 2026", "meal_type": "weekend brunch", "time": "11:00 AM"}

--- Task 21 ---
Task: book reservation
task_info: {"location": "Bloomington", "meal_time": "lunchtime", "date": "June 19, 2026"}

--- Task 22 ---
Task: order cake
task_info: {"location": "Lincoln, NE"}

--- Task 23 ---
Task: book reservation
task_info: {"location": "Thai restaurant in Asheville, NC", "date": "May 21, 2026", "time": "1:00 PM"}

--- Task 24 ---
Task: list healthy menu items
task_info: {"type": "pizza place", "location": "Tomah, WI"}

--- Task 25 ---
Task: assemble bakery order
task_info: {"location": "Irvine", "items": ["cakes", "pastries", "sandwiches"], "family_size": 3}

--- Task 26 ---
Task: find price
task_info: {"product": "dozen pasture-raised eggs"}

--- Task 27 ---
Task: compare price
task_info: {"product": "ribeye steak", "pricing_context": "includes quantity data"}

--- Task 28 ---
Task: compare price
task_info: {"product": "Food For Life Baking Co. cereal"}

--- Task 29 ---
Task: browse restaurant portfolio
task_info: {"cuisine": "Spanish", "task_steps": ["visit website", "add 4 popular items to cart", "proceed to checkout", "record prices"]}

--- Task 30 ---
Task: browse product
task_info: {"category": "coffee makers", "rating": "5 stars"}

--- Task 31 ---
Task: find product
task_info: {"product_category": "wine"}

--- Task 32 ---
Task: find product
task_info: {"product": "Easter sprinkles", "purpose": "baking"}

--- Task 33 ---
Task: shop pizza
task_info: {"type": "thin crust frozen pepperoni pizza", "delivery_type": "same-day", "quantity": 2}

--- Task 34 ---
Task: find product in stock
task_info: {"product": "tortillas", "quantity": 5, "pack_size": "12 pcs", "zip_code": "59901", "action": "view cart"}

--- Task 35 ---
Task: book featured table
task_info: {"passengers": 2}

--- Task 36 ---
Task: get table alert
task_info: {"cuisine": "Thai restaurant", "time_range": "5 to 7 PM"}

--- Task 37 ---
Task: add produce to cart
task_info: {"items": [{"product": "blueberries", "quantity": 1, "unit": "pack"}, {"product": "bananas", "quantity": 6}, {"product": "grape tomato", "quantity": 1}, {"product": "roma tomato", "quantity": 1}, {"product": "cilantro", "quantity": 1, "unit": "bundle"}], "delivery_date": "June 10, 2026", "delivery_time": "10:00 AM to 1:00 PM", "delivery_address": "default"}

--- Task 38 ---
Task: find cheapest product
task_info: {"product": "bananas"}

--- Task 39 ---
Task: browse weekly ad
task_info: {"view_type": "list"}

--- Task 40 ---
Task: search restaurants
task_info: {"location": "Concord, CA", "cuisine": "Mexican", "action": "start order"}

--- Task 41 ---
Task: find food delivery
task_info: {"cuisine": "American", "location": "New York", "party_size": 4, "date": "June 20, 2026", "time": "8 PM"}

--- Task 42 ---
Task: compare prices
task_info: {"product": "organic strawberries", "stores_count": 3, "action": "add lowest-price option to cart", "zip_code": "94105"}

--- Task 43 ---
Task: find frozen pizza
task_info: {"type": "vegetarian cheese", "price_min": 5, "price_max": 10}

--- Task 44 ---
Task: add combos for pickup
task_info: {"items": [{"combo": "Box Combo", "drink": "Diet Coke"}, {"combo": "Kids Combo", "drink": "milk"}], "location": "store near ZIP 10001", "pickup_date": "June 10, 2026", "pickup_time": "12:00 PM"}

--- Task 45 ---
Task: find wine page
task_info: {"product": ["highest critic-scored red wine", "highest critic-scored white wine"], "origin": "Oregon", "price_max": 40, "pairing": ["fish", "dessert"]}
