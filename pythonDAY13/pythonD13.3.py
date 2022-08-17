#spot the problem in the given code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

#corrected code

for number in range(1, 101): #indendation error correction
    if number % 3 == 0 and number % 5 == 0: # used 'or' instead of 'and'
        print("FizzBuzz")
    elif number % 3 == 0: #instead of only if we should use 'elif'
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print([number])
