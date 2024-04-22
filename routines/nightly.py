import subprocess
import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

def open_app(path):
    if sys.platform.startswith('darwin'):
        proc = subprocess.Popen(['open', '-W', path])
        proc.wait()
    else:
        proc = subprocess.Popen(['start', path], shell=True)
        proc.wait()

word_path = os.getenv('DEFINITE_STATEMENT_WORD_PATH')
# NOT CONTINUING SEQUENCE:
#! onenote_path = os.getenv('WINDOWS_ONENOTE_PATH')
onenote_path = os.getenv('MAC_ONENOTE_PATH')
todoist_path = os.getenv('MAC_TODOIST_PATH')
gcal_path = os.getenv('MAC_GCAL_PATH')
excel_path = os.getenv('VIRTUES_EXCEL_PATH')

#TODO change paths to windows apps
# Open word definite statement
open_app(word_path)
# Open gCal
open_app(gcal_path)
# Open OneNote
open_app(onenote_path)
# Open Todoist
open_app(todoist_path)

# TODO: Okay there is an issue with Excel, it's not opening, it's opening the directory.
#! Open excel virtues sheet
open_app(excel_path)