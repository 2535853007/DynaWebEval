I want to build a comprehensive investment and market insights platform where people can research stocks, track their financial interests, and discover new opportunities. Users should be able to look up current and historical stock prices, read the latest company news, and review detailed financial records like balance sheets and cash flows. 

The platform needs to help users find specific investments. They should be able to screen for companies based on their sector or size, discover high-yield dividend stocks, and explore upcoming IPOs. It also needs to cover the broader financial picture, allowing people to monitor global indices, currency exchange rates, and commodity prices like gold.

Personalization is highly important for the user journey. Users need to be able to build categorized watchlists, bookmark important corporate events like upcoming earnings dates, and set up real-time alerts for when a stock hits a specific price or volume. Additionally, I want them to have access to helpful tools, like an investment calculator to project how their money will grow over time with compound interest and regular contributions. Finally, they should be able to manage their personal trade offers and view visual charts to easily compare market performance, moving averages, and complex market trends.

The app you build must support the following tasks:
--- Task 1 ---
Task: compute investment growth
task_info: {"principal": 10000, "monthly_contribution": 200, "duration_years": 10, "interest_rate": 5.0, "compounding_frequency": "quarterly", "plot_colors": "identify"}

--- Task 2 ---
Task: find stock events
task_info: {"entity": "stock"}

--- Task 3 ---
Task: retrieve stock price
task_info: {"time_range": "past month"}

--- Task 4 ---
Task: access market chart
task_info: {"time_range": "1-year", "market": "European"}

--- Task 5 ---
Task: find stock price
task_info: {"stock_price_time": "closing", "date": "March 17, 2026"}

--- Task 6 ---
Task: find dividend stocks
task_info: {"type": "high-yield", "action": "share list"}

--- Task 7 ---
Task: check performance chart
task_info: {"time_range": "5-year", "index": "S&P 500"}

--- Task 8 ---
Task: generate chart
task_info: {"chart_type": "moving average", "index": "Dow 30"}

--- Task 9 ---
Task: access calendar
task_info: {"type": "IPO", "focus": "upcoming offerings", "time_period": "August", "action": "add to alerts", "location": "personal dashboard"}

--- Task 10 ---
Task: add stock
task_info: {"list_type": "watch list"}

--- Task 11 ---
Task: show equity screener
task_info: {"market_segment": "Mid Cap", "industry": "Healthcare"}

--- Task 12 ---
Task: find price
task_info: {"commodity": "gold", "action": "monitor"}

--- Task 13 ---
Task: create alert
task_info: {"symbol": "BUD"}

--- Task 14 ---
Task: display financial statements
task_info: {"statements": ["balance sheet", "cash flow"], "fiscal_year": 2026}

--- Task 15 ---
Task: review trades
task_info: {"filter": "active trade offers", "tasks": ["evaluate current status", "archive expired or completed offers"], "scope": "portfolio"}

--- Task 16 ---
Task: browse stock news
task_info: {"entity": "Microsoft", "news_scope": "top news"}

--- Task 17 ---
Task: show historical data
task_info: {"asset": "EUR/USD"}

--- Task 18 ---
Task: retrieve company code
task_info: {"criterion": "top mover", "sector": "Technology", "index": "Sector Index", "date_reference": "latest market close"}

--- Task 19 ---
Task: analyze and compare data
task_info: {"metric": "U.S. ETP Odd Lot Rate (%)", "comparison_groups": ["Quartile 1", "Quartile 4"], "group_organization": "by price", "visualization": {"chart_type": "logarithmic scale"}}
