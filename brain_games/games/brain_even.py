import random


print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def question():
    num = random.randint(0, 100)
    print("Question:", num)
    return num


def r_answer():
    que = question()
    right_answer = "yes" if que % 2 == 0 else "no"
    return right_answer
