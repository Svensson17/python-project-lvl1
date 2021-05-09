from brain_games.brain_even_game import question

def is_prime():
    num = question()
    if num < 2:
        return False
    divider = 2
    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1
    return True
