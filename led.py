import RPi.GPIO as GPIO
import time

pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

for i in range(1, 10):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    
GPIO.cleanup()
