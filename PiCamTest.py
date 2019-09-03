from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.rotation = 180

camera.start_preview()
sleep(5)

camera.capture('/home/pi/RPI Security System/Captured Images/test1.jpg')
camera.stop_preview()
