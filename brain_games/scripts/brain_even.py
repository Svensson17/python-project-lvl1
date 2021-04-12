#!/usr/bin/env python
from brain_games.question import question

from brain_games.answer import answer

from brain_games.welcome_user import welcome


def main():
    welcome()
    question()
    answer()
    que = question()
    ans = answer()
    right_answer = "yes" if que % 2 == 0 else "no"
    while right_a:
        if right_answer == ans:
        print("Correct!")
    else:
        name = input()
        print("\'yes\' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + "!")
        print("Congratulations," + name + "!")
