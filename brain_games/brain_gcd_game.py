import random


def question():
    num = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print("Question:", num, num2)
    return num, num2
