print("Welcome to Treasure Island")
print("Ur mission is to find the treasure")
direct = input("Where u have to go? left or right :")
if(direct=="right"):
    print("GAME OVER")
else:
    direct2 = input("Do u want to wait or swim :")
    if(direct2=="swim"):
        print("Game Over")
    else:
        direct3 = input("Which door u want to open? blue,red or yellow :")
        if(direct3=="yellow"):
            print("Hurrah! U won")
        else:
            print("GAME OVER")
        