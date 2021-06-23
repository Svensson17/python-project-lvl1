import random


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    question = random.randint(0, 100)
    right_answer = "yes" if num % 2 == 0 else "no"
    return question, right_answer
