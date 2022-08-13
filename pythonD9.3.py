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
def add_new_country(country,num_visited,cities):
    dic = {}
    dic["country"]=country
    dic["visits"]=num_visited
    dic["cities"]=cities
    travel_log.append(dic)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
