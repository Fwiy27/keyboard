import numpy as np
import string

def get_close_letter(letter: str) -> str:
    """Get Close Letter, Used for Errors

    Args:
        letter (str): Letter to Get Close

    Returns:
        str: Close Letter
    """
    close = {
        'q': ['w', 'a', 's'],
        'w': ['q', 'e', 's'],
        'e': ['r', 'd', 'w'],
        'r': ['t', 'e', 'f'],
        't': ['y', 'r', 'g', 'f'],
        'y': ['u', 't', 'h'],
        'u': ['i', 'y', 'j'],
        'i': ['o', 'u', 'j'],
        'o': ['i', 'p', 'l'],
        'p': ['l', ';'],
        'a': ['s', 'q'],
        's': ['w', 'a', 'd'],
        'd': ['e', 'f'],
        'f': ['g'],
        'g': ['h'],
        'h': ['g'],
        'j': ['h'],
        'k': ['l', 'j'],
        'l': [';', 'k'],
        'z': ['x', 'a'],
        'x': ['z', 'c'],
        'c': ['v', 'x'],
        'v': ['c', 'b'],
        'b': ['n', 'v', 'g'],
        'n': ['m', 'b'],
        'm': ['n'],
    }

    close: str = np.random.choice(close[letter.lower()])
    lowercase = True if letter in string.ascii_lowercase else False
    return close if lowercase else close.upper()

def get_pause(wpm: int, average_word_length: float = 5.1) -> float:
    """Returns Sleep Time Between Characters Given WPM

    Args:
        wpm (int): Desired WPM
        average_word_length (float, optional): Average Word Length. Defaults to 5.1.

    Returns:
        float: Sleep Time Between Characters Given WPM
    """
    average_pause_between_letters = 60 / (wpm * average_word_length)
    return average_pause_between_letters