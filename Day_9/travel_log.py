# TODO: Write the function that will allow new countries to be added to the travel_log.

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def  add_new_country(country_p, visits_p, cities_p):
    new_country = {}
    new_country["country"] = country_p
    new_country["visits"] = visits_p
    new_country["cities"] = cities_p

    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)