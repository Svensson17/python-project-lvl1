import random

import prompt


def question():
    num = random.randint(0,100)
    print("Question: ", num)
    return num

def answer():
    answer = prompt.string("Your answer: ")
    return answer
