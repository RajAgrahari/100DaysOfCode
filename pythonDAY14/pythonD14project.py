print("*WELCOME TO HIGHER LOWER GAME*")
from pythonD14projectArt import logo
from pythonD14projectArt import vs
from pythonD14projectData import data
from random import randint

def compare(first,second):
    if(first>second):
        return "A"
    else:
        return "B"


is_game_over = False
score = 0
first_per = data[randint(0,len(data)-1)]
print(first_per)
print(vs)
while not is_game_over:
    idxsec = randint(0,len(data)-1)
    second_per = data[idxsec]
    if(first_per == second_per):
        second_per = data[(idxsec+1)%len(data)]
    print(second_per)
    ans = compare(first_per["followers"],second_per["followers"])
    guess = input("Type 'A' for first person or 'B' for second person :")
    if(ans == guess):
        first_per = second_per
        score+=1
        print(first_per)
        print(vs)
    else:
        is_game_over=True
        print(f"YOUR SCORE IS {score}")


