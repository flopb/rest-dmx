from flask import Flask, jsonify, request
from lib.udmx import uDMX
import importlib
app = Flask(__name__)
dmx = uDMX()

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

    script = importlib.import_module("scripts." + scriptname)
    script.play(dmx = dmx, args = request.args)

    return jsonify(dmx.fixtures)

@app.route('/health')
def health():
    return "foobar"

if __name__ == '__main__':
    app.run(host='192.168.178.53',port=5010)
