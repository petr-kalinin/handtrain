import time

from JoystickImitator import JoystickImitator
from AligmentTest import AligmentTest

class DummyDrawer:
    def reset(self):
        print('')
        
    def drawObject(self,x):
        print('object at %0.5f ' % x, end='')
        
    def drawText(self,s):
        print(s, end='')
        
    def show(self):
        pass
        

class DummyTimer:
    time = 100
    
    def currentTime(self):
        return self.time
        
    def sleep(self,x):
        self.time = self.time + x
        time.sleep(x/1000)

joy1 = JoystickImitator(-0.4, 0.9)
joy2 = JoystickImitator(0.6, 0.95)
test = AligmentTest(joy1, joy2, DummyTimer(), DummyDrawer())
test.run()