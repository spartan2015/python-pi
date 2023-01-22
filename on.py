import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)

try:
    while True:
        GPIO.output(in1, True)
        time.sleep(1)
        GPIO.output(in1, False)
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
