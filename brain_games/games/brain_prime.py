RULE = "Answer \"yes\" if the number is prime. Otherwise answer \"no\"."


def is_prime(num):
    if num < 2:
        return False
    divider = 2
    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1
    right_answer = "yes" if True else "no"
    return True, right_answer
