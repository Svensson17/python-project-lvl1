#!/usr/bin/env python
from brain_games.brain_calc_game import question

from brain_games.brain_even_game import answer

from brain_games.welcome_user import welcome


def main():
    name = welcome()
    print("What is the result of the expression?")
    score = 0
    while score < 3:
        que = int(question())
        ans = int(answer())
        if que == ans:
            print("Correct!")
            score = score + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                str(ans),
                str(que)))
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
