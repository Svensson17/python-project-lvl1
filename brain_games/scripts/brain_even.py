#!/usr/bin/env python
from brain_games.brain_even_game import question, answer

from brain_games.welcome_user import welcome


def main():
    name = welcome()
    que = question()
    ans = answer()
    right_answer = "yes" if que % 2 == 0 else "no"
    score = 0
    while score < 3:
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print("\'yes\' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + "!")
            return
    print("Congratulations," + name + "!")


if __name__ == "__main__":
    main()
