import time

import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

A = 7
B = 11
C = 13
D = 15

gpio.setup(A, gpio.OUT)
gpio.setup(B, gpio.OUT)
gpio.setup(C, gpio.OUT)
gpio.setup(D, gpio.OUT)


def gpio_setup(a, b, c, d):
    gpio.output(A, a)
    gpio.output(B, b)
    gpio.output(C, c)
    gpio.output(D, d)
    time.sleep(0.001)


def power_pins(dir="left"):
    if dir is "left":
        gpio_setup(1, 0, 0, 0)
        gpio_setup(1, 1, 0, 0)
        gpio_setup(0, 1, 0, 0)
        gpio_setup(0, 1, 1, 0)
        gpio_setup(0, 0, 1, 0)
        gpio_setup(0, 0, 1, 1)
        gpio_setup(0, 0, 0, 1)
        gpio_setup(1, 0, 0, 1)
        gpio_setup(0, 0, 0, 0)
    elif dir is "right":
        gpio_setup(1, 0, 0, 1)
        gpio_setup(0, 0, 0, 1)
        gpio_setup(0, 0, 1, 1)
        gpio_setup(0, 0, 1, 0)
        gpio_setup(0, 1, 1, 0)
        gpio_setup(0, 1, 0, 0)
        gpio_setup(1, 1, 0, 0)
        gpio_setup(1, 0, 0, 0)
        gpio_setup(0, 0, 0, 0)


def turn(dir):
    full_circle = 510
    degree = full_circle / 360 * 32
    while degree > 0.0:
        power_pins(dir)
        degree -= 1
