print("WELCOME TO AVERAGE FINDER")
stu_heights = input("Enter the heights of the students :").split(" ")
for i in range(0,len(stu_heights)):
    stu_heights[i] = int(stu_heights[i])
h=0
for i in stu_heights:
    h+=i
print(f"AVERAGE OF STUDENTS HEIGHTS : {h/len(stu_heights)}")