import random


RULE = "What is the result of the expression?"


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    symbol = random.randint(1, 3)
    if symbol == 1:
        question = num1 + " + " + num2
        right_answer = num1 + num2
    elif symbol == 2:
        question = num1 + " - " + num2
        right_answer = num1 - num2
    elif symbol == 3:
        question = num1 + " * " + num2
        right_answer = num1 * num2
    return question, right_answer
