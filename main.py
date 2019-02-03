import helpers
from threading import Thread
import logger

def main():
    '''
    Run the seperate processes
        * Collect mouse pointer data
        * Collect keyboard logs
        * Run notepad to paint app
    '''
    thread1 = Thread(target=logger.mouse_pos)
    thread2 = Thread(target=helpers.test2Paint)
    thread3 = Thread(target=logger.keyboard_logger)
    
    print("*Starting Mouse Tracking!")
    thread1.start()
    print("@Starting Students Test!")
    thread2.start()
    print("*Starting Keyboard Logging")
    thread3.start()


if __name__ == '__main__':
    '''
    Run notepad and open paint if correct answer given
    '''
    #helpers.test2Paint()
    #main()
    #print("Done!")