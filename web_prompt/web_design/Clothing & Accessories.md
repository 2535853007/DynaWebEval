I want to build an online clothing and accessories store where people can easily shop for everyday wear, activewear, shoes, and jewelry for the whole family. 

Users should be able to browse through a wide variety of items and pinpoint exactly what they need based on their exact size, favorite colors, specific budget, or top customer ratings. It is really important that shoppers can put together complete outfits or find complementary accessories, like pairing a vacation shirt with the perfect shorts, or finding the right socks to go with new sneakers. They should also be able to easily compare different products to find the best value and read up on specific item details, sizing guides, and return policies. 

The shopping experience needs to be smooth. Customers should be able to add items to their bag, adjust quantities, and see their final total with taxes clearly calculated. If they aren't ready to buy right away, they should have the option to save items for later or create a wishlist. Finally, they need a simple checkout process where they can choose between standard shipping, fast local pickup, and express payment options.

The app you build must support the following tasks:
--- Task 1 ---
Task: purchase product
task_info: {"brand": "Under Armour", "product": "Men's Project Rock BSR training shoes", "size": 8}

--- Task 2 ---
Task: purchase product
task_info: {"product": "Modern V-Neck T-Shirt", "color": "white", "size": "M"}

--- Task 3 ---
Task: purchase product
task_info: {"product": "navy shoes", "gender": "women", "size": 8}

--- Task 4 ---
Task: purchase product
task_info: {"brand": "Under Armour", "product": "Men's UA Base 4 long sleeve", "size": "M"}

--- Task 5 ---
Task: purchase product
task_info: {"product": "full-length leather coat", "gender": "women", "size": "S", "price_max": 200}

--- Task 6 ---
Task: purchase product
task_info: {"brand": "Starter", "product": "Pittsburgh Steelers hoodie"}

--- Task 7 ---
Task: purchase product
task_info: {"products": [{"product": "mid-rise denim bermuda shorts", "size": 26}, {"product": "blue top", "size": "M"}]}

--- Task 8 ---
Task: purchase product
task_info: {"products": [{"product": "pump sneakers", "gender": "men", "size": 10}, {"product": "athletic socks", "color": "any"}]}

--- Task 9 ---
Task: purchase product
task_info: {"products": [{"brand": "Irish Setter", "product": "Kasota 6-inch work boots", "size": 9.5, "width": "regular"}, {"product": "brown chukka boots", "size": 9.5}]}

--- Task 10 ---
Task: purchase product
task_info: {"products": [{"brand": "Birkenstocks", "product": "Arizona style shoes", "color": "black", "gender": "women"}, {"product": "shoe care kit"}]}

--- Task 11 ---
Task: purchase product
task_info: {"products": [{"product": "Alabama vintage t-shirt"}, {"product": "Alabama Crimson Tide cap"}]}

--- Task 12 ---
Task: purchase product
task_info: {"products": [{"product": "black classic rock sweatshirt"}, {"product": "hat"}]}

--- Task 13 ---
Task: purchase product
task_info: {"products": [{"product": "heeled sandals", "gender": "women"}, {"product": "winter boots", "size": 8}]}

--- Task 14 ---
Task: purchase product
task_info: {"products": [{"product": "athletic cut jeans", "gender": "women", "size": 30, "date": "June 15, 2026"}, {"product": "medium wash straight cut jeans", "date": "June 18, 2026"}]}

--- Task 15 ---
Task: purchase product
task_info: {"products": [{"product": "men's knit nightshirt", "size": "Large", "date": "May 10, 2026"}, {"product": "slippers", "date": "June 14, 2026"}]}

--- Task 16 ---
Task: compare product
task_info: {"product": "men's golf swing flex cargo short", "attributes": ["price", "level of sun protection"]}

--- Task 17 ---
Task: compare product
task_info: {"product": "boys' black swim trunks", "attributes": ["price", "shipping costs", "delivery windows"]}

--- Task 18 ---
Task: compare product
task_info: {"product": "navy blazer", "attributes": ["price", "product details"]}

--- Task 19 ---
Task: compare product
task_info: {"product": "6-pack white undershirts", "attributes": ["price"]}

--- Task 20 ---
Task: compare product variety
task_info: {"product": "men's 7\" sweat shorts", "attribute": "colors"}

--- Task 21 ---
Task: compare product
task_info: {"product": "men's Adidas Stan Smith sneakers", "retailers": 2, "attributes": ["price", "best offer"]}

--- Task 22 ---
Task: browse catalog
task_info: {"category": "male outfits", "context": "beach vacation"}

--- Task 23 ---
Task: browse catalog
task_info: {"category": "large-sized men's winter coats", "status": "on clearance"}

--- Task 24 ---
Task: add to cart
task_info: {"product": "men's slim jeans", "size": "26*29"}

--- Task 25 ---
Task: filter product
task_info: {"category": "handbags", "sub_category": "evening bags", "color": "blue", "style": "embellished", "price_max": 50}

--- Task 26 ---
Task: search product
task_info: {"category": "girls' training leggings", "size": "YXL", "results_saved": 3}

--- Task 27 ---
Task: add to cart
task_info: {"products": [{"product": "green shirts", "quantity": 10, "attributes": ["lowest price"]}]}

--- Task 28 ---
Task: search product details
task_info: {"product": "Men's football short sleeve", "attribute": "return policy"}

--- Task 29 ---
Task: browse catalog
task_info: {"category": "shirts for sale"}

--- Task 30 ---
Task: display product
task_info: {"category": "women's athletic shoes", "attribute": "most popular"}

--- Task 31 ---
Task: search product
task_info: {"category": "men's shoes", "condition": "pre-owned", "size": 9, "pickup": "free local", "price_max": 75}

--- Task 32 ---
Task: purchase product
task_info: {"category": "women's running shoes", "condition": "used", "size": 5, "attributes": ["cheapest"]}

--- Task 33 ---
Task: search product
task_info: {"category": "women's sportswear", "size": "S"}

--- Task 34 ---
Task: browse catalog
task_info: {"category": "men's black hoodies", "size": "Big and Tall", "price_min": 25, "price_max": 50, "status": "best selling"}

--- Task 35 ---
Task: search product
task_info: {"category": "women's hiking shoes", "color": "brown", "size": 9, "location": "Columbus, Ohio", "condition": "new", "attributes": ["average rating above 4", "cheapest"]}

--- Task 36 ---
Task: display product
task_info: {"category": "gender-neutral skirts", "attribute": "best seller"}

--- Task 37 ---
Task: add to cart
task_info: {"product": "diamond stud earrings"}

--- Task 38 ---
Task: search and add
task_info: {"category": "men's running shoes", "size": 9, "attributes": ["lowest price"]}

--- Task 39 ---
Task: filter product
task_info: {"category": "women's sports bras", "color": "purple", "support": "high", "size": "small"}

--- Task 40 ---
Task: browse and add to wishlist
task_info: {"category": "women's sports bras", "status": "trending", "quantity": 3, "color": "black"}

--- Task 41 ---
Task: search product details
task_info: {"type": "Men's size guide for bottoms"}

--- Task 42 ---
Task: search and add
task_info: {"category": "women's one-piece swimsuits", "color": "black", "size": "large", "attribute": "highest discount percentage"}

--- Task 43 ---
Task: display product
task_info: {"category": "Men's Blazers", "color": "Black", "size": "M"}

--- Task 44 ---
Task: add to cart
task_info: {"category": "men's clogs", "color": "brown", "size": "10-10.5", "status": "top-selling"}
