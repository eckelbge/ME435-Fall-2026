import motor
import mqtt_helper as mh
import signal
import time
from rosebot import Rosebot

class App:

    def __init__(self):
            self.robot = Rosebot()
    
            self.mqtt_client = mh.MqttClient()
            self.mqtt_client.connect(subscription_topic_name="me435/eckelbge/to_pi",
                                     publish_topic_name="me435/eckelbge/to_computer")
            self.mqtt_client.callback = self.mqtt_callback
    
    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type: ", message_type)
        print("Recieved payload: ", message_payload)

        if message_type == "left":
            print("Side: Left   Direction: ", message_payload[0], "  Time: ", message_payload[1], "  Speed: ", message_payload[2])
            if message_payload[0] == 1:
                direction = 1
            elif message_payload[0] == 0:
                direction = -1
            fast = direction*message_payload[2]
            self.robot.drive_system.set_speeds(fast,fast,0,0)
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "right":
            print("Side: Right   Direction: ", message_payload[0], "  Time: ", message_payload[1], "  Speed: ", message_payload[2])
            if message_payload[0] == 1:
                direction = 1
            elif message_payload[0] == 0:
                direction = -1
            fast = direction*message_payload[2]
            self.robot.drive_system.set_speeds(0,0,fast,fast)
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()

        if message_type == "both":
            print("Side: Both   Direction: ", message_payload[0], "  Time: ", message_payload[1], "  Speed Left: ", message_payload[2], "  Speed Right: ", message_payload[3])
            if message_payload[0] == 1:
                direction = 1
            elif message_payload[0] == 0:
                direction = -1
            fastL = direction*message_payload[2]
            fastR = direction*message_payload[3]
            self.robot.drive_system.set_speeds(fastL,fastL,fastR,fastR)
            time.sleep(message_payload[1])
            self.robot.drive_system.stop()
        

def main():
    print("Car MQTT")
    app = App()
    
    try:
        while True:
            app.mqtt_client.send_message("ultra",app.robot.ultrasonic.get_cm())
            print("Ultra: ", app.robot.ultrasonic.get_cm())
            time.sleep(2)
        #signal.pause() # Keep the program alive but does nothing.
    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop()
        app.mqtt_clinet.close()
    
main()