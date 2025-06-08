# src/core/formats/pdf_cracker.py
import PyPDF2

class PdfCracker:
    def __init__(self, file_path):
        self.file_path = file_path

    def try_password(self, password):
        try:
            with open(self.file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                if reader.is_encrypted:
                    if reader.decrypt(password):
                        return True
                    else:
                        return False
                else:
                    # File is not encrypted, should not happen if selected by user
                    print(f"Warning: PDF file '{self.file_path}' is not encrypted.")
                    return True # Or False, depending on desired behavior
        except FileNotFoundError:
            print(f"Error: PDF file not found at {self.file_path}")
            return False
        except Exception as e:
            # PyPDF2 can raise various exceptions
            print(f"Error cracking PDF file: {e}")
            return False
