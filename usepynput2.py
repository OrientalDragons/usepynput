from pynput import keyboard
import time

class myButton:
    ctrlPress = False
    ctrlRelease=True
    Controller=keyboard.Controller()
    Key=keyboard.Key
    def __init__(self):
        pass


    def on_press(self,key):
        print(str(key))
        if str(key)=='Key.ctrl':
            self.ctrlPress = True
            self.ctrlRelease=False
        if self.startDo(key)==True:
            self.doingSth(key)

    def startDo(self,key):
        
        # ctrl+0 
        if  self.ctrlPress==True and str(key)=="'0'":
            return True

    def endDo(self,key):
        # ctrl+0 
        if   str(key)=="Key.end":
            return True
        else:
            return False

    def doingSth(self,key):
        i=10
        while  i>0:
            i=i-1

            # copy
            self.Controller.press(self.Key.ctrl)
            self.Controller.press('c')
            self.Controller.release('c')
            time.sleep(0.5)
            self.Controller.release(self.Key.ctrl)
            time.sleep(0.5)
            
            # tab
            self.Controller.press(self.Key.alt)
            self.Controller.press(self.Key.tab)
            self.Controller.release(self.Key.tab)
            time.sleep(0.5)
            self.Controller.release(self.Key.alt)
            time.sleep(0.5)

            self.Controller.press(self.Key.ctrl)
            self.Controller.press('v')
            self.Controller.release('v')
            time.sleep(0.5)
            self.Controller.release(self.Key.ctrl)
            time.sleep(0.5)

            # tab
            self.Controller.press(self.Key.alt)
            self.Controller.press(self.Key.tab)
            self.Controller.release(self.Key.tab)
            time.sleep(0.5)
            self.Controller.release(self.Key.alt)
            time.sleep(0.5)

            # self.Controller.press('a')
            # self.Controller.release('a')
            time.sleep(0.5)

            print("this is a try")


    def on_release(self,key):
        print("release"+str(key))
        if str(key)=='Key.ctrl':
            self.ctrlPress =False
            self.ctrlRelease= True
        if key == keyboard.Key.esc:
            return False

if __name__ == "__main__":
    myB=myButton()
    while True:
        with keyboard.Listener(
        on_press = myB.on_press,
        on_release = myB.on_release,
        suppress = False) as listener:
            listener.join()
    pass