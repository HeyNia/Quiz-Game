


class QuizBrain:
    def __init__(self,q_list):
        self.question_number =0
        self.question_list = q_list
        self.user_score = 0


    def still_has_question(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(current_question.text)
        self.question_number += 1
        user_ans = input(f"Q. {self.question_number }: {current_question.text} (True / False) :")
        self.check_answer(user_ans,current_question.answer)



    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.user_score += 1
            print("You got right!")
        else :
            print("You got wrong!")

        print(f"The correct answer was : {correct_ans}.")
        print(f"your current score is: {self.user_score} / {self.question_number}")
        print("\n")
