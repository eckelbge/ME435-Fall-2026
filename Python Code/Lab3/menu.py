import plateloader

def main():
    print("Serial Menu")
    #loader = plateloader.PlateLoader("/dev/ttyUSB0")
    loader = plateloader.PlateLoader()
    loader.connect()
    print("0. Exit") #Seems to work
    print("1. RESET") #Seems to work
    print("2. X-AXIS") #Seems to work
    print("3. GRIPPER") #Seems to work
    print("4. Z-AXIS") #Seems to work
    print("5. MOVE") #Seems to work
    print("6. Status") #Seems to work since I don't think Arduino has this coded on it
    while True:
        selection = int(input("Selection: "))
        if selection == 0:
            break
        elif selection == 1:
            response = loader.send_command("RESET")
            print(response)
        elif selection == 2:
            xselect = str(input("X Position: "))
            response = loader.send_command("X-AXIS "+ xselect)
            print(response)
        elif selection == 3:
            print("1 for OPEN")
            print("0 for CLOSE")
            gripselection = int(input("Selection: "))
            if gripselection == 1:
                response = loader.send_command("GRIPPER OPEN")
                print(response)
            elif gripselection == 0:
                response = loader.send_command("GRIPPER CLOSE")
                print(response)
        elif selection == 4:
            print("1 for EXTEND")
            print("0 for RETRACT")
            zselection = int(input("Selection: "))
            if zselection == 1:
                response = loader.send_command("Z-AXIS EXTEND")
                print(response)
            elif zselection == 0:
                response = loader.send_command("Z-AXIS RETRACT")
                print(response)
        elif selection == 5:
            frselect = str(input("Start Position: "))
            toselect = str(input("End Position: "))
            response = loader.send_command("MOVE "+ frselect +", "+ toselect)
        elif selection == 6:
            response = loader.send_command("LOADER_STATUS")
            print(response)


    loader.disconnect()
    print("Goodbye")





main()
