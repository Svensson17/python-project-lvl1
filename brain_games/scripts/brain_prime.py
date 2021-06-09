#!/usr/bin/env python
from brain_games.games.answer import answer

from brain_games.games.brain_prime.is_prime import right_answer

from brain_games.welcome_user import welcome


def main():
    name = welcome()
    score = 0
    while score < 3:
        if right_answer == answer:
            print("Correct!")
            score = score + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer,
                right_answer))
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations, " + name + "!")


if __name__ == "__main__":
    main()
