import helpers
import glob
from threading import Thread
import Data_Logger


def main():
    # Two processes in two threads
    thread1 = Thread(target=Data_Logger.mouse_pos)
    thread2 = Thread(target=helpers.test2Paint)
    thread3 = Thread(target=Data_logger.Keyboard_logger)
    print("*Starting Mouse Tracking!")
    thread1.start()
    print("@Starting Students Test!")
    thread2.start()
    print("*Starting Keyboard Logging")
    thread3.start()

if __name__ == '__main__':
    
    '''
    Read mouse data
    '''
    #helpers.mouse_pos()
    '''
    Upload files to drive
    '''   
    #all_file_paths = glob.glob("files/*.txt")
    #helpers.upload_all(all_file_paths)
    
    '''
    Compare two text files
    '''
    #path_1 = "checkers/test.txt"
    #path_2 = "checkers/test_case.txt"
    #helpers.compare_files(path_1, path_2)

    helpers.test2Paint()

    #main()
