from brain_games.welcome_user import welcome


from brain_games.games.answer import answer


def base(question):
    name = welcome()
    score = 0
    while score < 3:
        num, right_answer = question()
        ans = answer()
        if ans == right_answer:
            print("Correct!")
            score = score + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                ans,
                right_answer))
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations, " + name + "!")
