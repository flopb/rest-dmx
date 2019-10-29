from pygame import mixer  # Load the required library
import threading
import urllib.request

virtualdj_running=True
def runScript(file_name, startpos, script, duration, dmx):
    global virtualdj_running
    try:
        if virtualdj_running:
            content = urllib.request.urlopen("http://desktop-4iq6unj:8080/fadeout",timeout=1).read()
            virtualdj_running = False
            print("Stopping VIrtual DJ:", content)
    except:
        pass
    mixer.init()
    mixer.music.load(file_name)
    # mixer.music.set_pos(5)
    mixer.music.play(0, startpos / 1000)
    print("-----START-----")
    if startpos != 0:
        for key in script.keys():
            if (str(key)[0] == "a"):
                # print("Found audio key", key)
                time = int(str(key)[1:])
            else:
                time = key
            if startpos > time:
                script[key] = "done"

    while mixer.music.get_busy():
        currenttime = mixer.music.get_pos() + startpos
        if duration is not None and currenttime > (startpos + duration):
            mixer.music.stop()
        for key in script.keys():
            if(str(key)[0] == "a"):
                #print("Found audio key", key)
                time = int(str(key)[1:])
            else:
                time = key

            if currenttime >= time and type(script[key]) == list:
                print("Play Script:", key)
                for func in script[key]:
                    #t1 = threading.Thread(target=func)
                    #t1.setDaemon(True)
                    #t1.start()
                    func()
                    script[key] = "done"

    try:
        dmx.activateAutoMode()
        if not virtualdj_running:
            content = urllib.request.urlopen("http://desktop-4iq6unj:8080/fadein", timeout=1).read()
            virtualdj_running = True
            print("Starting VIrtual DJ:", content)
    except:
        pass

def stop(dmx):
    try:
        values = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        dmx.set_all_rgb(values)
        dmx.update()
        mixer.music.stop()
    except:
        pass