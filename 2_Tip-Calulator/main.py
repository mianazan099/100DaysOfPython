print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))  # 20
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))  # 50
people = int(input("How many people to split the bill? "))  # 2
bill_per_person = round(((bill / 100) * tip + bill) / people, 2)
print(f"Each person should pay: ${bill_per_person}")  # 15.0
