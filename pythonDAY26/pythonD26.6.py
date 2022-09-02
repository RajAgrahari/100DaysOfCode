weather_c = {
    'Monday': 12,
    'Tuesday': 20,
    'Wednesday': 23,
    'Thursday': 15,
    'Friday': 10,
    'Saturday': 22,
    'Sunday': 21
}
weather_f = {key: ((9/5)*value+32) for (key, value) in weather_c.items()}
print(weather_f)
