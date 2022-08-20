from pythonD16projectMenu import Menu, MenuItem
from pythonD16projectCoffee_Maker import CoffeeMaker
from pythonD16projectMoney_Machine import MoneyMachine
logo = '''

   _____ ____  ______ ______ ______ ______   __  __          _____ _    _ _____ _   _ ______ 
  / ____/ __ \|  ____|  ____|  ____|  ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
 | |   | |  | | |__  | |__  | |__  | |__    | \  / |  /  \ | |    | |__| | | | |  \| | |__   
 | |   | |  | |  __| |  __| |  __| |  __|   | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
 | |___| |__| | |    | |    | |____| |____  | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
  \_____\____/|_|    |_|    |______|______| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|
                                                                                             
                                                                                             
'''
print(logo)
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What do want? ({options})").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

