Here's the API documentation for the provided Flask application. This documentation covers both the `/autoblow` and `/api/handy/v2` endpoints, detailing the routes, methods, expected request payloads, and response formats.

---

# API Documentation

## Base URLs
- Autoblow API: `http://127.0.0.1:5000/autoblow`
- Handy API: `http://127.0.0.1:5000/api/handy/v2`

## Autoblow API

### 1. `GET /autoblow/connected`
- **Description**: Returns the connection status.
- **Response**:
  ```json
  {
    "connected": true,
    "cluster": "192.168.1.129:5000"
  }
  ```

### 2. `PUT /autoblow/oscillate`
- **Description**: Controls oscillation settings.
- **Response**:
  ```json
  {
    "operationalMode": "OSCILLATOR_PLAYING",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 0,
    "oscillatorLowPoint": 5,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 0,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "",
    "syncScriptLoop": false
  }
  ```

### 3. `PUT /autoblow/sync-script/offset`
- **Description**: Sets the offset for the sync script.
- **Response**:
  ```json
  {
    "operationalMode": "SYNC_SCRIPT_PAUSED",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 7840,
    "syncScriptOffsetTime": 100,
    "syncScriptToken": "7a93bfc5-4043-4ade-aee5-bec8012b0e12",
    "syncScriptLoop": true
  }
  ```

### 4. `GET /autoblow/info`
- **Description**: Retrieves information about the device.
- **Response**:
  ```json
  {
    "firmwareStatus": "UP_TO_DATE",
    "firmwareVersion": 1.01,
    "firmwareBranch": "prod",
    "hardwareVersion": "ultra",
    "mac": "b0b21c3141e8"
  }
  ```

### 5. `GET /autoblow/state`
- **Description**: Returns the state of the device.
- **Response**:
  ```json
  {
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
    "syncScriptLoop": false
  }
  ```

### 6. `PUT /autoblow/sync-script/upload-csv-url`
- **Description**: Uploads the sync script using a CSV URL.
- **Response**:
  ```json
  {
    "operationalMode": "SYNC_SCRIPT_PAUSED",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 0,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "346d0210-3708-48c8-8e1c-55f3ed1960ec",
    "syncScriptLoop": false
  }
  ```

### 7. `PUT /autoblow/sync-script/start`
- **Description**: Starts the sync script.
- **Response**:
  ```json
  {
    "operationalMode": "SYNC_SCRIPT_PLAYING",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 15,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "7a93bfc5-4043-4ade-aee5-bec8012b0e12",
    "syncScriptLoop": false
  }
  ```

### 8. `PUT /autoblow/sync-script/stop`
- **Description**: Stops the sync script.
- **Response**:
  ```json
  {
    "operationalMode": "SYNC_SCRIPT_PAUSED",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 15,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "7a93bfc5-4043-4ade-aee5-bec8012b0e12",
    "syncScriptLoop": false
  }
  ```

### 9. `PUT /autoblow/sync-script/load-token`
- **Description**: Loads the sync script using a token.
- **Response**:
  ```json
  {
    "operationalMode": "SYNC_SCRIPT_PAUSED",
    "localScript": 0,
    "localScriptSpeed": 0,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 50,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 0,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "ea5d85d2-4db7-4f76-88fe-23a6fb5a8eab",
    "syncScriptLoop": false
  }
  ```

### 10. `PUT /autoblow/goto`
- **Description**: Controls the machine's position and speed.
- **Request**:
  ```json
  {
    "position": 50,
    "speed": 30
  }
  ```
- **Response**:
  ```json
  {
    "operationalMode": "GO_TO",
    "localScript": 0,
    "localScriptSpeed": 30,
    "motorTemperature": 30,
    "oscillatorTargetSpeed": 30,
    "oscillatorLowPoint": 0,
    "oscillatorHighPoint": 100,
    "syncScriptCurrentTime": 0,
    "syncScriptOffsetTime": 0,
    "syncScriptToken": "ea5d85d2-4db7-4f76-88fe-23a6fb5a8eab",
    "syncScriptLoop": false,
    "position": 50
  }
  ```

## Handy API

### 1. `GET /api/handy/v2/connected`
- **Description**: Returns the connection status of the Handy device.
- **Response**:
  ```json
  {
    "connected": true
  }
  ```

### 2. `PUT /api/handy/v2/slide`
- **Description**: Sets the slide position range.
- **Request**:
  ```json
  {
    "min": 0,
    "max": 100
  }
  ```
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 3. `PUT /api/handy/v2/hstp/offset`
- **Description**: Sets the HSTP offset.
- **Request**:
  ```json
  {
    "offset": 50
  }
  ```
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 4. `GET /api/handy/v2/hstp/offset`
- **Description**: Retrieves the HSTP offset.
- **Response**:
  ```json
  {
    "result": 0,
    "offset": 0
  }
  ```

### 5. `GET /api/handy/v2/info`
- **Description**: Retrieves information about the Handy device.
- **Response**:
  ```json
  {
    "fwVersion": "3.1.0-a28b8bb",
    "fwStatus": 0,
    "hwVersion": 1,
    "model": "H01",
    "branch": "master",
    "sessionId": "01FZZR1H25CWF77Q5T26YSJMBY"
  }
  ```

### 6. `GET /api/handy/v2/settings`
- **Description**: Retrieves the slide settings.
- **Response**:
  ```json
  {
    "slideMin": 0,
    "slideMax": 

100
  }
  ```

### 7. `PUT /api/handy/v2/mode`
- **Description**: Sets the operating mode of the device.
- **Request**:
  ```json
  {
    "mode": 1
  }
  ```
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 8. `PUT /api/handy/v2/hssp/setup`
- **Description**: Sets up the HSSP using a provided URL.
- **Request**:
  ```json
  {
    "url": "https://example.com"
  }
  ```
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 9. `PUT /api/handy/v2/hssp/play`
- **Description**: Starts the HSSP playback.
- **Request**:
  ```json
  {
    "startTime": 12345,
    "estimatedServerTime": 67890
  }
  ```
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 10. `PUT /api/handy/v2/hssp/stop`
- **Description**: Stops the HSSP playback.
- **Response**:
  ```json
  {
    "result": 0
  }
  ```

### 11. `GET /api/handy/v2/servertime`
- **Description**: Retrieves the server time.
- **Response**:
  ```json
  {
    "serverTime": 1700000000000
  }
  ```

---

This documentation covers the primary endpoints of both the Autoblow and Handy APIs, detailing the requests and responses for each route.
