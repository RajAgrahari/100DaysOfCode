print("Welcome to raj's rollercoaster")
height = int(input("Enter your height in cms:"))
if(height>=120):
    print("Go to ticket counter")
    age = int(input("Enter your age:"))
    if(age<12):
        bill=5
    elif(age<=18):
        bill=7
    else:
        bill=9
    wants_photo = input("Do u want photo also:")
    if(wants_photo=='Y'):
        bill+=3
    print(f"Ur bill is ${bill}")
    
else:
    print("U r not allowed")