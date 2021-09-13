import win32api
import os
from os.path import isfile, join, isdir
from shutil import copyfile


def read_extensions():
    with open('extensions', 'rb') as ext_file:
        line = ext_file.readline()
        extensions = line.decode().split(sep=',')
        print(extensions)
        return extensions


def process_dir(directory, extensions):
    for element in os.listdir(directory):
        joined = join(directory, element)
        if isfile(joined):
            print(element)

            if any(extension in element for extension in extensions):
                # print(joined)
                # command = 'copy ' + joined + ' .\\found\\'
                copyfile(joined, '.\\found\\')
                print(joined)
            if element.endswith("pdf"):
                print(element)


        elif isdir(joined):
            try:
                process_dir(joined, extensions)
            except Exception:
                pass


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
os.system('mkdir found')
cur_dir = os.path.abspath(os.getcwd())
cur_dir += '\\found'

exts = read_extensions()

for drive in enumerate(drives):
    try:
        process_dir(drive[1], exts)
    except Exception:
        pass
