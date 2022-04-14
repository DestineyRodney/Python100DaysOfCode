print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_amount = int(input("What tip percentage would you like to tip? Enter a whole number "))
split_by = int(input("how many people to split the bill? "))
pay_by_each = total_bill/ split_by
pay = (pay_by_each * (tip_amount/100)) + pay_by_each
print(f"Each person should pay ${pay}")