# print squared numbers
numbers = [1, 1, 2, 3, 8, 13, 21]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)
# print even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)