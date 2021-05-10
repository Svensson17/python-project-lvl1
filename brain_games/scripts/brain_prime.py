#!/usr/bin/env python
from brain_games.brain_prime_game import is_prime

from brain_games.brain_even_game import question, answer

from brain_games.welcome_user import welcome


def main():
    name = welcome()
    print("Answer \"yes\" if the number is prime. Otherwise answer \"no\".")
    score = 0
    while score < 3:
        que = question()
        ans = answer()
        prime = is_prime(que)
        right_answer = "yes" if prime else "no"
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