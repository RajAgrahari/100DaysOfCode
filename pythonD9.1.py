print("WELCOME TO GRADING SYSTEM")
stu_scores = {
    "harry" : 81,
    "ron" : 78,
    "hermione" : 99,
    "draco" : 74,
    "neville" : 62,
}
stu_grades = {}
for it in stu_scores:
    var = stu_scores[it]
    if(var>90):
        stu_grades[it] = "Outstanding"
    elif(var>80):
        stu_grades[it] = "Exceeds Expectation"
    elif(var>70):
        stu_grades[it] = "Acceptable"
    elif(var<=70):
        stu_grades[it] = "Fail"
print(stu_grades)