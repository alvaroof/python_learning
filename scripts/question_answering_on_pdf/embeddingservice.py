# -*- coding: utf-8 -*-
from dotenv import load_dotenv

load_dotenv()

import numpy as np
import openai
from pypdf import PdfReader


class EmbeddingService:
    def __init__(self, pdf_path: str):
        self.openai_client = openai.OpenAI()
        self.pdf_path = pdf_path

        self.parsed_chunks = None
        self.embeddings = None

    def read_pdf(self, chunk_length: int):
        reader = PdfReader(self.pdf_path)
        chunks = []
        for page in reader.pages:
            text_page = page.extract_text()
            chunks.extend(
                [
                    text_page[i : i + chunk_length].replace("\n", " ")
                    for i in range(0, len(text_page), chunk_length)
                ]
            )
        self.parsed_chunks = chunks

    def get_embeddings(self, model="text-embedding-ada-002"):
        chunks = self.parsed_chunks
        if not isinstance(self.parsed_chunks, list):
            chunks = [self.parsed_chunks]
        self.embeddings = self.openai_client.embeddings.create(
            input=chunks, model=model
        )  # .data[0:len(chunks)].embedding

    def test_openai_client(self):
        completion = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
                },
                {
                    "role": "user",
                    "content": "Compose a poem that explains the concept of recursion in programming.",
                },
            ],
        )

        print(completion.choices[0].message)


if __name__ == "__main__":
    embed_service = EmbeddingService(pdf_path="data/pdf-example.pdf")
    embed_service.read_pdf(1000)
    print(embed_service.parsed_chunks[-1])
    embed_service.get_embeddings()
    embeddings = embed_service.embeddings
    parsed_chunks = embed_service.parsed_chunks
    print(
        f"We should have {len(embeddings.data)} different vector embeddings for {len(parsed_chunks)} different parsed chunks."
    )

    # df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
    # df.to_csv('output/embedded_1k_reviews.csv', index=False)
