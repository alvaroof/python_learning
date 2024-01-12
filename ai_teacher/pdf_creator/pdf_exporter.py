# -*- coding: utf-8 -*-
from fpdf import FPDF


class PDFExporter:
    def __init__(self):
        self.pdf = FPDF()

    def create_pdf(self, content, file_name="exam.pdf"):
        """Creates a PDF file from the provided content."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.output(file_name)


# Test the PDF exporter (you can remove this test in your actual application)
if __name__ == "__main__":
    exporter = PDFExporter()
    sample_content = "Your sample exam content here."
    exporter.create_pdf(sample_content, "sample_exam.pdf")
