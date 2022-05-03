########## 10 Debugging Steps ##########
# 1. Describe The Problem
# 2. Reproduce The Bug
# 3. Play Computer
# 4. Fix The Errors
# 5. Print is Your Friend
# 6. Use a Debugger
# 7. Take a Break
# 8. Ask a Friend
# 9. Run Code Often
# 10. Ask StackOverflow

########## Debugging Odd or Even Start ##########
##### Starting Code #####

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

##### Fixed Code #####

# number = int(input("Which number do you want to check?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

########## Debugging Odd or Even End ##########

########## Debugging Leap Year Start ##########
##### Starting Code #####

# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

##### Fixed Code #####

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

########## Debugging Leap Year End ##########

########## Debugging FizzBuzz Start ##########
##### Starting Code #####

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

##### Fixed Code #####

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

########## Debugging FizzBuzz End ##########
