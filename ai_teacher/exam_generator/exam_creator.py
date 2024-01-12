# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI


class ExamCreator:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    def generate_questions(self, content):
        """Generates multiple-choice questions based on the provided content."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant designed to output a multiple choice exam as a JSON.",
                    },
                    {"role": "user", "content": self._create_prompt(content)},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in generating questions: {e}")
            return None

    @staticmethod
    def _create_prompt(content):
        """Creates a prompt for the OpenAI API based on the content."""
        prompt = f"Create 5 multiple-choice questions based on content between the content tags: <content>\n\n{content}\n\n</content>"
        return prompt


# Test the exam creator (you can remove this test in your actual application)
if __name__ == "__main__":
    exam_creator = ExamCreator()
    sample_content = "Your sample text content here."
    questions = exam_creator.generate_questions(sample_content)
    print(questions)
