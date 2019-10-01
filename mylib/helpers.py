from pygame import mixer  # Load the required library
import threading

def runScript(file_name, startpos, script, duration):
    mixer.init()
    mixer.music.load(file_name)
    # mixer.music.set_pos(5)
    mixer.music.play(0, startpos / 1000)

    if startpos != 0:
        for key in script.keys():
            if startpos > key:
                script[key] = "done"

    while mixer.music.get_busy():
        currenttime = mixer.music.get_pos() + startpos
        if duration is not None and currenttime > (startpos + duration):
            mixer.music.stop()
        for key in script.keys():
            if currenttime >= key and type(script[key]) == list:
                print("Play Script:", key)
                for func in script[key]:
                    #t1 = threading.Thread(target=func)
                    #t1.setDaemon(True)
                    #t1.start()
                    func()
                    script[key] = "done"

def stop(dmx):
    values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
    dmx.set_all_rgb(values)
    # dmx.update()
    mixer.music.stop()