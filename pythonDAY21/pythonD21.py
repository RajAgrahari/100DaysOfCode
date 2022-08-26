# SLICING OF LIST

animals = ["cat", "dog", "rat", "horse", "monkey"]
#         0-----1------2------3--------4---------5
for _ in animals[2:4]:
    print(_)
print("\n")
for _ in animals[0:4]:
    print(_)
print("\n")
for _ in animals[::2]:
    print(_)
print("\n")
for _ in animals[::]:
    print(_)
