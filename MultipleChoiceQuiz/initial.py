from QuestionClass import Question
question_prompts = [
                    "what colour are bananas? \n(a) red \n(b) yellow\n(c) green\n\n",
                    "what colour are strawberries? \n(a) red \n(b) yellow\n(c) green\n\n",
                    "what colour are kiwi's? \n(a) red \n(b) yellow\n(c) green\n\n"
]# these elements are stored within an array

questions = [
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"c")
]

def run(questions):
    score = 0
    for question in questions:
        answer = input(question.question + " >")
        if answer == question.answer:
            score += 1
    print("< You got " + str(score) + "/" + str(len(questions)) + " Correct >")

run(questions)