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

# NOT CONTINUING SEQUENCE:
#! onenote_path = os.getenv('WINDOWS_ONENOTE_PATH')
onenote_path = os.getenv('MAC_ONENOTE_PATH')
todoist_path = os.getenv('MAC_TODOIST_PATH')
gcal_path = os.getenv('MAC_GCAL_PATH')

#TODO change paths to windows apps
# gCal: Review the week
open_app(gcal_path)
# OneNote: Mind Dump and Refine Monthly Goals
open_app(onenote_path)
# Plan upcoming Week
open_app(todoist_path)
open_app(gcal_path)