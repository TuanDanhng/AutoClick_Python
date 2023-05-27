import time
import threading
from pynput.mouse import Button,Controller
from pynput.keyboard import Listener,KeyCode

buttonDirection = Button.right
delayTime = 1
startstopButton = KeyCode(char = 's')
terminateButton = KeyCode(char = 'x')

class ClickTheMouse(threading.Thread):
    def __init__(self,delayTime,buttonDirection):
        super(ClickTheMouse,self).__init__()
        self.delayTime = delayTime
        self.buttonDerection = buttonDirection
        self.running = False
        self.program_running = True

    def startMouseClick(self):
        self.running = True

    def stopMouseClick(self):
        self.running = False
    
    def exitScript(self):
        self.stopMouseClick()
        self.program_running = False    
    
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.buttonDerection)
                time.sleep(self.delayTime)
            time.sleep(0.1)
 
mouse = Controller()
clickThread = ClickTheMouse(delayTime, buttonDirection)
clickThread.start()

def on_press(key):
    if key == startstopButton:
        if clickThread.running:
            clickThread.stopMouseClick()
        else:
            clickThread.startMouseClick()
    elif key == terminateButton:
        clickThread.exitScript()
        Listener.stop()
        
with Listener(on_press = on_press) as listener:
    listener.join()