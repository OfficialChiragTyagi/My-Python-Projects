import random
import string
while True:

    x = input("Need a Password? (y/n) ").strip().lower()

    if(x == "n"):
        print("see you soon...")
        break

    elif(x == "y"):

        def random_pasword(lenght):
            char = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choices(char, k=lenght))

            return password

        try:
            lenght = int(input("Enter pasword lenght: "))
            if(lenght < 4):
                print("pasword lenght must be 4 or more")


            else:
                print(f"Generated Password: {random_pasword(lenght)}")    

        except ValueError:
            print("Invalid pasword length") 

    else:
        print("\n\tInvalid!!")       


# .....................................................................................................................................................................................................................................................................................................
