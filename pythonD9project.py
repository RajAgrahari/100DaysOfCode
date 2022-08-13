print("Welcome to Blind auction")
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bid = {}
sold = False
bidder = ""
while not sold:
    name = input("What is your name? :")
    price = input("What is the bid amount? :$")
    bid[name] = price
    bidder=name
    anyone = input("Are there any other biders? Type 'YES' OR 'NO' :")
    if(anyone=="NO"):
        sold = True
print(f"The winner is {bidder} with bid amount :{bid[bidder]}")