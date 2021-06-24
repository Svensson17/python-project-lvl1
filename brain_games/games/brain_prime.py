import random


RULE = "Answer \"yes\" if the number is prime. Otherwise answer \"no\"."


def get_question_and_answer():
    num = random.randint(0, 100)
    if num < 2:
        return False
    divider = 2
    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1
    right_answer = "yes" if True else "no"
    question = num
    return question, right_answer
