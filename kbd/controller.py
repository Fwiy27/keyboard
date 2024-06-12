from pynput.keyboard import Controller, Key, Listener
from kbd.utils import get_pause, get_close_letter
import numpy as np
import string
import time

controller = Controller()

def send(key: Key) -> None:
    """Send Key

    Args:
        key (Key): Key to send 
    """
    controller.press(key) 
    controller.release(key)

def type_word(word: str, wpm: float = 150, errors: bool = True, error_percentage: float = 2, pause = True) -> None:
    """Type Word Given WPM

    Args:
        word (str): Word to type out
        wpm (float, optional): Word per minute to type at. Defaults to 150.
        errors (bool, optional): Allows errors. Defaults to True.
        error_percentage (float, optional): Error percentage. Defaults to 2.
        pause (bool, optional): Pause at end of word. Defaults to True.
    """
    wpm = wpm if not errors else abs(np.random.normal(wpm, 40))
    average_pause = get_pause(wpm)
    
    for i, letter in enumerate(word):
        same_as_previous: bool = False if i == 0 else (letter == word[i-1])
    
        if errors and np.random.random() * 100 <= error_percentage and not same_as_previous and letter in string.ascii_letters:
            send(get_close_letter(letter))
            time.sleep(average_pause)
            send(Key.backspace)
            time.sleep(average_pause)
            send(letter)
        else:
            send(letter)
    
        if i != len(word) - 1:
            time.sleep(average_pause) if not same_as_previous else time.sleep(average_pause / 2)           
        elif pause:
            time.sleep(average_pause)
        
def type_content(content: str, wpm: float = 150, errors: bool = False, error_percentage = 2) -> None:
    """Type content

    Args:
        content (str): Content to type
        wpm (float, optional): Word per minute to type at. Defaults to 150.
        errors (bool, optional): Allows errors. Defaults to False.
        error_percentage (int, optional): Error percentage. Defaults to 2.
    """
    words = content.split(' ')
    for i, word in enumerate(words):
        pause: bool = i != len(words) - 1
        type_word(word, wpm, errors, error_percentage, pause)
        if pause:
            send(Key.space)
            time.sleep(get_pause(np.random.normal(wpm - 40, 20)))