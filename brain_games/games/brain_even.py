import random


print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def question():
    num = random.randint(0, 100)
    print("Question:", num)
    global right_answer
    right_answer = "yes" if num % 2 == 0 else "no"
    return num
