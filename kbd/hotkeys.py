from kbd.controller import Key, Listener
from threading import Event
import time

def wait(until: Key, callback: callable = lambda: None, output = True) -> Listener:
    """Wait Until Key Is Pressed and Activate Callback

    Args:
        until (Key): Key to Wait For
        callback (_type_, optional): Function to Activate on Key Press. Defaults to lambda:None.
        output (bool, optional): Prints Notification Message to Console. Defaults to True.

    Returns:
        Listener: Listener Object
    """
    def action(key):
        if key == until:
            callback()
            listener.stop()
    listener = Listener(on_press=action)
    listener.start()
    print(f'Waiting for {until.name} to be pressed. . .')
    listener.join()
    return listener

def once(key: Key, callback: callable = lambda: None, message: str = 'One Use Hotkey', init_output: bool = True, output = True) -> Listener:
    """Initializes A One Time Use Hotkey

    Args:
        key (Key): Key to Listen For
        callback (_type_, optional): Function to Activate on Key Press. Defaults to lambda:None.
        message (str, optional): Hotkey Message. Defaults to 'One Use Hotkey'.
        init_output (bool, optional): Prints Notification Message to Console. Defaults to True.
        output (bool, Prints Notification Message to Console upon Activation): _description_. Defaults to True.
    Returns:
        Listener: Listener Object
    """
    def action(event):
        if event == key:
            if output:
                print(f'Activated {message}')
            callback()
            listener.stop()
    listener = Listener(on_press=action)
    listener.start()
    if init_output:
        print(f'{message}: [{key.name}]')
    return listener

def toggle(key: Key, callback: callable = lambda: print('on'), message: str = 'Toggle Hotkey', output: bool = True, sleep_time: float = .1) -> Listener:
    """Continuously Runs Callback Once Hotkey is Toggled

    Args:
        key (Key): Key to Listen For
        callback (_type_, optional): Function to Activate on Toggle. Defaults to lambda:print('on').
        message (str, optional): Hotkey Message. Defaults to 'Toggle Hotkey'.
        output (bool, optional): Prints Notification Message to Console. Defaults to True.
        sleep_time (float, optional): Time to Sleep Between Invocations. Defaults to .1.

    Returns:
        Listener: Listener Object
    """
    def loop():
        stop_event = Event()

        def stop():
            stop_event.set()
            print(f'Stopped {message}')

        # Define Stop
        once(key, stop, init_output = False, output = False)

        while not stop_event.is_set():
            callback()
            time.sleep(sleep_time)

        # Define Start
        once(key, loop, message, init_output = False, output = True)

    once(key, loop, message)
    
def hotkey(key: Key, callback: callable = lambda: None, message: str = 'Hotkey Initialized', output: bool = True) -> Listener:
    """Initializes Hotkey

    Args:
        key (Key): Key to Listen For
        callback (_type_, optional): Function to Activate on Key Press. Defaults to lambda:None.
        message (str, optional): Hotkey Message. Defaults to 'Hotkey Initialized'.
        output (bool, optional): Prints Notification Message to Console. Defaults to True.

    Returns:
        Listener: Listener Object
    """
    def action(event):
        if event == key:
            callback()
    listener = Listener(on_press=action)
    listener.start()
    print(f'{message}: [{key.name}]')
    return listener