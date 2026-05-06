I want to build a platform where people can easily discover and buy tickets for live events like concerts, comedy shows, and sports games. Users should be able to look up events happening in specific cities, within a certain distance, or on specific dates, like finding something to do this weekend or planning a trip for next summer. They need to be able to find their favorite artists or simply browse by genres like hip-hop, classic rock, or professional boxing. 

When booking, users should see transparent pricing that includes any estimated fees. They need the ability to choose specific seating areas, whether they want VIP access, floor tickets near the stage, or seats in the upper sections, and they should be able to add extras like a reserved parking spot. 

I also want users to have a personal profile where they can safely store their purchased tickets, set up reminders for upcoming shows, and even see who else is attending an event so they can connect and follow them. The checkout process must be straightforward, whether someone is buying a ticket for themselves, picking up a few for their family, or purchasing them as a gift. Finally, there should be an accessible help section to explain common questions, like how event presales work.

The app you build must support the following tasks:
--- Task 1 ---
Task: buy tickets
task_info: {"event_name": "Celebration Belle Riverfest", "year": 2026, "quantity": 3, "attendees": ["me", "parents"], "notification": true}

--- Task 2 ---
Task: buy tickets
task_info: {"event_name": "Barrington Levy concert", "location_radius": "50-mile radius of Cincinnati, OH", "notification": true, "online_purchase": true}

--- Task 3 ---
Task: buy tickets
task_info: {"location": "Shoreline Amphitheatre", "city": "Mountain View", "state": "CA", "event_type": "upcoming event", "notification": true}

--- Task 4 ---
Task: buy tickets
task_info: {"event_name": "Buckeye Countryfest", "notification": true}

--- Task 5 ---
Task: find tickets
task_info: {"event_name": "Amy Grant concert", "price_min": 200, "price_max": 300}

--- Task 6 ---
Task: book tickets
task_info: {"event_name": "Kevin Hart show", "quantity": 4, "section": "upper", "location": "Brisbane, Australia", "deadline": "June 30, 2026", "view_prices": true}

--- Task 7 ---
Task: browse tickets
task_info: {"event_type": "concert", "location": "Mexico", "date": "May 26, 2026", "view_prices": true}

--- Task 8 ---
Task: find tickets
task_info: {"event_name": "Taylor Swift concert", "ticket_selection": true}

--- Task 9 ---
Task: find and book tickets
task_info: {"event_name": "Celine Dion concert", "quantity": 3, "ticket_type": "Golden Circle", "country": "France", "date": "June 15, 2026", "paper_tickets": true, "view_prices": true}

--- Task 10 ---
Task: find tickets
task_info: {"location": "Austin, Texas", "date": "May 23, 2026", "quantity": 1}

--- Task 11 ---
Task: check parking
task_info: {"event_type": "concert"}

--- Task 12 ---
Task: find tickets
task_info: {"price": 200, "quantity": 1, "event_type": "game", "week": 23, "date": "June 10, 2026"}

--- Task 13 ---
Task: browse tickets
task_info: {"section": "floor", "event_type": "game", "date": "May 22, 2026"}

--- Task 14 ---
Task: search tickets
task_info: {"ticket_type": "VIP", "quantity": 4, "event_type": "concert", "location": "Australia", "date": "June 8, 2026"}

--- Task 15 ---
Task: check ticket listing
task_info: {"section": "Floor B", "row": 17, "seat_number": "listing", "event_type": "music concert", "date_time": "Mon August 14, 2026, 7:00 pm"}

--- Task 16 ---
Task: show events
task_info: {"location": "Phoenix", "date_range": "next 3 days"}

--- Task 17 ---
Task: browse concerts
task_info: {"genre": "hip hop", "date_range": "this weekend"}

--- Task 18 ---
Task: find tickets
task_info: {"location": "Boston", "event_type": "events"}

--- Task 19 ---
Task: find events
task_info: {"artist": "Coldplay", "location": "Columbus, OH", "date": "May 17, 2026"}

--- Task 20 ---
Task: browse concert tickets
task_info: {"genre": "classic rock"}

--- Task 21 ---
Task: search events
task_info: {"genre": "comedy", "location": "Chicago, IL", "date": "June 15, 2026", "expand_results": true}

--- Task 22 ---
Task: find events
task_info: {"genre": "music", "location": "Los Angeles", "date": "June 10, 2026"}

--- Task 23 ---
Task: book tickets
task_info: {"quantity": 2, "ticket_as_gift": true, "event_info": ["Dave Chappelle stand-up", "The Roots concert"]}

--- Task 24 ---
Task: browse events
task_info: {"location_type": "arena or event center"}

--- Task 25 ---
Task: book tickets
task_info: {"price_min": 50, "price_max": 100}

--- Task 26 ---
Task: select tickets
task_info: {"event_type": "similar to professional boxing"}

--- Task 27 ---
Task: find events
task_info: {"genre": "rock music", "location": "Canada", "date": "June 13, 2026", "save_top_events": 3}

--- Task 28 ---
Task: find events
task_info: {"date_start": "May 1, 2026", "distance": "100 miles of New York", "social_interactions": {"follow_attendees": "top listed event"}}

--- Task 29 ---
Task: find information
task_info: {"topic": "how presale works"}

--- Task 30 ---
Task: find tickets
task_info: {"event_name": "Lady Gaga concert", "location": "New York", "date_range": "June 2026", "quantity": 4, "proximity": "close to the stage", "calculate_total_price": true}
