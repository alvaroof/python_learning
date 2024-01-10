# -*- coding: utf-8 -*-
from api_client import ApiClient
from question import Question


class QuizManager:
    self.score = 0
    self.api_client = ApiClient()

    def start_quiz(self):
        question_list = self.api_client.fetch_questions()
        for idx, q in enumerate(question_list):
            question = Question(q)
            print(f"\nQuestion number {idx+1}: ")
            print(question.question)
            answer = []
            while answer not in ["True", "False"]:
                answer = input("Provide a True/False answer: ")
            is_correct = question.check_answer(answer)
            if is_correct:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        print(f"\n\nFinal Score is: {self.score}/{len(question_list)} correct questions.")
