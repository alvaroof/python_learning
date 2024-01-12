# -*- coding: utf-8 -*-
from exam_generator.exam_creator import ExamCreator
from file_processor.docx_processor import DOCXProcessor
from file_processor.pdf_processor import PDFProcessor
from file_processor.ppt_processor import PPTProcessor
from pdf_creator.pdf_exporter import PDFExporter
from utils.file_uploader import FileUploader


def process_file(file_path):
    """Determines the file type and processes it using the appropriate processor."""
    if file_path.endswith(".pdf"):
        return PDFProcessor.process_pdf(file_path)
    elif file_path.endswith(".pptx"):
        return PPTProcessor.process_ppt(file_path)
    elif file_path.endswith(".docx"):
        return DOCXProcessor.process_docx(file_path)
    else:
        print("Unsupported file format.")
        return None


def main():
    print("Welcome to the Exam Generator!")
    file_path = FileUploader.upload_file()
    content = process_file(file_path)

    if content:
        print("File processed successfully.")
        exam_creator = ExamCreator()
        exam_questions = exam_creator.generate_questions(content)
        if exam_questions:
            print("Exam generated successfully.")
            pdf_exporter = PDFExporter()
            pdf_exporter.create_pdf(exam_questions, "generated_exam.pdf")
            print("Exam exported as PDF successfully.")
        else:
            print("Failed to generate exam.")
    else:
        print("Failed to process the file.")


if __name__ == "__main__":
    main()
