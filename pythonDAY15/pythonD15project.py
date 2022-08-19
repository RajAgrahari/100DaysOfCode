from pythonD15projectData import menu
from pythonD15projectData import resources
logo = '''

   _____ ____  ______ ______ ______ ______   __  __          _____ _    _ _____ _   _ ______ 
  / ____/ __ \|  ____|  ____|  ____|  ____| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
 | |   | |  | | |__  | |__  | |__  | |__    | \  / |  /  \ | |    | |__| | | | |  \| | |__   
 | |   | |  | |  __| |  __| |  __| |  __|   | |\/| | / /\ \| |    |  __  | | | | . ` |  __|  
 | |___| |__| | |    | |    | |____| |____  | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____ 
  \_____\____/|_|    |_|    |______|______| |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|
                                                                                             
                                                                                             
'''
print(logo)
while True :
    choice = input("WHAT DO YOU WANT? (ESPRESSO,LATTE,CAPPUCCINO or REPORT) :").lower()
    collection = 0
    if(choice == "report"): 
        print(f'Water : {resources["water"]}ml')
        print(f'Milk : {resources["milk"]}ml')
        print(f'Coffee : {resources["coffee"]}g')
        print(f"Total collection :Rs{collection}.")
    else:
        print("Please insert money.")
        ten_coin = int(input("how many 10-rupee coin? :"))
        five_coin = int(input("how many 5-rupee coin? :"))
        two_coin = int(input("how many 2-rupee coin? :"))
        one_coin = int(input("how many 1-rupee coin? :"))
        sum = 5*five_coin + 10*ten_coin + 2*two_coin + one_coin
        resources_ind_w = resources["water"]
        resources_ind_m = resources["milk"]
        resources_ind_c = resources["coffee"]
        if(choice == "espresso"):
            menu_cost = menu["espresso"]["cost"]
            menu_ind_w = menu["espresso"]["ingredients"]["water"]
            menu_ind_c = menu["espresso"]["ingredients"]["coffee"]
            if(menu_ind_w <= resources_ind_w and menu_ind_c <= resources_ind_c):
                if(sum >= menu_cost):
                    print("Enjoy your espresso☕.")
                    print(f"Take your change :Rs{sum-menu_cost}.")
                else:
                    print("Sorry, that's not enough money.Money refunded.")
            else:
                print(f"Not enough resources available to make {choice}.")    
        elif(choice == "latte"):
            menu_cost = menu["latte"]["cost"]
            menu_ind_w = menu["latte"]["ingredients"]["water"]
            menu_ind_m = menu["latte"]["ingredients"]["milk"]
            menu_ind_c = menu["latte"]["ingredients"]["coffee"]
            if(menu_ind_w <= resources_ind_w and menu_ind_m <= resources_ind_m and menu_ind_c <= resources_ind_c):
                if(sum >= menu_cost):
                    print("Enjoy your latte☕.")
                    print(f"Take your change :Rs{sum-menu_cost}.")
                else:
                    print("Sorry, that's not enough money.Money refunded.")
            else:
                print(f"Not enough resources available to make {choice}.")
        elif(choice == "cappuccino"):
            menu_cost = menu["cappuccino"]["cost"]
            menu_ind_w = menu["cappuccino"]["ingredients"]["water"]
            menu_ind_m = menu["cappuccino"]["ingredients"]["milk"]
            menu_ind_c = menu["cappuccino"]["ingredients"]["coffee"]
            if(menu_ind_w <= resources_ind_w and menu_ind_m <= resources_ind_m and menu_ind_c <= resources_ind_c):
                if(sum >= menu_cost):
                    print("Enjoy your cappuccino☕.")
                    print(f"Take your change :Rs{sum-menu_cost}.")
                else:
                    print("Sorry, that's not enough money.Money refunded.")
            else:
                print(f"Not enough resources available to make {choice}.")
