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
        right_answer = str(math.gcd(*question()))
        ans = answer()
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print("{0} is wrong answer ;(. Correct answer was {1}".format(
                ans,
                right_answer))
            print("Let's try again, {0}!".format(
                name))
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
