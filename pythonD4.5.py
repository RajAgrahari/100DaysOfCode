#put the treasure at user specified position
print("PUTTING THE TREAURE")
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
x = input("ENTER THE POSITION WHERE U WANT TO PUT THE TREASURE :")
col = int(x[0])
row = int(x[1])
matrix[row-1][col-1] = "X"
print(f"{row1}\n{row2}\n{row3}")