#Namespace local vs global scope
enemies = 2
def count_enemies():
    enemies=3
    print(f"The number of enemies is :{enemies}")
count_enemies()
print(f"The number is enemies is :{enemies}")

def first_fn():
    def second_fn():
        print(f"The number is enemies is :{enemies}")
    second_fn()

first_fn()