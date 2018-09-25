# file for logging
import os

# just going to write to the current path, log files

def InfoMessage(message):
    with open(f"{os.curdir}/LogFile.txt", 'a') as f:
        f.write(f"Info Message: {message}\n")

def ErrorMessage(message):
    with open(f"{os.curdir}/LogFile.txt", 'a') as f:
        f.write(f"Error Message: {message}\n")