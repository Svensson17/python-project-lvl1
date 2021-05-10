#!/usr/bin/env python
from brain_games.brain_even_game import question, answer

from brain_games.welcome_user import welcome


def main():
    name = welcome()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    score = 0
    while score < 3:
        que = question()
        ans = answer()
        right_answer = "yes" if que % 2 == 0 else "no"
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print(f"{ans} is wrong answer ;(. Correct answer was {right_answer}")
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
