import subprocess
import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

# Function to open a Word document
def open_app(path):
    if sys.platform.startswith('darwin'):
        subprocess.call(['open', path])
    else:
        subprocess.Popen(['start', path], shell=True)


word_path = os.getenv('DEFINITE_STATEMENT_WORD_PATH')
onenote_path = os.getenv('WINDOWS_ONENOTE_PATH')

# Running the sequence of actions
open_app(word_path)
open_app(onenote_path)


