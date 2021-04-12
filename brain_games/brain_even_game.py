import random


def question():
    num = random.randint(0,100)
    print("Question: ", num)
    return num


    import prompt


def answer():
    answer = prompt.string("Your answer: ")
    return answer
