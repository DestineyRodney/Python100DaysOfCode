age = input("What is your current age?")

final_age = 90
years_left = final_age - int(age)
print(years_left)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12
print("You have " + str(days) +  " days, " + str(weeks) + " weeks, " + str(months) + " months left." )