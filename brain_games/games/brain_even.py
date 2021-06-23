import random


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    num = random.randint(0, 100)
    print("Question:", num)
    right_answer = "yes" if num % 2 == 0 else "no"
    return right_answer
