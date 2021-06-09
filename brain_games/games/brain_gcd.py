import random

import math


print("Find the greatest common divisor of given numbers.")


def question():
    num = random.randint(0, 100)
    num2 = random.randint(0, 100)
    print("Question:", num, num2)
    right_answer = str(math.gcd(*question()))
    global right_answer
    return num, num2
