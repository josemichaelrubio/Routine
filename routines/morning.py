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
outlook_path = os.getenv('MAC_OUTLOOK_PATH')
gcal_path = os.getenv('MAC_GCAL_PATH')

#TODO change paths to windows apps
open_app(word_path)
open_app(onenote_path)
open_app(gcal_path)
open_app(todoist_path)
open_app(outlook_path)