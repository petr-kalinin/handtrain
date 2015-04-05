import time

from JoystickImitator import JoystickImitator
from AligmentTest import AligmentTest

class DummyDrawer:
    s = ''
    width = 80
    def reset(self):
        self.s = ' ' * self.width
        
    def drawObject(self,x, active):
        if active:
            ch = '*'
        else:
            ch = '.'
        pos = int(self.width * (1+x)/2)
        self.s = self.s[:pos] + ch + self.s[pos+1:]
        
    def drawText(self,s):
        self.s = self.s + s
        
    def show(self):
        print(self.s + '\r')
        

class DummyTimer:
    time = 100
    
    def currentTime(self):
        return self.time
        
    def sleep(self,x):
        self.time = self.time + x
        time.sleep(x/1000)

joy1 = JoystickImitator(-0.4, 0.95)
joy2 = JoystickImitator(0.6, 0.98)
test = AligmentTest(joy1, joy2, DummyTimer(), DummyDrawer())
test.requiredTime = 1000
test.run()