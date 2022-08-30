import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temperature':
            temperatures.append(row[1])
    print(temperatures)
