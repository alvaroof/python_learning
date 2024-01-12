# -*- coding: utf-8 -*-
import docx


class DOCXProcessor:
    @staticmethod
    def process_docx(file_path):
        """Processes the Word file and extracts its content."""
        doc = docx.Document(file_path)
        content = [paragraph.text for paragraph in doc.paragraphs]
        return " ".join(content)


# Test the processor (you can remove this test in your actual application)
if __name__ == "__main__":
    docx_content = DOCXProcessor.process_docx("path_to_your_docx.docx")
    print(docx_content)
