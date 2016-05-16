import RPi.GPIO as GPIO
import time, sys


class beer():

    def __init__(self):
        self.count = 0
        self.liters = 0
    def countPulse(self,channel):
        self.count = self.count+1
        self.liters = float(float(self.count)/450)
        print self.count
        print self.liters


if __name__ == "__main__":
    new_beer=beer()
    FLOW_SENSOR = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=new_beer.countPulse)

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
