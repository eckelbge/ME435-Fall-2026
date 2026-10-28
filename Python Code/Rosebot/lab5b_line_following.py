from rosebot import Rosebot
import time

def main():
    print("Lab 5b Line Following")
    robot=Rosebot()


    try:
        while True:

            print(robot.ultrasonic.get_cm())
            print(robot.line_sensors.get_line_word())
            if robot.ultrasonic.get_cm() < 20:
                robot.drive_system.stop()
            else:
                if robot.line_sensors.get_line_word() == "WBW":
                    robot.drive_system.go(20,20)
                elif robot.line_sensors.get_line_word() == "BBW":
                    robot.drive_system.spin_in_place_for_degrees(10,20)
                elif robot.line_sensors.get_line_word() == "WBB":
                    robot.drive_system.spin_in_place_for_degrees_CW(10,-20)
                elif robot.line_sensors.get_line_word() == "BWW":
                    robot.drive_system.spin_in_place_for_degrees(10,20)
                elif robot.line_sensors.get_line_word() == "WWB":
                    robot.drive_system.spin_in_place_for_degrees_CW(10,-20)
                elif robot.line_sensors.get_line_word() == "WWW":
                    robot.drive_system.spin_in_place_for_degrees_CW(45,-20)
                    time.sleep(1)
                    robot.drive_system.spin_in_place_for_degrees(15,20)

            
            #Get ultrasonic sensor
            # if distance < 20 cm
            #   stop robot
            # else
            #   Get the line sensor readings
            #   Adjust wheel speeds based on YOUR strategy



            time.sleep(0.1)

    except KeyboardInterrupt:
        # Handle Ctrl-C to exit the program cleanly.
        robot.drive_system.stop()
        print("Goodbye!")


main()