import random


print("What is the result of the expression?")


def question():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    symbol = random.randint(1, 3)
    if symbol == 1:
        print("Question: ", num1, num2, sep='+')
        result = num1 + num2
    elif symbol == 2:
        print("Question: ", num1, num2, sep='-')
        result = num1 - num2
    elif symbol == 3:
        print("Question: ", num1, num2, sep='*')
        result = num1 * num2
    return result
