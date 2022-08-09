#WHO WILL PAY
import random
test_seed = int(input("enter the seed : "))
random.seed(test_seed)
names = input("ENTER THE NAMES OF THE FRIENDS : ")
namesSplited = names.split(", ")
index = random.randint(0,len(namesSplited)-1)
print(f"{namesSplited[index]} will pay for today")

