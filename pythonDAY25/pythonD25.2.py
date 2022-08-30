import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)
temp = data["temperature"].to_list()
print(temp)
# GET AVERAGE OF TEMPERATURE COLUMN
avg = data["temperature"].mean()
print(avg)
# GET DATA IN COLUMN
print(data["condition"])
# GET DATA IN ROW
print(data[data["temperature"].max() == data.temperature])
monday = data[data.day == "Monday"]
print((9 * monday.temperature + 160) / 5)
# HOW TO CREATE DATA DICTIONARY
data_dictionary = {
    'Student': ['Amy', 'Raj', 'Angela'],
    'Marks': [90, 75, 50]
}
data_dict = pandas.DataFrame(data_dictionary)
print(data_dict)
data_dict.to_csv("new_data.csv")


