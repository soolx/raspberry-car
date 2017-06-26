import RPi.GPIO as GPIO
import time

def gpioinit():
    GPIO.setmode(GPIO.BOARD)

    # 定义GPIO接口编号
    # LEFT
    INT1 = 11
    INT2 = 12
    #RIGHT
    INT3 = 13
    INT4 = 15

    GPIO.setup(INT1, GPIO.OUT)
    GPIO.setup(INT2, GPIO.OUT)
    GPIO.setup(INT3, GPIO.OUT)
    GPIO.setup(INT4, GPIO.OUT)


def next():
    GPIO.output(INT1, GPIO.HIGH)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, GPIO.HIGH)
    GPIO.output(INT4, GPIO.LOW)

def left():
    GPIO.output(INT1, False)
    GPIO.output(INT2, False)
    GPIO.output(INT3, GPIO.HIGH)
    GPIO.output(INT4, GPIO.LOW)

def right():
    GPIO.output(INT1, GPIO.HIGH)
    GPIO.output(INT2, GPIO.LOW)
    GPIO.output(INT3, False)
    GPIO.output(INT4, False)

def reverse():
    GPIO.output(INT1, GPIO.LOW)
    GPIO.output(INT2, GPIO.HIGH)
    GPIO.output(INT3, GPIO.LOW)
    GPIO.output(INT4, GPIO.HIGH)

def stop():
    GPIO.cleanup()