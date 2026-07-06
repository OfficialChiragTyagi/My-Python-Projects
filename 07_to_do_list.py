tasks = []

while True:
    print("\n\t------Enter 1 to create task 2 to show task 3 to remove task and 4 to exit------ ")
    
    user_input = input("\nChoose: ").strip()

    if(user_input == "1"):
        create_task = input("Add task : ")
        tasks.append(create_task)
        

    elif(user_input == "2"):

        for task in tasks:
            print(task)
        

    elif(user_input == "3"):
        if(not tasks):
            print("No tasks available!!")
        else:
            try:
                for task in tasks:
                    print(task)
                remove_task = int(input("choose task no.- "))
                tasks.pop(remove_task-1)
                
            except IndexError:
                print("Put Valid Nomber")
            except ValueError:
                print("Put Nombers only")  

    elif(user_input == "4"):
        print("see you soon") 
        break 

    else:
        print("Enter 1, 2, 3, or 4 only!! ") 