import servo
import time

class RoseServo:
    def __init__(self):
        self.servo = servo.Servo()

    def turn_servo(self, num, angle):
        servnum = str(num)
        self.servo.set_servo_pwm(servnum, angle)
