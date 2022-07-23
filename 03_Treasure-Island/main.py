from art import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if road != "left":
    print("You fell into a hole. Game Over.")
else:
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if lake != "wait":
        print("You get attacked by an angry trout. Game Over.")
    else:
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
