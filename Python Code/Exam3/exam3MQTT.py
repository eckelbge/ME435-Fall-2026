import motor
import mqtt_helper as mh
import signal
import time
from rosebot import Rosebot

class App:

    def __init__(self):
            self.robot = Rosebot()
    
            self.mqtt_client = mh.MqttClient()
            self.mqtt_client.connect(subscription_topic_name="me435/eckelbge/#",
                                     publish_topic_name="me435/eckelbge/")
            self.mqtt_client.callback = self.mqtt_callback
    
    def mqtt_callback(self, message_type, message_payload):
        print("Recieved type: ", message_type)
        print("Recieved payload: ", message_payload)

        if message_type == "left":
            if message_payload[0] == 1:
                direction = 1
            elif message_payload[0] == 0:
                direction = -1
        fast = direction*message_payload[2]
        self.robot.drive_system.set_speeds(fast,fast,0,0)
        time.sleep(message_payload[1])
        self.robot.drive_system.stop()
        

def main():
    print("Car MQTT")
    app = App()
    
    try:
        #while True:
                # Send test messages!
                #app.mqtt_client.send_message("set_speeds", [40, 40, 40, 40])
                #time.sleep(1)
                #app.mqtt_client.send_message("stop")
                #time.sleep(1)
    
        signal.pause() # Keep the program alive but does nothing.
    except KeyboardInterrupt:
        print("Goodbye")
        app.robot.drive_system.stop()
        app.mqtt_clinet.close()
    
main()