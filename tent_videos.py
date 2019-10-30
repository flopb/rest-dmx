from os import listdir, popen
from os.path import isfile, join
import random
import subprocess
from time import sleep


path="F:/Docker/rest-dmx/videos/"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]


while True:
    wait_timer = random.randint(65, 360)
    file = random.choice (onlyfiles)
    file_name = path + file

    p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe", "file:///"+ file_name, "--fullscreen", "--play-and-pause"])
    print("Starting waittimer", wait_timer)
    sleep(wait_timer)