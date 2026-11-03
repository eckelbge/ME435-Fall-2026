import gpiozero as gz
import mqtt_helper as mh
import signal
import time
import motor
from rosebot import Rosebot

class App:

    def __init__(self):
        self.car = motor.OrdinaryCar()
        robot = Rosebot()

        self.mqtt_client = mh.MqttClient()
        self.mqtt_client.connect(subscription_topic_name="me435/eckelbge/to_pi",
                                 publish_topic_name="me435/eckelbge/to_computer")
        self.mqtt_client.callback = self.mqtt_callback

    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type: ", message_type)
        print("Recieved payload: ", message_payload)

        if message_type == "left":
            if message_payload[0] == 1:
                direction = 1
            elif message_payload[0] == 0:
                direction = -1
            Rosebot.drive_system.go(direction*message_payload[3], 0)
            time.sleep(message_payload[2])
            Rosebot.drive_system.stop()


def main():
    print("Exam 3")
    app = App()

    signal.pause() # Keep the program alive but does nothing.

main()