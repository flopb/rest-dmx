from pygame import mixer  # Load the required library
import keyboard
import random

startpos = 0
duration = 15000

## Set filename of music-title
#file_name = "./sounds/Culcha_Candela_Monsta.mp3"
file_name = "./sounds/LMFAO_party_rock_anthem.mp3"
#file_name = "./sounds/Alice_Cooper_Feed_My_Frankenstein.mp3"
#file_name = "./sounds/intro.mp3"
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
            elif key == "t":
                content = 'script["a' + str(pos) + '"] = [f(s.speak, who=["paulinchen"], minmax=[350,450])] #' + str(key) + "\n"
            elif key == "z":
                content = 'script["a' + str(pos) + '"] = [f(s.stop, who=["paulinchen"])] #' + str(key) + "\n"
            elif key == "d":
                content = 'script["a' + str(pos) + '"] = [f(s.speak, who=["paulinchen"], minmax=[350,500])] #' + str(key) + "\n"
            elif key == "s":
                content = 'script["a' + str(pos) + '"] = [f(s.speak, who=["paulinchen"], minmax=[300,450])] #' + str(key) + "\n"
            elif key == "a":
                content = 'script["a' + str(pos) + '"] = [f(s.speak, who=["paulinchen"], minmax=[150,350])] #' + str(key) + "\n"
            elif str(key) == "nach-oben":
                content = 'script[' + str(pos) + '] = [f(fx.set_front_rgb, values=fx.' + color + '(), update=True, autoOff=False)] #' + str(key) + "\n"
            elif str(key) == "nach-unten":
                content = 'script[' + str(pos) + '] = [f(fx.set_floor_rgb, values=fx.' + color + '(), update=True, autoOff=False)] #' + str(key) + "\n"
            elif str(key) == "x":
                content = 'script[' + str(pos) + '] = [f(fx.rgb_crossfade, fixtures_out=["rgb4"], color=fx.blue(0), fixtures_in=["rgb6"], out_stepping=5, in_stepping=5, step_delay=0, end_brightness=255)] #' + str(key) + "\n"
            elif str(key) == "m":
                content = 'script[' + str(pos) + '] = [f(fx.mh_move_to, fixture = "gobo", rotation = 175, tilt = 0, speed = 70, update = True)] #' + str(key) + "\n"
            elif str(key) == "n":
                content = 'script[' + str(pos) + '] = [f(fx.mh_move_to, fixture = "gobo", rotation = 175, tilt = 255, speed = 70, update = True)] #' + str(key) + "\n"
            elif str(key) == "l":
                content = 'script[' + str(pos) + '] = [f(fx.set_rgb, fixtures=["rgb4","rgb5","rgb6"], values=fx.white(), update=True, autoOff=False)] #' + str(key) + "\n"


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