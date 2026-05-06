I need a website where people can stay easily updated on public alerts, government news, and official reports. Users should be able to browse and read the latest press releases from federal departments, find local city council meeting livestreams, and research specific civic information like state minimum wages, historical government lists, or safety statistics. 

The platform needs to help people stay safe and informed by providing timely updates on regional health advisories, specific product recalls, local park or river conditions, and law enforcement notices. 

A major part of the site should be a personal space for the user. When someone finds an important document, like a yearly performance report or an interesting news article, they should be able to save it, add their own notes, and organize it for later reading. Users also need the ability to bookmark older press releases, track ongoing updates for specific alerts or safety notices, and pin important items to their profile so they can quickly check on them whenever they return to the site.

The app you build must support the following tasks:
--- Task 1 ---
Task: find meeting
task_info: {"organization": "City of Covington", "state": "Kentucky", "meeting_type": "board of commissioners", "output_format": "livestream source"}

--- Task 2 ---
Task: find news release
task_info: {"organization": "US Dept. of Labor", "details_requested": ["media contact", "contact count"]}

--- Task 3 ---
Task: find news
task_info: {"topic": "climate"}

--- Task 4 ---
Task: view list
task_info: {"list_type": "most wanted fugitives", "count": 15}

--- Task 5 ---
Task: locate publication
task_info: {"publisher": "attorney general", "filter": "latest"}

--- Task 6 ---
Task: find list
task_info: {"list_type": "Attorney Generals of the United States", "sort_order": "oldest to newest"}

--- Task 7 ---
Task: show report
task_info: {"report_name": "Annual Performance Report", "year": 2026}

--- Task 8 ---
Task: find out
task_info: {"details": null}

--- Task 9 ---
Task: display alerts
task_info: {"source": "health authorities", "filter": "latest"}

--- Task 10 ---
Task: find rate
task_info: {"rate_type": "minimum wage", "state": "California", "details_requested": "current rate"}

--- Task 11 ---
Task: find recalls
task_info: {"model": "4C"}

--- Task 12 ---
Task: retrieve alerts
task_info: {"location": "Alagnak Wild River", "details_requested": ["alerts", "conditions"]}

--- Task 13 ---
Task: find press releases
task_info: {"division": "antitrust", "month": "May", "year": 2026}

--- Task 14 ---
Task: find press release
task_info: {"filter": "earliest"}

--- Task 15 ---
Task: show figure
task_info: {"comparison": ["Occupational Fatalities Trends"], "locations": ["Ohio", "New York"]}
