def atm_sim():
    while True:
        add_account = input("Did you want to a new Bank Account? (y/n) ").strip().lower()
        if(add_account == "n"):
            print("See you next time 😉")
            break

        elif(add_account == "y"):
            account_name = input("Enter your Account Name: ")
            balance = float()
            print(f"\nYour Account name is {account_name}\nWhat do you want now....\n")

            while True:
                user_input = input("\nTo check Balance press 1  to Dabit money press 2  to cradit money press 3  to logout press 4 or exit. ").strip().lower()

                if(user_input == "1"):
                    print("\nAccount Balance: ",balance)

                elif(user_input == "2"):
                    try:
                        add_money = int(input("Enter Your Amount to Dabit:-\n"))
                        if(add_money <0):
                            print("Enter positive Amount only 😊")
                        else:
                            balance += add_money
                            print(f"\nYou Successfully dabited {add_money} rupees 😊😊")

                    except ValueError:
                        print("Invalid Amount 😑😑")

                elif(user_input == "3"):
                    try:
                        cradit_money = int(input("Enter Amount you want to cradit:-\n"))

                        if(cradit_money < 0):
                            print("Enter positive Amount to cradit 😊")

                        else:
                            if(balance < cradit_money):
                                print("\nyou have not enough money to cradit 🤔")

                            elif(balance >= cradit_money):
                                balance -= cradit_money
                                print(f"\nYou successfully cradit {cradit_money} rupees 😊😊")

                    except ValueError:
                        print("Invalid Amount 😑😑")

                elif(user_input == "4" or user_input == "exit"):
                    print("\nYou successfully logouted and Your Account was Deleted 😪\nSee You soon 😊 ")
                    break

                else:
                    print("\nEnter 1 2 3 or 4 only!! 😫")

        else:
            print("\nEnter (y/n) only!! 😫")

atm_sim()