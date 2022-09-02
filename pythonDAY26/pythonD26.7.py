# Looping through dictionary
dict_items = {
    "Student" : ["Angela", "Mathew", "Agrahari"],
    "Score" : [56, 76, 86]
}
for (key, value) in dict_items.items():
    print(key)

# Looping through dataFrame
import pandas
dict_items_dataFrame = pandas.DataFrame(dict_items)
print(dict_items_dataFrame)
for (key, value) in dict_items_dataFrame.items():
    print(value)
for (index, row) in dict_items_dataFrame.iterrows():
    if row.Student == "Angela":
        print(row)

