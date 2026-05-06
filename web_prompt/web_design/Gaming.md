I need a website to serve as the ultimate gaming hub where users can discover, buy, and track their favorite games. Gamers should be able to easily explore top-selling hits, upcoming releases, free-to-play options, and specific genres like RPGs, VR titles, or even board games. I want them to find interesting details about any game, such as its release date, publisher, platform availability, or whether it has a TV show adaptation.

A massive part of the platform will revolve around guides and reviews. People need to read top-rated editor's choices, see what seasoned players with over 100 hours of playtime think, and vote on helpful feedback. They should also be able to look up step-by-step walkthroughs and save critical tips to get past tricky parts of a game. 

Additionally, users need personal profiles to manage their gaming lives. They should be able to build wishlists, organize personal collections, track their recently played titles, and pin their all-time favorites. Finally, the site needs a seamless store experience where users can add games and extra content like DLCs to their cart and securely check out.

The app you build must support the following tasks:
--- Task 1 ---
Task: find game
task_info: {"criteria": "top-selling", "date": "June 15, 2026", "tv_series_adaptation": true, "streaming_services": true}

--- Task 2 ---
Task: identify game
task_info: {"platform": "Xbox", "criteria": "top-selling", "details": ["publisher", "release_date"], "additional_calculation": "years_elapsed_between_ceo_birth_year_and_release_date"}

--- Task 3 ---
Task: find review
task_info: {"criteria": "editor's choice", "score": 10, "category": "boardgame"}

--- Task 4 ---
Task: find walkthrough
task_info: {"game_title": "The Legend of Zelda: Breath of the Wild"}

--- Task 5 ---
Task: find game
task_info: {"criteria": ["newest", "farming & crafting simulation"], "price": "free"}

--- Task 6 ---
Task: find game
task_info: {"availability": true, "price": "free", "rewards": true}

--- Task 7 ---
Task: provide guide
task_info: {"type": "walkthrough", "category": "video game"}

--- Task 8 ---
Task: show reviews
task_info: {"category": "computer game", "sort_by": "score"}

--- Task 9 ---
Task: display games
task_info: {"genre": "RPG", "category": "video game"}

--- Task 10 ---
Task: open list
task_info: {"list_type": "recently played games"}

--- Task 11 ---
Task: show games
task_info: {"criteria": "most played", "metric": "daily players"}

--- Task 12 ---
Task: show games
task_info: {"criteria": "most popular", "status": "upcoming releases"}

--- Task 13 ---
Task: locate game
task_info: {"platform": "PS5", "status": "upcoming", "release_date": "August 2026"}

--- Task 14 ---
Task: manage cart
task_info: {"action": "add all DLC", "status": "game found"}

--- Task 15 ---
Task: add to wishlist
task_info: {"criteria": "top-rated", "genre": "JRPG"}

--- Task 16 ---
Task: show reviews
task_info: {"game_title": "Fallout 4", "action_on_reviews": "mark first review as helpful"}

--- Task 17 ---
Task: display games
task_info: {"genre": "Massively Multiplayer", "features": ["Virtual Reality (VR)"]}

--- Task 18 ---
Task: find game
task_info: {"genre": "adventure", "status": "highest rated", "availability": "early access"}

--- Task 19 ---
Task: manage guide
task_info: {"game_title": "Uncharted: Legacy of Thieves Collection", "additional_query": "Queen's bracelet information"}

--- Task 20 ---
Task: find details
task_info: {"game_title": "Elden Ring", "details": ["release_date", "supported_platforms"]}

--- Task 21 ---
Task: add to collection
task_info: {"game_title": "Atlantis"}

--- Task 22 ---
Task: find reviews
task_info: {"game_title": "Cyberpunk 2077"}

--- Task 23 ---
Task: browse reviews
task_info: {"criteria": "negative", "player_playtime": {"min_hours": 100}, "award": "2026 VR Game of the Year"}

--- Task 24 ---
Task: browse reviews
task_info: {"criteria": ["top-played list", "past year"], "player_playtime": {"min_hours": 100}, "device_preference": true}

--- Task 25 ---
Task: identify game
task_info: {"category": "boardgame", "rating_min": 7.5, "criteria": "most popular", "player_count": 2}
