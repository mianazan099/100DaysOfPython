# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
full_name = name1 + name2
t = int(full_name.count('t'))
r = int(full_name.count('r'))
u = int(full_name.count('u'))
e = int(full_name.count('e'))
l = int(full_name.count('l'))
o = int(full_name.count('o'))
v = int(full_name.count('v'))
e = int(full_name.count('e'))
true = str(t+r+u+e)
love = str(l+o+v+e)
true_love = int(true+love)
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love < 50 and true_love > 40:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
