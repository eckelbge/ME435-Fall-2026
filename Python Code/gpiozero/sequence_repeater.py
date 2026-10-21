import gpiozero as gz
import time
import signal

n=0
global seq
seq=[[0,0,0]]

# TODO Code seems to work, but I need to find a way to save code in-between function runs so it can properly index

def some_helper_function(led_board, brightnessR, brightnessY, brightnessG):
    print("Some helper function")
    print("Matrix =", seq)
    print("Index =", n)
    led_board.value = (brightnessR, brightnessY, brightnessG)
    matrix_maker(brightnessR, brightnessY, brightnessG)
    time.sleep(1)
    led_board.off()
    time.sleep(0.1)

def matrix_maker(brightnessR, brightnessY, brightnessG):
    global n
    global seq
    seq[n][0]=brightnessR
    seq[n][1]=brightnessY
    seq[n][2]=brightnessG
    n +=1
    seq.append([0,0,0])
    print("Matrix =", seq)
    print("Index =", n)

def sequence_function(led_board,seq,n):
    print("Simon doesn't say")
    for k in range(n):
        led_board.value = (seq[k][0],seq[k][1],seq[k][2])
        time.sleep(0.5)
        led_board.off()
        time.sleep(0.1)
    reset_sequence()

def reset_sequence():
    global n
    n=0
    global seq
    seq=[[0,0,0]]
    print("Matrix =", seq)
    print("Index =", n)

def button_events():
    print("Button Events")
    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)
    seqeuncebutton = gz.Button(25)
    led_board=gz.LEDBoard(14,15,18,pwm=True)

    button_red.when_pressed = lambda: some_helper_function(led_board,1,0,0)
    button_yellow.when_pressed = lambda: some_helper_function(led_board,0,1,0)
    button_green.when_pressed = lambda: some_helper_function(led_board,0,0,1)
    seqeuncebutton.when_pressed = lambda: sequence_function(led_board,seq,n)
    signal.pause()

def main():
    print("Pushbuttons")
    button_events()

main()