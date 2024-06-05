from pynput.keyboard import Controller, Key, Listener
from kbd.utils import get_pause, get_close_letter
import numpy as np
import string
import time

controller = Controller()

def send(key: Key) -> None:
    """Simulates Pressing and Releasing Key

    Args: 
        key (Key): Key to Press
    """
    controller.press(key)
    controller.release(key)
    
def type_content(content: str, wpm: float = 150, errors: bool = False, error_percentage = 2) -> None:
    """Types Content at Given WPM with Optional Errors

    Args:
        content (str): Content You Want Typed
        wpm (float, optional): Average WPM Desired. Defaults to 150.
        errors (bool, optional): Allows Errors in Typing. Defaults to False.
        error_percentage (int, optional): Percentage of Error Occuring. Defaults to 2.
    """
    average_sleep_time: float = get_pause(wpm)
    error_delay: float = average_sleep_time * 2.4

    last_index = len(content) - 1

    for i, character in enumerate(content):
        if errors and character in string.ascii_letters and (np.random.random() * 100) < error_percentage and i != last_index:
            send(get_close_letter(character))
            time.sleep(error_delay)
            send(Key.backspace)
            time.sleep(error_delay)
        send(character)
        if i != last_index:
            pause_time = abs(np.random.normal(average_sleep_time, average_sleep_time / 7))
            time.sleep(pause_time)