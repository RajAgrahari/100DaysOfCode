#life left in days and weeks and months if we are going to live till 90
age = input("Enter your age:")
# print(age)
left_yrs = 90-int(age)
left_months = left_yrs*12
left_weeks = left_yrs*52
left_days = left_yrs*365
print(f" Number of weeks left:{left_weeks}\n Number of months left:{left_months}\n Number of days left:{left_days}")
