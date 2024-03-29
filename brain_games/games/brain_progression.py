import random


RULE = "What number is missing in the progression?"


def get_question_and_answer():
    result = []
    score = random.randint(1, 15)
    score2 = random.randint(1, 5)
    score1 = score + (score2 * 9)
    for num in range(score, score1, score2):
        result.append(str(num))
    right_answer = random.choice(result)
    for index, value in enumerate(result):
        if right_answer == value:
            result[index] = ".."
    question = " ".join(result)
    return question, right_answer
