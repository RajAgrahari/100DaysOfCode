from pythonD17projectQuestions_data import question_data
from pythonD17projectQuestion_model import Question
from pythonD17projectQuiz_brain import QuizBrain
question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your overall score is {quiz.score}/{quiz.question_no}")
