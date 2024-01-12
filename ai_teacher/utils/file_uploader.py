# -*- coding: utf-8 -*-
import os


class FileUploader:
    @staticmethod
    def upload_file():
        """Prompts the user to enter the file path and checks if the file exists.

        Returns the path if the file exists, otherwise prompts again.
        """
        while True:
            file_path = input("Enter the path of your file: ")
            if os.path.isfile(file_path):
                return file_path
            else:
                print("File not found. Please try again.")


# Test the uploader (you can remove this test in your actual application)
if __name__ == "__main__":
    uploader = FileUploader()
    file_path = uploader.upload_file()
    print(f"File {file_path} uploaded successfully.")
