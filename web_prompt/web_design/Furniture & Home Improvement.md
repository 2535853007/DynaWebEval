I want to build an online store where people can shop for everything related to furniture and home improvement, from large appliances and lumber to everyday items like rugs and seasonal decor. Customers should be able to easily find exactly what they need based on specific sizes, colors, materials, and their budget. 

It is important that shoppers can compare different products, read reviews, and see the differences in features to make informed decisions. When a user buys an item, the platform should naturally suggest helpful add-ons, like mounting hardware for a new bathroom sink or rollers for a can of paint. 

Shoppers need flexible fulfillment options, whether they want to schedule a home delivery for a specific date or check local inventory for store pick-up using their zip code. The site should also let people create personal accounts to save favorite items, organize specific project lists like "New Home", and keep track of their order history, warranties, and receipts all in one place. Finally, the checkout process should be incredibly simple, supporting quick guest purchases while letting users easily apply warranties or choose gift-wrapping options.

The app you build must support the following tasks:
--- Task 1 ---
Task: order product
task_info: {"type": "wall-hung bathroom sink", "dimensions": "14\" x 12\""}

--- Task 2 ---
Task: purchase product
task_info: {"type": "refrigerator", "feature": "built-in water dispenser"}

--- Task 3 ---
Task: buy product
task_info: {"type": "rug", "color": "green", "size": "8'x10'", "alternative_size": "something close"}

--- Task 4 ---
Task: order product
task_info: {"type": "freezer", "capacity": "18 cu ft", "price": "cheapest"}

--- Task 5 ---
Task: purchase product
task_info: {"type": "sectional sofa", "style": "Chesterfield", "length": "90'", "color": "light"}

--- Task 6 ---
Task: purchase product
task_info: {"type": "dining table", "shape": "rectangular", "style": "drop leaf", "length_min": "54\""}

--- Task 7 ---
Task: purchase product
task_info: {"type": "cotoneaster plant"}

--- Task 8 ---
Task: purchase product
task_info: {"type": "hammock chair", "feature": "with stand"}

--- Task 9 ---
Task: purchase product
task_info: {"type": "Gemini Bed"}

--- Task 10 ---
Task: purchase product
task_info: {"type": "window curtains", "color": "turquoise and orange", "style": "Bohemian Stripe"}

--- Task 11 ---
Task: purchase product
task_info: {"type": "shelving", "tier": 4, "material": "chrome", "dimensions": {"width": "35 inches", "height": "50 inches"}}

--- Task 12 ---
Task: purchase product
task_info: {"type": "photo frame", "material": "ceramic"}

--- Task 13 ---
Task: add to cart
task_info: {"products": [{"type": "semi-gloss Acrylux Exterior Paint"}, {"type": "painting tools", "examples": ["brushes", "rollers"]}]}

--- Task 14 ---
Task: purchase product
task_info: {"products": [{"type": "toilet", "dimensions": "19-inch high", "color": "white"}, {"type": "electric bidet seat"}]}

--- Task 15 ---
Task: purchase product
task_info: {"products": [{"type": "clock hands", "size": "8-inch extra fancy large"}, {"type": "cleaning tool", "specific": "brass brush"}]}

--- Task 16 ---
Task: purchase product
task_info: {"products": [{"type": "rug", "dimensions": "9'x12'", "usage": "indoor/outdoor", "shape": "rectangular"}, {"type": "kitchen mat", "dimensions": "18-inch by 30-inch"}]}

--- Task 17 ---
Task: purchase product
task_info: {"products": [{"type": "dinnerware set", "quantity": 12, "variety": "mixed"}, {"type": "luncheon plate", "color": ["blue", "green"]}]}

--- Task 18 ---
Task: purchase product
task_info: {"products": [{"type": "T-nuts", "size": "1/4-20", "quantity_max": "100"}, {"type": "softwood threaded inserts", "size": "1/4-20"}]}

--- Task 19 ---
Task: purchase product
task_info: {"products": [{"type": "adhesive", "material": "silicone", "purchase_date": "May 14, 2026"}, {"type": "caulking gun", "feature": "dripless", "usage_date": "June 20, 2026"}]}

--- Task 20 ---
Task: calculate cost
task_info: {"products": [{"type": "vinyl outside corner trim", "attribute": "standard length"}]}

--- Task 21 ---
Task: compare prices
task_info: {"type": "towel bar", "feature": "3-arm wall-mounted pivoting"}

