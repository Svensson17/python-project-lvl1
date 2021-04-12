import prompt


def welcome():
        print("Welcome to the Brain Games!")
        name = prompt.string("May I have your name?")
        print("Hello, " + name + "!")
        print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    
