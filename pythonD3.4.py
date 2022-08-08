print("Welcome to python pizza deliveries")
size = input("What the size of pizza do u want? S,M or L :")
pep = input("Do u want pepproni? Y or N :")
cheese = input("Do u want extra pizza? Y or N :")
if(size=='S'):
    bill=15
elif(size=='M'):
    bill=20
elif(size=='L'):
    bill=25
if(pep=='Y'):
    if(size=='S'):
        bill+=2
    else:
        bill+=3
if(cheese=='Y'):
    bill+=1
print(f"Ur bill is :${bill}")