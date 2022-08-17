#spot the problem in the given code
# num = int(input("ENTER THE NUMBER :"))
# if(num%2 = 0):
#     print("THE NUMBER IS EVEN.")
# else:
#     print("THE NUMBER IS ODD.")

#corrected
num = int(input("ENTER THE NUMBER :"))
if(num%2 == 0):# instead of == we had '=' assignment operator.
    print("THE NUMBER IS EVEN.")
else:
    print("THE NUMBER IS ODD.")
