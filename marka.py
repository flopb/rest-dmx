from pygame import mixer  # Load the required library
import keyboard
import random

startpos = 80000
duration = 15000

## Set filename of music-title
file_name = "./sounds/Culcha_Candela_Monsta.mp3"
#file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"
#file_name = "./sounds/Pirates_of_the_Caribbean.mp3"
mixer.init()
mixer.music.load(file_name)
mixer.music.play(0, startpos/1000)

currenttime = 0
positions=[]
def triggered(key):
    positions.append((key.name , currenttime))
    print(currenttime, key)
keyboard.on_press(triggered, suppress=False)

def show_positions():
    print("Recorded positions:", positions)

def save_script():
    colors = ["red", "blue", "green"]
    color = random.choice(colors)
    previousColor = None
    with open("./marka_script.py", "w+") as file:
        for key, pos in positions:
            while color == previousColor:
                color = random.choice(colors)
            if  key == "strg down":
                color = "white"

            if key == "1":
                content = 'script[' + str(pos) + '] = [f(fx.blackout)] #' + str(key) + "\n"
            elif key == "2":
                content = 'script[' + str(pos) + '] = [f(fx.racer, color_brgbw=[255, 255, 0, 0, 0], splittime=0.1, laps=1, reverse=False)] #' + str(key) + "\n"
            else:
                content = 'script[' + str(pos) + '] = [f(fx.set_back_rgb, values=fx.' + color + '(), update=True, autoOff=False)] #' + str(key) + "\n"
            previousColor = color
            file.write(content)


while mixer.music.get_busy():
    currenttime = mixer.music.get_pos() + startpos
    #f keyboard.is_pressed('q'):  # if key 'q' is pressed
    #    print('You Pressed A Key!')
    if duration is not None and currenttime > startpos + duration:
        mixer.music.stop()

show_positions()
save_script()