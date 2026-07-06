import random

while True:

    user_input = input("Press Y to start or N to exit: ").strip().lower()

    dice_range = range(1,7)
    if(user_input == "y"):
        roll = random.randint(1,6)
        print(f"Your dice is roll and {roll} is comming!!")

    elif(user_input == "n"):
        print("Nice to see you!!")
        break
    else:
        print("Enter Y or N only.......\nYou want to roll dice")    