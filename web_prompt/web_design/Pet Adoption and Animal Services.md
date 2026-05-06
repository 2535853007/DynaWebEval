I need a website for pet adoption and animal services where people can easily find their perfect furry friend. Users should be able to search for pets—like cats, dogs, and rabbits—by entering their city or zip code and deciding how far they are willing to travel. They need to be able to look for specific details, such as a pet's age, breed, gender, coat color, and even personality traits like energy levels or barking habits, and easily see the newest arrivals or the pets closest to them. 

When they find an animal they love, they should be able to save it to their favorites, share the listing with friends, or reach out to schedule a visit and express their interest in adopting. If their perfect match isn't available right away, they should be able to set up free email alerts to get notified when new animals are added. 

Lastly, the platform should help people learn about pet ownership. Users need to be able to compare different breeds, learn about breed characteristics like average size and playfulness, save breeds they like to their profile, and read helpful guides on general pet care and grooming.

The app you build must support the following tasks:
--- Task 1 ---
Task: search adoption listings
task_info: {"gender": "female", "species": "cat"}

--- Task 2 ---
Task: search adoption listings
task_info: {"gender": "male", "species": "rabbit", "breed": "specific breed", "location": "New York", "action": "copy share URL link"}

--- Task 3 ---
Task: search adoption listings
task_info: {"gender": "male", "species": "cat", "location": "zip code 75209", "action": "add to favorites"}

--- Task 4 ---
Task: search adoption listings
task_info: {"age_group": "young", "species": "cat", "location": "Seattle", "action": "show newest additions"}

--- Task 5 ---
Task: create alert
task_info: {"species": "dog", "breed": "Jack Russell Terrier", "location": "zip code 10019", "notifications": "email", "email": "buckeye.foobar@gmail.com", "alert_type": "free"}

--- Task 6 ---
Task: search adoption listings
task_info: {"gender": "female", "species": "kitten", "color": "white", "location_radius": "35 miles", "location": "zip code 77494"}

--- Task 7 ---
Task: retrieve information
task_info: {"topic": "average size", "breed": "golden retriever"}

--- Task 8 ---
Task: search adoption listings
task_info: {"gender": "male", "age_group": "young", "color": "white", "species": "dog", "breed": "German Shepherd", "location_radius": "50 miles", "location": "zip code 78613"}

--- Task 9 ---
Task: retrieve information
task_info: {"topic": "playful level", "breed": "corgi"}

--- Task 10 ---
Task: locate webpage
task_info: {"topic": "Dog and Puppy Grooming"}

--- Task 11 ---
Task: search adoption listings
task_info: {"species": "rabbit", "location_radius": "100 miles", "location": "zip code 94587", "action": "add to favorites"}

--- Task 12 ---
Task: search adoption listings
task_info: {"age_group": "adult", "species": "cat", "location": "Naperville, IL"}

--- Task 13 ---
Task: search adoption listings
task_info: {"age_group": "adult", "species": "dog", "breed": "husky", "location": "zip code 10019"}

--- Task 14 ---
Task: compare breeds
task_info: {"breed_list": ["Afghan Hound", "Akita", "Azawakh"]}

--- Task 15 ---
Task: search adoption listings
task_info: {"breed": "hairless dog", "energy_level": "energetic", "barking_level": "medium"}
