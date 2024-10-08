import time
from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define state variables for Autoblow
autoblow_state = {
    "connected": True,
    "cluster": "192.168.1.129:5000",
    "operationalMode": "ONLINE_CONNECTED",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 0,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "",
    "syncScriptLoop": False
}

# Autoblow API routes
@app.route('/autoblow/connected', methods=['GET'])
def get_connected_status():
    return jsonify({"connected": autoblow_state["connected"], "cluster": autoblow_state["cluster"]}), 200

@app.route('/autoblow/oscillate', methods=['PUT'])
def oscillate():
    autoblow_state["operationalMode"] = "OSCILLATOR_PLAYING"
    return jsonify(autoblow_state), 200

@app.route('/autoblow/sync-script/offset', methods=['PUT'])
def offset():
    data = request.get_json()
    autoblow_state["syncScriptOffsetTime"] = data.get("offsetTime", 100)
    autoblow_state["operationalMode"] = "SYNC_SCRIPT_PAUSED"
    return jsonify(autoblow_state), 200

@app.route('/autoblow/info', methods=['GET'])
def info():
    return jsonify({
        "firmwareStatus": "UP_TO_DATE",
        "firmwareVersion": 1.01,
        "firmwareBranch": "prod",
        "hardwareVersion": "ultra",
        "mac": "b0b21c3141e8"
    }), 200

@app.route('/autoblow/state', methods=['GET'])
def state():
    return jsonify(autoblow_state), 200

@app.route('/autoblow/sync-script/upload-csv-url', methods=['PUT'])
def upload():
    autoblow_state["syncScriptToken"] = "346d0210-3708-48c8-8e1c-55f3ed1960ec"
    autoblow_state["operationalMode"] = "SYNC_SCRIPT_PAUSED"
    return jsonify(autoblow_state), 200

@app.route('/autoblow/sync-script/start', methods=['PUT'])
def start():
    autoblow_state["operationalMode"] = "SYNC_SCRIPT_PLAYING"
    autoblow_state["syncScriptCurrentTime"] = 15
    return jsonify(autoblow_state), 200

@app.route('/autoblow/sync-script/stop', methods=['PUT'])
def stop():
    autoblow_state["operationalMode"] = "SYNC_SCRIPT_PAUSED"
    return jsonify(autoblow_state), 200

@app.route('/autoblow/sync-script/load-token', methods=['PUT'])
def tokenload():
    autoblow_state["syncScriptToken"] = "ea5d85d2-4db7-4f76-88fe-23a6fb5a8eab"
    autoblow_state["operationalMode"] = "SYNC_SCRIPT_PAUSED"
    return jsonify(autoblow_state), 200

@app.route('/autoblow/goto', methods=['PUT'])
def goto():
    data = request.get_json()
    autoblow_state["position"] = data.get("position", None)
    autoblow_state["oscillatorTargetSpeed"] = data.get("speed", 50)
    autoblow_state["operationalMode"] = "GO_TO"
    return jsonify(autoblow_state), 200

# Handy API setup
handy_api = Blueprint('handy_api', __name__, url_prefix='/api/handy/v2')

# State variables for Handy
handy_state = {
    "server_time_offset": 0,
    "slide_min": 0,
    "slide_max": 100,
    "connected": True
}

# Handy API routes
@handy_api.route('/connected', methods=['GET'])
def get_connected():
    return jsonify({"connected": handy_state["connected"]}), 200

@handy_api.route('/slide', methods=['PUT'])
def put_slide():
    data = request.get_json()
    handy_state["slide_min"] = data.get('min', handy_state["slide_min"])
    handy_state["slide_max"] = data.get('max', handy_state["slide_max"])
    return jsonify({"result": 0}), 200

@handy_api.route('/hstp/offset', methods=['PUT'])
def put_hstp_offset():
    data = request.get_json()
    handy_state["server_time_offset"] = data.get('offset', 0)
    return jsonify({"result": 0}), 200

@handy_api.route('/hstp/offset', methods=['GET'])
def get_hstp_offset():
    return jsonify({"result": 0, "offset": handy_state["server_time_offset"]}), 200

@handy_api.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "fwVersion": "3.1.0-a28b8bb",
        "fwStatus": 0,
        "hwVersion": 1,
        "model": "H01",
        "branch": "master",
        "sessionId": "01FZZR1H25CWF77Q5T26YSJMBY"
    }), 200

@handy_api.route('/settings', methods=['GET'])
def get_settings():
    return jsonify({"slideMin": handy_state["slide_min"], "slideMax": handy_state["slide_max"]}), 200

@handy_api.route('/mode', methods=['PUT'])
def put_mode():
    data = request.get_json()
    handy_state["mode"] = data.get('mode', 0)
    return jsonify({"result": 0}), 200

@handy_api.route('/hssp/setup', methods=['PUT'])
def put_hssp_setup():
    data = request.get_json()
    handy_state["hssp_url"] = data.get('url', '')
    return jsonify({"result": 0}), 200

@handy_api.route('/hssp/play', methods=['PUT'])
def put_hssp_play():
    data = request.get_json()
    handy_state["startTime"] = data.get('startTime', 0)
    return jsonify({"result": 0}), 200

@handy_api.route('/hssp/stop', methods=['PUT'])
def put_hssp_stop():
    return jsonify({"result": 0}), 200

@handy_api.route('/servertime', methods=['GET'])
def get_servertime():
    return jsonify({"serverTime": int(time.time() * 1000) + handy_state["server_time_offset"]}), 200

# Register the Handy Blueprint
app.register_blueprint(handy_api)

if __name__ == '__main__':
    app.run(host='192.168.1.129', port=5000, debug=True)
