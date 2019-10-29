import keyboard

def fadeout():
    print("Got fadeout command")
    keyboard.press_and_release('ctrl+p')

def fadein():
    print("Got fadein command")
    keyboard.press_and_release('ctrl+g')
