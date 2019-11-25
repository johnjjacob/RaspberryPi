trigger = False


def triggerOn():
    global trigger
    trigger = True
    
def triggerOff():
    global trigger 
    
    
triggerOn()
print(bool(trigger))