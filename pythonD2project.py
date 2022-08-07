print("Welcome to the tip calculator")
tot_bill = float(input("What was the total bill? $"))
tot_person = float(input("How many people to spilt the bill? "))
tip_persent = float(input("What percentage of bill u want to give as a tip? 10, 12 or 15:"))
tip = ((tot_bill)*(tip_persent))/100
bill_per_person = (tot_bill + tip)/tot_person
# print("Amount to be paid by per person: $"+str(round(bill_per_person,2)))
print(f"Amount to be paid by per person: ${round(bill_per_person,2)}")