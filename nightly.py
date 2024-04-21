import subprocess
import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

# Function to open an Excel file and wait for it to close
def open_and_wait_excel(excel_path):
    if sys.platform.startswith('darwin'):
        subprocess.call(['open', excel_path])
    else:
        subprocess.Popen(['start', excel_path], shell=True)
    print("Excel opened. Please close it to continue...")
    input("Press Enter after you have closed Excel...")

# Function to open a Word document
def open_word(word_path):
    if sys.platform.startswith('darwin'):
        subprocess.call(['open', word_path])
    else:
        subprocess.Popen(['start', word_path], shell=True)

# Function to open an application on macOS
def open_mac_app(app_name):
    subprocess.call(['open', f'/Applications/{app_name}.app'])

# Function to open OneNote to a specific section
# This is a placeholder as opening OneNote to a specific section may require additional steps or use of the OneNote API
def open_onenote_section(section_path):
    print("This function needs to be implemented based on OneNote API or specific system commands.")

# Function to open ToDoist
# This is a placeholder as opening ToDoist may require the use of the ToDoist API or specific system commands
def open_todoist():
    print("This function needs to be implemented based on ToDoist API or specific system commands.")

# Paths to the Excel and Word files
excel_path = os.getenv('VIRTUES_EXCEL_PATH')
word_path = os.getenv('DEFINITE_STATEMENT_WORD_PATH')

# Names of the macOS applications
mac_app_name = 'AppOnMac'  # Replace with the actual app name
onenote_section_path = 'path/to/onenote/section'  # Replace with the actual path or identifier
todoist_path = 'path/to/todoist'  # Replace with the actual path or identifier

# Running the sequence of actions
open_and_wait_excel(excel_path)
open_word(word_path)
if sys.platform.startswith('darwin'):
    open_mac_app(mac_app_name)
open_onenote_section(onenote_section_path)
open_todoist()
