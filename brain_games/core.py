import prompt


from brain_games.welcome_user import welcome


def base(game):
    name = welcome()
    print(game.RULE)
    score = 0
    end_score = 3
    while score < end_score:
        question, right_answer = game.get_question_and_answer()
        print("Question:", question)
        answer = prompt.string("Your answer: ")
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
