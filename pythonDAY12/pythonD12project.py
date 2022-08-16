import random
print("WELCOME TO NUMBER GUESSING GAME")
logo = '''

   _____ _    _ ______  _____ _____    _____          __  __ ______ 
  / ____| |  | |  ____|/ ____/ ____|  / ____|   /\   |  \/  |  ____|
 | |  __| |  | | |__  | (___| (___   | |  __   /  \  | \  / | |__   
 | | |_ | |  | |  __|  \___ \\___ \  | | |_ | / /\ \ | |\/| |  __|  
 | |__| | |__| | |____ ____) |___) | | |__| |/ ____ \| |  | | |____ 
  \_____|\____/|______|_____/_____/   \_____/_/    \_\_|  |_|______|
                                                                    
                                                                    

'''

print(logo)
print("THINK OF A NUMBER BETWEEN 1 TO 100.")
gen_num = random.randint(1,101)
diff = input("CHOOSE A DIFFICULTY 'EASY' OR 'HARD' :").lower()
if(diff=="hard"):
    attempts = 5
else:
    attempts = 10
print(f"YOU HAVE {attempts} ATTEMPTS.")
is_game_over = False
while(attempts>0 and not is_game_over):
    num = int(input("Guess a number :"))
    if(num<gen_num):
        print("Too low.")
        print("Guess again.")
    elif(num>gen_num):
        print("Too high.")
        print("Guess again.")
    else:
        print(f"You got it🤩! the answer is {num}")
        is_game_over = True
    attempts-=1
if(not is_game_over):
    print("You have used all your attempts.")

