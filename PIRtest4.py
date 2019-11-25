from gpiozero import MotionSensor



pir = MotionSensor(17)

while True:
    i = pir.motion_detected()
    if i:
        print("Detected")
    else:
        print("nothing")
    

