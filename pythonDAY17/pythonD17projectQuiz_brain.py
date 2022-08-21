
class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        curr_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no}: {curr_question.text}:")
        self.check_ans(ans, curr_question.answer)


    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_ans(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print("You got it! correct")
        else:
            print("You got it wrong!")
        print(f"Correct answer is {correct_ans}")
        print(f"Your score is {self.score}/{self.question_no}\n")
