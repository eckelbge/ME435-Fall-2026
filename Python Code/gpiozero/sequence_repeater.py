import gpiozero as gz
import time
import signal

n=0
seq=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# TODO Code seems to work, but I need to find a way to save code in-between function runs so it can properly index

def some_helper_function(led_board, brightnessR, brightnessY, brightnessG,n,seq):
    print("Some helper function")
    print("Matrix =", seq)
    print("Index =", n)
    led_board.value = (brightnessR, brightnessY, brightnessG)
    matrix_maker(brightnessR, brightnessY, brightnessG,n,seq)
    time.sleep(1)
    led_board.off()
    time.sleep(1)

def matrix_maker(brightnessR, brightnessY, brightnessG,n,seq):
    seq[n][0]=brightnessR
    print("Matrix =", seq)
    seq[n][1]=brightnessY
    print("Matrix =", seq)
    seq[n][2]=brightnessG
    n=n+1
    print("Matrix =", seq)

def sequence_function(led_board,seq):
    print("Simon doesn't say")
    led_board.value = (1,0,1)
    time.sleep(0.5)
    led_board.off()
    time.sleep(0.1)


def button_events():
    print("Button Events")
    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)
    seqeuncebutton = gz.Button(25)
    led_board=gz.LEDBoard(14,15,18,pwm=True)

    button_red.when_pressed = lambda: some_helper_function(led_board,1,0,0,n,seq)
    button_yellow.when_pressed = lambda: some_helper_function(led_board,0,1,0,n,seq)
    button_green.when_pressed = lambda: some_helper_function(led_board,0,0,1,n,seq)
    seqeuncebutton.when_pressed = lambda: sequence_function(led_board,seq)
    signal.pause()

def main():
    print("Pushbuttons")
    button_events()

main()