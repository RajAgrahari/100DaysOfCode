# python sequences
# list comprehension
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
name = "Raj Agrahari"
new_name = [items for items in name]
print(new_name)
_range = [i for i in range(1, 5, 1)]
new_range = [i*2 for i in range(1, 5, 1)]
print(_range)
print(new_range)
names = ["raj", "mukulrana", "ayushraj", "raviranjan", "amankumarverma"]
new_names = [n.upper() for n in names if len(n) > 5]
print(new_names)


