def f092_travelLog():
    travel_log = [{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
    ]
    new_country = addNewCountry(country_name='Russia', visite_times=3, cities=['Moscow', 'Sait-petersburg'])
    travel_log.append(new_country)

    for item in travel_log:
        print(f"You've visited {item['country']} {item['visits']}")
        print(f"You've been to {item['cities'][0]} and {item['cities'][1]}")

def addNewCountry(country_name, visite_times, cities):
    new_travel = {
            "country": country_name,
            "visits" : visite_times,
            "cities": cities
            }
    return new_travel

f092_travelLog()
