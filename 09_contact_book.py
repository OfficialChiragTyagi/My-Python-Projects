def contact_app():
    contact_book = {}
    while True:
        user_choice = input("\nEnter 1 to add new contact No. \nEnter 2 to show contact Details \nEnter 3 to find contact No. \nEnter 4  to exit\n\n ")
        if(user_choice == "1"):
            user_name = input("Enter user name: ")
            try:
                user_contact = int(input("Enter user Phone No.  "))
                contact_book.update({user_name:user_contact})
            except ValueError:
                print("invalid mobile no.")

        elif(user_choice == "2"):
            for name ,mobile in contact_book.items():
                print(f"{name} : {mobile}")

        elif(user_choice == "3"):
            user_name = input("Enter user name: ")
            contect = contact_book.get(user_name)
            if contect:
               print(contact_book.get(user_name))
            else:
                print("Contect not found")   

        elif(user_choice == "4"):
            print("See you soon")
            break
        
        else:
            print("invalid!!")    

contact_app()