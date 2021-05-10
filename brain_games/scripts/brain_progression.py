#!/usr/bin/env python
from brain_games.brain_even_game import answer

from brain_games.welcome_user import welcome

from brain_games.brain_progression_game import question


def main():
    name = welcome()
    print("What number is missing in the progression?")
    score = 0
    while score < 3:
        right_answer = question()
        ans = answer()
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was {1}".format(
                ans,
                right_answer))
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
