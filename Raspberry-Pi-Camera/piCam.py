import RPi.GPIO as GPIO 
from time import *
from picamera import PiCamera

print("Now running 'piCam.py'"); #To verify if the program is active

GPIO.setwarnings(False)

#Setup for LEDs and Button via GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Creates object for camera
camera = PiCamera()
camera.resolution = (1024, 786)

rerun = True;

#Upon call:
    """(1) Opens camera preview (2) Turns on red LED (3) After 3 seconds camera module captures and saves a picture"""
def take_picture():
    print("running take_picture") #To verify if the function is active
    
    GPIO.output(17, True)
    camera.start_preview
    # Camera warm-up time
    sleep(3)
    camera.capture('image1.jpg')
    GPIO.output(17, False)
    print("image succesfully saved to file")

while rerun:

    """Constantly checks if the button is pushed
        Take_picture() is called once the program detects that the button is pushed
        Green LED turns on for 2 seconds before turning back off to verify that the image was saved"""
    if (GPIO.input(26) == GPIO.HIGH):
        take_picture()
        GPIO.output(13, True)
        sleep(1)
        GPIO.output(13, False)

        print("do you want to re-run the program?")
        if(input() == 'no'):
            rerun = False;
        
