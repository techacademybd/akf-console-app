import subprocess
import filecmp
import os
import glob
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

print("Logging in, wait...!")

# Authetication and login
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

print("Logged in!")

# ID for destination folder in test email (PyDrive Test in this case)
dest_id = "1JTXMaXBVZcuBplSF7wYrUvQpBDYYqKmF"


def upload_file(path):
    '''Takes input the file path in the directory
    Uploads the file in google drive folder (PyDrive Test)
    See uploaded files
    Link: https://drive.google.com/open?id=1JTXMaXBVZcuBplSF7wYrUvQpBDYYqKmF
    '''
    assert type(path) is str, "I need a string"
    # Upload in destionation folder 
    f = drive.CreateFile({"parents": [{"kind": "https://drive.google.com/open?id=1JTXMaXBVZcuBplSF7wYrUvQpBDYYqKmF", "id": dest_id}]})
    # Set the path to the file to be uploaded
    f.SetContentFile(path)
    # Some sick parsing done here!
    f['title'] = path[6:-4]
    f.Upload()
    #c:\Users\Tashfeen\Desktop\Hasib_TTA\akf-console-appC:\Users\Tashfeen\Desktop\Hasib_TTA\akf-console-appC:\Users\Tashfeen\Desktop\Hasib_TTA\akf-console-appC:\Users\Tashfeen\Desktop\Hasib_TTA\akf-console-appC:\Users\Tashfeen\Desktop\Hasib_TTA\akf-console-app
    # Some info!
    #print('Created file %s with mimeType %s' % (f['title'], f['mimeType']))


def upload_all(paths):
    '''Take input of all paths as a list of strings(paths) and
    uploads all files to drive
    '''
    assert type(paths) is list, "I need a list"
    for path in paths:
        upload_file(path)
    print("Successfully Uploaded!")


def compare_files(p1, p2):
    '''Args:
    p1: path for user file
    p2: path for test case file

    Compares two files and gives results
    '''
    assert type(p1) is str, "I need a string"
    assert type(p2) is str, "I need a string"
    
    # Compare the two text files
    if(filecmp.cmp(p1, p2)):
        print("Matched! You're awesome")
    else:
        print("No match found!")
        

def test2Paint():
    '''Opens notepad, if user gives the correct input
    then gets a reward - opens paint for drawing. During opening
    paint, the log files are uploaded in drive
    '''
    program = subprocess.call(['notepad', 'checkers/test.txt'])
    
    while True:

        if(filecmp.cmp('checkers/test.txt', 'checkers/test_case.txt')):
            print("Compared!")
            break
        else:
            print("No match found!")
            subprocess.call(['notepad', 'test.txt'])

    #print("Uploading files to drive....")
    #all_file_paths = glob.glob("files/*.txt")
    #upload_all(all_file_paths)
    
    print("Opening mspaint...")
    program2 = subprocess.call('mspaint.exe')
