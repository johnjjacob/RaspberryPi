import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Buzzer


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
GPIO.setup(3, GPIO.OUT)         #LED output pin
GPIO.setup(37,GPIO.OUT)

GPIO.output(37,0)
buzzer = Buzzer(13)




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
    j=0
    while True:
        i=GPIO.input(11)
        if i==0:                 #When output from motion sensor is LOW
            print ("No intruders")
            GPIO.output(3, 0)  #Turn OFF LED
            sleep(0.5)
        elif i==1:               #When output from motion sensor is HIGH
            print ("Intruder detected")
            camera.capture('/home/pi/RPI Security System/Captured Images/RPI Footage%s.jpg'% j)
            camera.capture('/home/pi/RPI Security System/Sending/Temp RPI Footage.jpg')
            GPIO.output(3, 1)  #Turn ON LED
            notification()
            buzzer.on()
            sleep(1)
            buzzer.off()
            sleep(1)
          
                
            j = j+1
            sleep(10)


    
Guard()

