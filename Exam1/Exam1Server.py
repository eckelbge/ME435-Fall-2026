import flask
import led
import threading


app = flask.Flask(__name__, static_url_path="",static_folder="publicE1")

serial_lock = threading.Lock()
led = led.LED() # TODO: Set port if needed. "/dev/ttyUSB0"

@app.route("/")
def handle_naked_domain():
    return flask.redirect("/htmlmenu.html")

@app.get("/api/<command>")
def handle_led_commands(command):
    with serial_lock:
        response = led.send_command(command)
    return response


if __name__ =="__main__":
    print("Running flask!")
    led.connect()
    try:
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False) # , use_reloader=False
    finally:
        print("Disconnecting from LED")
        led.disconnect()