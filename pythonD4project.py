import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
outcomes = [rock,paper,scissors]
user = int(input("ENTER YoUR CHOICE: 0 FOR ROCK, 1 FOR PAPER OR 2 FOR SCISSORS :"))
if(user==0):
    print(rock)
elif(user==1):
    print(paper)
else:
    print(scissors)
computer = random.randint(0,2)
print(f"COMPUTER'S CHOICE :{computer}")
print(outcomes[computer])
if(computer==user):
    print("IT'S A DRAW")
elif(computer==0):
    if(user==1):
        print("USER WON!")
    else:
        print("COMPUTER WON!")
elif(computer==1):
    if(user==2):
        print("USER WON!")
    else:
        print("COMPUTER WON!")
else:
    if(user==0):
        print("USER WON!")
    else:
        print("COMPUTER WON!")



