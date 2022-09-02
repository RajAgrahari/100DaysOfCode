# dictionary comprehension
student = {
    'Raj': 60,
    'Mohan': 70,
    'Maru': 80,
    'pakya': 85,
    'Jay': 75
}
new_student = {key: value for (key, value) in student.items() if value < 80}
print(new_student)

