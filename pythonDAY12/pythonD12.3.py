#Modifying global scope
enemies = 1

def increase_enemies():
    global enemies
    enemies+=1
    return enemies
print(increase_enemies())
# OR
def increase_enemies():
    return (enemies+1)
    
print(increase_enemies())
