print("hightest score calculator")
stu_scores = input("Enter the scores of students :").split(" ")
m = 0
for i in range(0,len(stu_scores)):
    stu_scores[i] = int(stu_scores[i])
for x in stu_scores:
    if(m<x):
        m=x
print(f"Maximum number is :{m}")


