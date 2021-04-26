#!/usr/bin/env python
from brain_games.brain_gcd_game import question

from brain_games.brain_even_game import answer

from brain_games.welcome_user import welcome

import math


def main():
    name = welcome()
    print("Find the greatest common divisor of given numbers.")
    score = 0
    while score < 3:
        que = question()
        ans = answer()
        right_answer = math.gcd(question())
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print(ans + "is wrong answer ;(. Correct answer was" + right_answer + "\nLet's try again, " + name + "!")
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