--- Task 22 ---
Task: compare prices
task_info: {"type": "garage door opener", "feature": "direct drive wireless keypad"}

--- Task 23 ---
Task: compare specifications
task_info: {"type": "ant killer baits", "details": ["price", "number per box"]}

--- Task 24 ---
Task: compare options
task_info: {"type": "Samsung laundry pedestal storage drawer", "dimensions": "27-inch", "attribute": "available color options"}

--- Task 25 ---
Task: compare prices
task_info: {"type": "Marey 2.0 GPM Electric Tankless Water Heater"}

--- Task 26 ---
Task: compare pricing
task_info: {"type": "topsoil", "attributes": ["bulk pricing", "package sizes"]}

--- Task 27 ---
Task: calculate cost difference
task_info: {"products": [{"type": "timber", "dimensions": "4-in x 6-in x 12-ft, pressure-treated ground-contact southern pine"}, {"type": "timber", "dimensions": "4 x 4 x 10 ft"}]}

--- Task 28 ---
Task: compare specifications
task_info: {"type": "bedspreads", "size": "California King", "color": "burgundy", "attributes": ["material", "fill weight", "care instructions", "dimensions"], "comparison_format": "table"}

--- Task 29 ---
Task: locate product
task_info: {"type": "backlit poster", "dimensions": "24x36 inches"}

--- Task 30 ---
Task: find price
task_info: {"type": "twin mattress", "attribute": "best organic", "target_audience": "kids"}

--- Task 31 ---
Task: compare products
task_info: {"type": "bedroom nightstand", "material": "solid wood", "count_highest_rated": 3, "comparison_scope": "differences only"}

--- Task 32 ---
Task: add to cart
task_info: {"type": "bed sheets", "size": "queen", "rating_min": 4}

--- Task 33 ---
Task: add to cart
task_info: {"type": "swivel vacuum", "price_max": 150}

--- Task 34 ---
Task: create list
task_info: {"list_name": "New Home", "added_product": {"type": "recliner chair", "price": "cheapest"}}

--- Task 35 ---
Task: show deals
task_info: {"type": "kitchen products", "material": "aluminum", "sale_only": true}

--- Task 36 ---
Task: find product
task_info: {"type": "multi-purpose painting tool", "availability": {"pickup_zip": 44240}}

--- Task 37 ---
Task: add to cart
task_info: {"type": "LED smart home indoor strip lighting", "price": "cheapest", "delivery_schedule": true}

--- Task 38 ---
Task: add to cart
task_info: {"type": "decorative LED candles"}

--- Task 39 ---
Task: locate product
task_info: {"type": "wall mirrors", "price_max": "$20"}

--- Task 40 ---
Task: find product
task_info: {"type": "trash can", "feature": "automated lid", "price_max": "$60", "condition": "new", "price": "cheapest"}

--- Task 41 ---
Task: show deals
task_info: {"type": "home essentials", "price_max": "$20", "favorites_quantity": 3}

--- Task 42 ---
Task: browse products
task_info: {"type": "candle holder red decor"}

--- Task 43 ---
Task: checkout product
task_info: {"type": "outdoor dining table", "availability": "limited-time offers", "price": "cheapest", "pickup_option": "store pickup", "guest_checkout": true}

--- Task 44 ---
Task: show products
task_info: {"type": "mattresses", "store_action": "follow"}

--- Task 45 ---
Task: find product
task_info: {"type": "bathroom baskets", "material": "plastic", "color": "gray", "price_sorting": "low to high", "location": {"near_zip": 60173}}

--- Task 46 ---
Task: find product
task_info: {"type": "antique Oak chair", "style": "French", "condition": "used", "manufacture_date_max": 1800, "listing_status": "newly listed"}

--- Task 47 ---
Task: search products
task_info: {"category_path": "Dining Room Sets > Furniture", "filter": {"listing_format": "Buy It Now"}}

--- Task 48 ---
Task: checkout product
task_info: {"type": "pillow protectors", "size": "queen", "quantity": 2}

--- Task 49 ---
Task: show products
task_info: {"type": "Easter home decor", "listing_status": "new arrivals"}

--- Task 50 ---
Task: find product
task_info: {"type": "electric dryers", "capacity_min": "7.3 cubic foot", "price_max": "$1000", "availability": "in store", "location": {"city": "Montgomery", "state": "Illinois", "zip": 60538}}
