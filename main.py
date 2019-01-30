import helpers
import glob
from threading import Thread

def main():
    # Two processes in two threads
    thread1 = Thread(target=helpers.mouse_pos)
    thread2 = Thread(target=helpers.test2Paint)
    print("*Starting Mouse Tracking!")
    thread1.start()
    print("@Starting Students Test!")
    thread2.start()

if __name__ == '__main__':
    
    # Read mouse data and upload in file
    # Works independently now
    #helpers.mouse_pos()
    
    # Get file paths and upload them
    #all_file_paths = glob.glob("files/*.txt")
    #print(all_file_paths)
    #helpers.upload_all(all_file_paths)
    #print("Done! Where's my cookie.")

    # compare two text files
    path_1 = "checkers/test.txt"
    path_2 = "checkers/test_case.txt"
    helpers.compare_files(path_1, path_2)