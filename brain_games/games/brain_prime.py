import random


RULE = "Answer \"yes\" if the number is prime. Otherwise answer \"no\"."


def get_question_and_answer():
    question = random.randint(0, 100)
    right_answer = "yes" if True else "no"
    return question, right_answer


    def is_prime(question):
        if question < 2:
            return False
        divider = 2
        while divider <= question / 2:
            if question % divider == 0:
                return False
            divider += 1
        return True
