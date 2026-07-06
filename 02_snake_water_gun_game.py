import random
def play_game():
    
    while True:
        user_command = input("Do you want to play? (y/n) ").strip().lower()
        if(user_command == "n"):
            print("See you soon......")
            break

        elif(user_command == "y"):
            print("\n----Lets PLAY----")
            user_choice = input("Enter snake water or gun:- ").strip().lower()
            choices = ["snake", "water", "gun"]
            conditions = {"snake":"water", "water":"gun", "gun":"snake"}

            computer_choice = random.choice(choices)

            print(f'''You choose {user_choice}\nComputer choose {computer_choice}''')

            if(user_choice not in conditions):
                print("Invalid Choice.....")
            elif (user_choice == computer_choice):
                print("\nIt's a Tie!!")

            elif(conditions[user_choice] == computer_choice):
                print("\nYou Win!!")

            else:
                print("\nComputer Win!!")

        else:
            print("Enter y or n only...")

play_game()