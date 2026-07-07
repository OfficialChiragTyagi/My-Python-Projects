def guass_game():

    import random


    while True:
        number_range = range(1,101)

        computer_choose = random.choice(number_range) 

        user_command = input("\nCan you play? (y/n) ").strip().lower()

        if(user_command == "n"):
            print("See you soon......")
            break


        elif(user_command == "y"):

            tries = 0
            print("\n----Lets PLAY----")

            while True: 
                try:
                    tries += 1

                    player_gauss = int(input("\n Guess a NO: between 1 to 100:- "))

                    if(player_gauss == computer_choose):
                        print(f"\nOh!! You Gauss The Number in {tries} tries...")
                        break

                    elif(player_gauss < computer_choose):
                        print("\nGo Higher")    

                    else:
                        print("\nGo Lower")

                except Exception:
                    tries -= 1
                    print("Numbers only Please!!")

        else:
            print("Enter Valid Command")        

guass_game()