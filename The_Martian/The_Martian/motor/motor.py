import time

import The_Martian.RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 7
B = 11
C = 13
D = 15

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)


def GPIO_SETUP(a, b, c, d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.001)


def POWER_PINS(dir="LEFT"):
    if dir is "LEFT":
        GPIO_SETUP(1, 0, 0, 0)
        GPIO_SETUP(1, 1, 0, 0)
        GPIO_SETUP(0, 1, 0, 0)
        GPIO_SETUP(0, 1, 1, 0)
        GPIO_SETUP(0, 0, 1, 0)
        GPIO_SETUP(0, 0, 1, 1)
        GPIO_SETUP(0, 0, 0, 1)
        GPIO_SETUP(1, 0, 0, 1)
    elif dir is "RIGHT":
        GPIO_SETUP(1, 0, 0, 1)
        GPIO_SETUP(0, 0, 0, 1)
        GPIO_SETUP(0, 0, 1, 1)
        GPIO_SETUP(0, 0, 1, 0)
        GPIO_SETUP(0, 1, 1, 0)
        GPIO_SETUP(0, 1, 0, 0)
        GPIO_SETUP(1, 1, 0, 0)
        GPIO_SETUP(1, 0, 0, 0)


def TURN(dir):
    full_circle = 510
    degree = full_circle / 360 * 32
    GPIO_SETUP(0, 0, 0, 0)

    while degree > 0.0:
        POWER_PINS(dir)
        degree -= 1


def MAKE_CLEAN(left_turns, right_turns):
    time.sleep(3)

    for i in range(0, left_turns):
        print("Reset left")
        TURN("RIGHT")
    for i in range(0, right_turns):
        print("Reset right")
        TURN("LEFT")


turned_left = 0
turned_right = 0

for i in range(0, 16):
    TURN("LEFT")
    print("Left turn")
    turned_left += 1
    time.sleep(0.1)

time.sleep(5)

for i in range(0, 5):
    TURN("RIGHT")
    print("Right turn")
    turned_right += 1
    time.sleep(0.1)

MAKE_CLEAN(turned_left, turned_right)

GPIO_SETUP(0, 0, 0, 0)
