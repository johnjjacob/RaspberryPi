from gpiozero import LED, Button, Buzzer
from time import sleep


buzzer = Buzzer(13)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
    