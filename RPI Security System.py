import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Buzzer
from gpiozero import LED
from tkinter import *
import PIL
from PIL import Image, ImageTk



import smtplib
import datetime
from picamera import PiCamera
camera = PiCamera()
camera.rotation = 180




from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 



MY_ADDRESS = 'jjjdev99@gmail.com'
PASSWORD = 'devpword'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
buzzer = Buzzer(13)
led = LED(18)
led.off()
trigger = False

caught = False
idx = 0  # loop index

def triggerOn():
    global trigger
    trigger = True
    print("trigger on")
    
    
def triggerOff():
    global trigger
    trigger = False
    print("trigger off")

def message():
    if trigger:
        print("Cerberus Online.")
    else:
        print("Cerberus Offline.")

def notification():
    email = 'johnjjacob78@gmail.com' # read contacts
    message = "Intruder Detected"

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template

        # Prints out the message body for our sake
    print("Notifying John")

        # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="ROOM ALERT"
        
        # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # open the file to be sent  
    filename = "Temp RPI Footage.jpg" 
    attachment = open("/home/pi/RPI Security System/Sending/Temp RPI Footage.jpg", "rb")

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
  
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
  
    # encode into base64 
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p)         # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
def Guard():
    j=0 #res
    
    i = 0 #reset PIR sensor
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders")
        led.off()              #Turn OFF LED
        sleep(0.5)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected")
        camera.capture('/home/pi/RPI Security System/Captured Images/RPI Footage%s.jpg'% j)
        camera.capture('/home/pi/RPI Security System/Sending/Temp RPI Footage.jpg')
        led.on()  #Turn ON LED
        notification()
        buzzer.on()
        sleep(1)
        buzzer.off()
        sleep(1)
          
                
        j = j+1
        sleep(10)


    



root = Tk()
root.title("Cerberus")
#root.geometry("250x100")

app = Frame(root)
app.grid()

statusMessage = StringVar()
statusMessage.set('STATUS: OFFLINE')

start = Button(app, text="ONLINE",fg="GREEN", command=lambda:[triggerOn(),message()])                                                           
stop = Button(app, text="OFFLINE",fg="RED", command=lambda:[triggerOff(),message()])
status = Label(root, textvariable = statusMessage)
logo = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/images.png"))
logoW = Label(root, image = logo)
#photoW.pack(side="bottom", fill="both", expand="yes")


start.grid()
stop.grid()
status.grid()
logoW.grid()

while True:
    if idx % 2 == 0:
        root.update()

    if trigger:
        statusMessage.set('STATUS: ONLINE')
        Guard()
        idx += 1
    else:
        statusMessage.set('STATUS: OFFLINE')

print("Done")
    
        







