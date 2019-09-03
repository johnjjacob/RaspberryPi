from gpiozero import LED
import time

led = LED(3)

while True:
    led.toggle()
    time.sleep(0.5)
    led.toggle()
    time.sleep(0.5)
    
    
    
