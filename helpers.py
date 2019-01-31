import subprocess
import filecmp
import os
from pynput.mouse import Controller
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


def mouse_pos():
    '''Opens a text file and dumps mouse data in it
        until the function exits
    '''
    f_name = input("Enter file name: ")
    # Rename file
    f_name += ".txt"
    # Opens txt file in files directory
    f = open("files/{}".format(f_name), "w+")
    # Init controller
    mouse = Controller()

    while(1):
        print( mouse.position )
        # Store location in txt file
        f.write("{} \n".format(str(mouse.position)))
    f.close()




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
        


# NEEDS MAJOR FIX
def test2Paint():
    '''Dont know what it does
    '''
    program = subprocess.call(['kate', 'test.txt'])
    
    while(1):
        if(filecmp.cmp('test.txt', 'test_case.txt')):
            break
        else:
            print("No match found!")
            subprocess.call(['kate', 'test.txt'])

    program2 = subprocess.call('inkscape')
