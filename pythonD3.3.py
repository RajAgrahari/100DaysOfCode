print("WELCOME TO BMI 2.0 CALCULATOR")
height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))
bmi = (weight/height**2)
if(bmi<18.5):
    print(f"ur bmi is {bmi} ,U r underweighted")
elif(bmi<25):
    print(f"ur bmi is {bmi} ,U r normalweighted")
elif(bmi<30):
    print(f"ur bmi is {bmi} ,U r overweighted")
elif(bmi<35):
    print(f"ur bmi is {bmi} ,U r obese")
elif(bmi>35):
    print(f"ur bmi is {bmi} ,U r clinically obese")