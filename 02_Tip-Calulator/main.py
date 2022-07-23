print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = "{:.2f}".format(((total_bill / 100) * tip_percentage + total_bill) / people)
print(f"Each person should pay: ${bill_per_person}")
