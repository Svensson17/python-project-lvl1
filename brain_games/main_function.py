from brain_games.welcome_user import welcome


from brain_games.games.answer import answer


def base(game):
    name = welcome()
    print(game.RULE)
    score = 0
    while score < 3:
        question, right_answer = game.get_question_and_answer()
        print("Question: ", question)
        ans = answer()
        if right_answer == ans:
            print("Correct!")
            score = score + 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                ans,
                right_answer))
            print("Let's try again, {0}!".format(name))
            return
    print("Congratulations, " + name + "!")
