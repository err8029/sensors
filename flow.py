import RPi.GPIO as GPIO
import time, sys
import MFRC522 
import signal


class beer():

    def __init__(self):
        self.count = 0
        self.liters = 0
        self.t = 0
        self.continue_reading= True
    def countPulse(self):
        self.count = self.count+1
        self.liters = float(float(self.count)/450)
        print self.count
        print self.liters

    def end_read(self):
        print "Ctrl+C captured, ending read."
        self.continue_reading = False
        GPIO.cleanup()

    def nfc_read(self):
        signal.signal(signal.SIGINT, end_read)
        MIFAREReader = MFRC522.MFRC522()
        print "Welcome to the MFRC522 data read example"
        print "Press Ctrl-C to stop."
        while continue_reading:
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            if status == MIFAREReader.MI_OK:
                print "Card detected"
                (status,uid) = MIFAREReader.MFRC522_Anticoll()
                if status == MIFAREReader.MI_OK:
                    print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

    def mainpart(self,channel):
        tans=1000
        while True:
            try:
                dt=self.t-tans
                if(dt<500):
                    countPulse()
                else:
                    nfc_read()
                tans=t
                time.sleep(1)
                self.t = time.time()
            except KeyboardInterrupt:
                print '\ncaught keyboard interrupt!, bye'
                GPIO.cleanup()
                sys.exit()




if __name__ == "__main__":
    new_beer=beer()
    FLOW_SENSOR = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=new_beer.mainpart)
