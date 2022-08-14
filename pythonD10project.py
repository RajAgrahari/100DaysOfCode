print("WELCOME TO CALCULATOR")
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def addition(n1,n2):
    return (n1+n2)
def subtraction(n1,n2):
    return (n1-n2)
def multiply(n1,n2):
    return (n1*n2)
def division(n1,n2):
    return (n1/n2)
operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiply,
    "/" : division,
}
def calculator():
    print(logo)
    f = True
    num1 = float(input("ENTER THE FIRST NUMBER :"))
    while f:
        for symbols in operations:
            print(symbols)
        op = input("Pick an operation from above :")
        num2 = float(input("ENTER THE NEXT NUMBER :"))
        calculation_fn = operations[op]
        ans = calculation_fn(num1,num2)
        print(f"{num1} {op} {num2} = {ans}")
        cont = input(f"DO U WANT TO CONTINUE WITH {ans} OR NOT IF YES THEN 'y' or 'n' :")
        if(cont == "n"):
            f = False
            calculator()
        else:
            num1 = ans
calculator()