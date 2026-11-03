import motor
import mqtt_helper as mh
import signal
import time
from rosebot import Rosebot

def __init__(self):
    self.car = motor.OrdinaryCar()
    

def mqtt_callback(self, message_type, message_payload):
    print("Recieved type: ", message_type)
    print("Recieved payload: ", message_payload)

    if message_type == "left":
        if message_payload[0] == 1:
            direction = 1
        elif message_payload[0] == 0:
            direction = -1
    fast = direction*message_payload[2]
        
    self.go((fast),0)
    time.pause(message_payload[1])
    self.stop

def scale_speed(self, speed):
        """Returns an int futy of 0 to 4095 (or 0 to -4095 based on the given speed)"""
        return int(speed / 100 *4095)

def set_speeds(self,left_front, left_rear, right_front, right_rear):
    """ Pass in 4 speeds each -100 to 100 to set the wheel duty cycles. """
    self.car.set_motor_model(self.scale_speed(left_front), 
                            self.scale_speed(left_rear), 
                            self.scale_speed(right_front), 
                            self.scale_speed(right_rear))

def go(self, left_wheel_speed, right_wheel_speed):
    """ Speeds as integers from -100 to 100. """
    self.set_speeds(left_wheel_speed, left_wheel_speed, 
                    right_wheel_speed, right_wheel_speed)

def stop(self):
    self.set_speeds(0, 0, 0, 0)
        

def main():
    print("Exam 3")
    
    mqtt_client = mh.MqttClient()
    mqtt_client.connect(subscription_topic_name="me435/eckelbge/to_pi",
                        publish_topic_name="me435/eckelbge/to_computer")
    mqtt_client.callback = mqtt_callback

    signal.pause() # Keep the program alive but does nothing.

main()