print("WELCOME TO LOVE CALCULATOR")
name1 = input("Enter the first person's name:")
name2 = input("Enter the second person's name:")
lower_n1 = name1.lower()
lower_n2 = name2.lower()
name = lower_n1+lower_n2
c = name.count('t')
c+= name.count('r')
c+= name.count('u')
c+= name.count('e')
d= name.count('l')
d+= name.count('o')
d+= name.count('v')
d+= name.count('e')
print(f"love percentage : {c}{d}%")
percent = int(str(c)+str(d))
if(percent>90):
    print("U both are made for each other")
elif(percent>40 and percent<90):
    print("U both can improve ur relationalship")
else:
    print("U can go for some other girl or boy")