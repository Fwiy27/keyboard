import kbd

"""
hotkey() initalizes a hotkey
send() sends a character or key
""" 
kbd.hotkey(
    key = kbd.Key.cmd_r, 
    callback = lambda: kbd.send('a'), 
    message = 'Hotkey Initalized', 
    output = True
)

"""
once() initalizes a one time event hotkey
type_content() types content in a realistic manner at set wpm
"""
kbd.once(
    key = kbd.Key.alt_r,
    callback = lambda: kbd.type_content(
        content = 'this is a one time event hotkey',
        wpm = 75,
        errors = True,
        error_percentage = 15
    ),
    message = 'One Use Hotkey',
    init_output = True,
    output = True,
)

"""
toggle() initializes hotkey that runs callback continuously with break of {sleep_time} between invocations
"""
kbd.toggle(
    key = kbd.Key.shift_r,
    callback = lambda: print('activated'),
    message = 'Toggle',
    output = True,
    sleep_time = 1
)

"""
wait() waits for key to be pressed before moving on
"""
kbd.wait(
    until = kbd.Key.esc, 
    callback = lambda: exit(),
    output = True
)