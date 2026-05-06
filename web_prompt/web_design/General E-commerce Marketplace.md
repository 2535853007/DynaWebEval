I need a website for a general online marketplace where people can shop for all kinds of products, from home goods to pantry staples. Shoppers should be able to browse trending daily deals, discover best-selling items, and easily compare different products to find the best price or size for their needs. 

The buying process should be smooth, allowing users to add things to their cart, confirm their shipping details, and check out securely. I also want a dedicated feature for digital gift cards, where customers can select a value, pick a fun design, write a personalized message, and email it directly to the recipient. 

As users browse, they should be able to create custom collections—like a wishlist for future birthday gifts or a list of saved deals—and easily add or remove items from their personal profiles. Lastly, it is important that people can easily manage their post-purchase experience. They need a simple way to look up the status of their past orders using their email and order number, as well as easily find instructions for returning items they no longer want.

The app you build must support the following tasks:
--- Task 1 ---
Task: purchase product
task_info: {"product": "metal cake stand"}

--- Task 2 ---
Task: compare product prices
task_info: {"product": "red indoor/outdoor electric grill", "capacity": "12 servings", "criteria": "cheaper"}

--- Task 3 ---
Task: compare product prices and dimensions
task_info: {"product": "outdoor drop box mailboxes", "criteria": ["bigger", "cheaper"]}

--- Task 4 ---
Task: compare product attributes
task_info: {"product": "clothesline rope", "comparison_attributes": ["type", "material", "length", "diameter", "weight capacity"], "retailers_count": 2}

--- Task 5 ---
Task: find product and recipe
task_info: {"product_category": "pantry staple item", "rank": 3, "recipe_criteria": {"includes_ingredient": "item"}, "output": ["recipe_name", "ingredients_list"]}

--- Task 6 ---
Task: send e-gift card
task_info: {"design": "Congrats", "message": "Best Wishes", "recipient_name": "James Smith", "recipient_email": "abc@abc.com"}

--- Task 7 ---
Task: locate webpage
task_info: {"content": "instructions for returning orders online"}

--- Task 8 ---
Task: retrieve order details
task_info: {"order_number": "12345", "email": "12345@gmail.com"}

--- Task 9 ---
Task: start purchase
task_info: {"product": "gift card"}

--- Task 10 ---
Task: create product collection
task_info: {"collection_name": "Future Birthday Gifts"}

--- Task 11 ---
Task: purchase gift card
task_info: {"amount": 25, "type": "digital", "recipient_name": "Tim Stebee", "recipient_email": "scisoorbros@gmail.com", "sender_name": "Jeerimiah Waton"}

--- Task 12 ---
Task: find deals
task_info: {"location": "New York"}

--- Task 13 ---
Task: purchase gift cards
task_info: {"amount_each": 100, "count": 2, "type": "digital", "design": "birthday card", "message": "Happy Birthday Love", "recipients": "two recipients via their email addresses"}

--- Task 14 ---
Task: browse deals
task_info: {"type": "trending daily deals"}

--- Task 15 ---
Task: save deals
task_info: {"location": "US", "count": 2, "offer_type": "deals and offers"}
