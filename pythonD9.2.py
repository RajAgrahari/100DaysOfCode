#Nesting of lists and dictionaries in dictionaries
travel_log = {
    "France" : {
        "cities_visited" : ["paris","lille","dijon"],
        "total_cities" : 12,
    },
    "Germany" : {
        "cities_visited" : ["Berlin","hamburg","stuttgart"],
        "total_cities" : 5,
    }    
}
travel_log = [
    {
        "country" : "France",
        "cities_visited" : ["paris","lille","dijon"],
        "total_cities" : 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin","hamburg","stuttgart"],
        "total_cities" : 5
    }
]
print(len(travel_log))