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
    
def type_word(word: str, wpm: float = 150, errors: bool = True, error_percentage = 2) -> None:
    """Types word at wpm

    Args:
        word (str): Word to type
        wpm (float, optional): Average wpm to type at. Defaults to 150.
        errors (bool, optional): Allows orsrre. Defaults to True.
        error_percentage (int, optional): Error percentage. Defaults to 2.
    """
    long_word: int = 8
    wpm = np.random.normal(wpm - 20, 5) if len(word) >= long_word else wpm
    average_pause = get_pause(wpm)
    error_pause = get_pause(wpm * .8)
    for i, letter in enumerate(word):
        if errors and (np.random.random() * 100) <= error_percentage and i not in [0, len(word) - 1] and letter not in [' ', '-', "'", ',', '.']:
            send(get_close_letter(letter))
            time.sleep(np.random.normal(error_pause, error_pause * .1))
            send(Key.backspace)
            time.sleep(np.random.normal(average_pause, average_pause * .1))
        send(letter)
        if i != len(word) - 1:
            time.sleep(np.random.normal(average_pause, average_pause * .1))

def type_content(content: str, wpm: float = 150, errors: bool = False, error_percentage = 2) -> None:
    """Types content at wpm
    Args:
        content (str): Content to type
        wpm (float, optional): Average wpm to type at. Defaults to 150.
        errors (bool, optional): Allows errors. Defaults to False.
        error_percentage (int, optional): Error percentage. Defaults to 2.
    """
    average_pause = get_pause(wpm)
    words = content.split()
    for i, word in enumerate(words):
        type_word(word, wpm, errors, error_percentage)
        if i != len(words) - 1:
            time.sleep(np.random.normal(average_pause, average_pause * .1))
            send(Key.space)
            time.sleep(np.random.normal(average_pause, average_pause * .1))