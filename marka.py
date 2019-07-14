from pygame import mixer  # Load the required library
import keyboard

startpos = 5000
duration = None

## Set filename of music-title
file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.ogg"
mixer.init()
mixer.music.load(file_name)
mixer.music.play(0, startpos/1000)

currenttime = 0
positions=[]
def triggered(key):
    positions.append({str(key) : currenttime})
    print(currenttime, key)
keyboard.on_press(triggered, suppress=False)

def show_positions():
    print("Recorded positions:", positions)

while mixer.music.get_busy():
    currenttime = mixer.music.get_pos() + startpos
    #f keyboard.is_pressed('q'):  # if key 'q' is pressed
    #    print('You Pressed A Key!')
    if duration is not None and currenttime > startpos + duration:
        mixer.music.stop()

show_positions()