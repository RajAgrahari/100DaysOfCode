#HANGEMAN PROJECT
import random
import pythonD7projectPart1
# import pythonD7projectPart2
from pythonD7projectPart2 import word_list 
from pythonD7projectPart1 import logo
print("WELCOME TO HANGMAN GAME")
print(logo)
choosen_word = random.choice(word_list)
l = len(choosen_word)
str=[]
end_of_game=False
for i in range(0,l):
    str.append("_")
lives=6
while not end_of_game:
    guess = input("Guess a Letter :").lower()
    for i in range(0,l):
        if(choosen_word[i]==guess):
            str[i]=guess   
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game=True
            print("YOU ARE HANGED😵")
    print(f"{' '.join(str)}")
    if '_' not in str:
        end_of_game=True
        print("YOU WON!")
    print(pythonD7projectPart1.stages[lives])




    


