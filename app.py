from flask import Flask, jsonify, request
from mylib.udmx import uDMX
from mylib.pwmdriver import Servo
import importlib
app = Flask(__name__)
try:
    dmx = uDMX()
except:
    print("uDMX Device not found")
from mylib.soundmanager import SoundManager
import os, time
from time import sleep
import requests

@app.route('/')
def default():
    dmx.resetFixtures()
    return jsonify(dmx.fixtures)

@app.route('/set_from_json', methods=["POST"])
def set_from_json():
    json = request.get_json()

    for entry in json:
        for fixture in entry.get("fixtures"):
            dmx.setFixtureValues(fixture, entry.get("channels"))

    dmx.update(entry.get("fixtures"))
    return jsonify(dmx.fixtures)

@app.route('/playscript', methods=["GET"])
def playscript():
    scriptname = request.args.get("script")
    pos = request.args.get("pos", 0)
    duration = request.args.get("duration")
    script = importlib.import_module("scripts." + scriptname)
    script.play(dmx = dmx, args = request.args, pos=pos, duration=duration)

    return jsonify(dmx.fixtures)

@app.route('/doorbell', methods=["GET"])
def doorbell():
    ############Set hue in entry area to blue
    url = "http://192.168.178.46/api/xtndDDnn4UblMG-JH1uu6ka8HiouI9Wa66liRYly/lights/14/state"

    payload = "{\"on\":true, \"xy\":[0.1206,0.05]}"
    headers = {}

    response = requests.request("PUT", url, data=payload, headers=headers)
    ############################################

    ############# Reduce music volume to 50%
    url = "http://192.168.178.53:9090/requests/status.xml"
    querystring = {"command": "volume", "val": "128"}
    headers = {
        'cache-control': "no-cache",
        "Authorization": "Basic OmZvb2Jhcg=="
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    ############################################

    ########### Play doorbell sound
    sm = SoundManager()
    sm.playFX(FX_name="doorbell", loops=1, maxtime=30000)
    script = importlib.import_module("scripts.lightning")
    time.sleep(1)
    script.play(dmx=dmx)
    time.sleep(4.5)
    script.play(dmx=dmx)
    time.sleep(10)
    ############################################

    ############ Reset music volume to 100%
    url = "http://192.168.178.53:9090/requests/status.xml"

    querystring = {"command": "volume", "val": "256"}

    headers = {
        'cache-control': "no-cache",
        "Authorization": "Basic OmZvb2Jhcg=="
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    ############################################

    time.sleep(11.5)
    script = importlib.import_module("scripts.door")
    script.play(dmx=dmx, args=request.args)

    return "Ok"

@app.route('/start_music', methods=["GET"])
def start_music():
    #bashCommand = "mount /mnt/homeserver"
    #os.system(bashCommand)

    #bashCommand = "vlc --http-host 192.168.178.53 --http-port 9090 --http-password foobar --loop /mnt/homeserver/Music/Halloween/playlist.m3u &"
    #os.system(bashCommand)

    return "Ok"

@app.route('/servo', methods=["POST"])
def servo():
    s = Servo()
    s.speak("paule")
    #json = request.get_json()
    #settings = json.get("servos")
    #for key, value in settings.items():
    #    s.set(key, value)
    #    sleep(1)

    return jsonify("foo")


@app.route('/health')
def health():
    return "foobar"

if __name__ == '__main__':
    app.run(host='localhost',port=8081, debug=True)
