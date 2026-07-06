import random

def quiz_game():
    while True:
        questions = {
            "What is the name of our contery?":"india",
            "What is the capital of India?":"new delhi",
            "How many colours are there in a rainbow?":"seven",
            "How many days are there in a week?":"seven",
            "What is the boiling point of water?":"100",
            "Which animal is known as the King of the Jungle?":"lion",
            "2+2":"4",
            "6+10-8":"8"
        }

        random_question = random.choice(list(questions.keys()))

        user_answer = input(f"{random_question}: ").strip().lower()

        if(questions[random_question] == user_answer):
            print("Right Answer!!")

        else:
            print("Wrong Answer!!")    

quiz_game()
