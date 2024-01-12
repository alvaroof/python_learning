# -*- coding: utf-8 -*-
import PyPDF2


class PDFProcessor:
    @staticmethod
    def process_pdf(file_path):
        """Processes the PDF file and extracts its content."""
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            content = []
            for page in range(pdf_reader.numPages):
                content.append(pdf_reader.getPage(page).extractText())
            return " ".join(content)


# Test the processor (you can remove this test in your actual application)
if __name__ == "__main__":
    pdf_content = PDFProcessor.process_pdf("path_to_your_pdf.pdf")
    print(pdf_content)
