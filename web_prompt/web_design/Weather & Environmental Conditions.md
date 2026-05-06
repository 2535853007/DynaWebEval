I want to build a comprehensive weather and environmental tracking platform. Users should be able to easily check the weather for any city, zip code, or specific point of interest like local airports, national parks, and hiking trails. 

People need to see current weather conditions, along with hourly, daily, weekend, and monthly forecasts, even for specific future dates. The platform should go beyond basic temperatures—users need to look up wind speeds, humidity, precipitation, and detailed air quality data. 

Safety is a big priority, so the site must allow users to track active storms, read severe weather alerts, and check for outdoor hazards or trail closures. I also want them to be able to view visual radar and wind flow maps to monitor major weather events as they happen. 

Finally, the experience should be highly personalized. Users need the ability to save preferred locations, set an active home base, view their recent searches, and curate a personal space to monitor specific conditions, with the freedom to add or remove locations and bookmark maps whenever they want.

The app you build must support the following tasks:
--- Task 1 ---
Task: verify trail conditions
task_info: {"trail_name": "Lake Eiler Trail", "report_type": ["closures", "hazards"]}

--- Task 2 ---
Task: get weather alerts
task_info: {"region": "Nova Scotia, Canada", "alert_type": "severe weather"}

--- Task 3 ---
Task: check wind speed
task_info: {"location": "Calgary, Alberta"}

--- Task 4 ---
Task: retrieve hourly forecast
task_info: {"location": "Seattle, WA", "duration": "next 24 hours"}

--- Task 5 ---
Task: show weekend forecast
task_info: {"location": "Allenford", "date": "June 15, 2026"}

--- Task 6 ---
Task: check current temperature
task_info: {"location": "zip code 10019"}

--- Task 7 ---
Task: add location
task_info: {"location": "Miami, FL"}

--- Task 8 ---
Task: find active storms
task_info: {"report_type": "current status"}

--- Task 9 ---
Task: check daily forecast
task_info: {"location": "Madison, WI", "start_date": "May 21, 2026", "end_date": "June 1, 2026"}

--- Task 10 ---
Task: find weather details
task_info: {"location": "Tallahassee, FL", "parameters": ["wind speed", "humidity"], "date": "June 10, 2026"}

--- Task 11 ---
Task: find radar map
task_info: {"location": "Los Angeles, CA"}

--- Task 12 ---
Task: obtain monthly forecast
task_info: {"location": "Manchester, GB", "month": "May 2026"}

--- Task 13 ---
Task: check weather conditions
task_info: {"location": "Los Angeles"}

--- Task 14 ---
Task: view wind flow map
task_info: {"location": "Utah, United States", "display_options": {"contours": false}}

--- Task 15 ---
Task: retrieve air quality data
task_info: {"location": "Maine North, County Cork, Ireland", "pollutant": "SO2", "duration": "last 24 hours"}

--- Task 16 ---
Task: find location conditions
task_info: {"location": "Dry Tortugas, Florida", "report_type": "current conditions"}

--- Task 17 ---
Task: find airport weather
task_info: {"location": "Camarillo Airport, CA", "task": "check weather", "additional_info": "airport information"}
