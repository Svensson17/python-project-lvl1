import random

import math


RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    num = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = str(num) + " " + str(num2)
    right_answer = str(math.gcd(num, num2))
    return question, right_answer
