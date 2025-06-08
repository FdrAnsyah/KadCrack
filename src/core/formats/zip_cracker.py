# src/core/formats/zip_cracker.py
import zipfile
import os

class ZipCracker:
    def __init__(self, file_path):
        self.file_path = file_path

    def try_password(self, password):
        try:
            with zipfile.ZipFile(self.file_path, 'r') as zf:
                zf.extractall(pwd=password.encode('utf-8'))
            return True
        except (RuntimeError, zipfile.BadZipFile) as e:
            # RuntimeError: Bad password
            # BadZipFile: Corrupted or not a zip file
            return False
        except Exception as e:
            # Handle other potential errors like disk full, permission issues
            print(f"Error cracking ZIP file: {e}")
            return False
        finally:
            # Clean up extracted files if any, for testing purposes
            # In a real tool, you might not extract but just check password validity
            pass
