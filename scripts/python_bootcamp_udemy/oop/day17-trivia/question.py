# -*- coding: utf-8 -*-
class Question:
    def __init__(self, content):
        self.question = content["question"]
        self.correct_answer = content["correct_answer"]

    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()
