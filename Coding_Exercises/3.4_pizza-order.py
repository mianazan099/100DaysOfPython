# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
final_bill = 0
size = size.lower()
add_pepperoni = add_pepperoni.lower()
extra_cheese = extra_cheese.lower()
if size == 's':
    final_bill += 15
elif size == 'm':
    final_bill += 20
elif size == 'l':
    final_bill += 25

if add_pepperoni == 'y':
    if size == 's':
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese == 'y':
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")
