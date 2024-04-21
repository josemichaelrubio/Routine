import os
import time
import subprocess

def open_excel_sheet(excel_path):
    # Open the Excel sheet
    subprocess.Popen(["start", excel_path], shell=True)

def open_word_document(word_path):
    # Wait until the Excel sheet is closed
    while True:
        try:
            # Try to open the Word document
            subprocess.Popen(["start", word_path], shell=True)
            break
        except Exception:
            # If the Word document can't be opened, wait for a few seconds and try again
            time.sleep(5)

# Set the paths to the Excel sheet and Word document
excel_path = "path/to/excel.xlsx"
word_path = "path/to/word.docx"

# Call the functions to open the Excel sheet and wait for it to close, then open the Word document
open_excel_sheet(excel_path)
open_word_document(word_path)

# Print a success message
print(f"{excel_path} was opened and {word_path} will be opened after the Excel sheet is closed.")
