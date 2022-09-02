with open("file1.txt") as file1:
    num1 = file1.readlines()
    new_num1 = [int(n.strip()) for n in num1]

with open("file2.txt") as file2:
    num2 = file2.readlines()
    new_num2 = [int(n.strip()) for n in num2]

new_num = [n for n in new_num1 if n in new_num2]
print(new_num)
