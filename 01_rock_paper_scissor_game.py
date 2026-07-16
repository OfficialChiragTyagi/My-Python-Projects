import random

# The Machine Function of the Game
def game():
    while True:
        user_command = input("Do you want to play game (y/n): ")
        if(user_command == "n" or user_command == "N"):
            print("Nice to meet you!!")
            break
        elif(user_command == "y" or user_command == "Y"):
            user_choice = input("Enter rock paper or scissor: ").lower()

            choices = ["rock", "paper", "scissor"]

            computer_choice = (random.choice(choices))

           

            if(user_choice == "rock" and computer_choice == "paper"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\tHaa Haa I win!!")

            elif(user_choice == "paper" and computer_choice == "scissor"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\tHaa Haa I win!!")

            elif(user_choice == "scissor" and computer_choice == "rock"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\tHaa Haa I win!!")

            elif(user_choice == "paper" and computer_choice == "rock"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\toh No!! You win!!")

            elif(user_choice == "scissor" and computer_choice == "paper"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\toh No!! You win!!")

            elif(user_choice == "rock" and computer_choice == "scissor"):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\toh No!! You win!!")    
            
            elif(user_choice == computer_choice):
                print(f"You choose {user_choice} and I choose {computer_choice}\n\tDraw!!")

            else:
                print("Re Enter Your Choice.....")    

        else:
            print("Invalid Command!! Re Enter Command.................")           

#To Call The Function
game()            