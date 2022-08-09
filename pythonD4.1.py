#head or tail generating machine
import random

# randomInt = random.randint(1,10)
# print(randomInt)
# randomFloat = random.random()*5
# # 0.0000...-4.999999
# print(randomFloat)
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)
rand_side = (random.randint(0,1))
if(rand_side == 1):
    print("Heads")
else:
    print("Tails")
