#!/usr/bin/python3
import time
import random

from RectangleTest import RectangleTest
from TestController import TestController
from FileWriter import FileWriter
from TestInterruptedError import TestInterruptedError
#from PygameDrawer import PygameDrawer

class DummyDrawer:
    s = ''
    def reset(self):
        self.s = ''
        
    def drawRectangle(self, width, height):
        self.s = self.s + " " + str(width) + " " + str(height)
        
    def drawText(self,s):
        self.s = self.s + " " + s
        
    def setState(self, ok):
        self.ok = ok
        if ok:
            raise TestInterruptedError()
    
        
    def show(self):
        print(self.s + str(self.ok) + '\r')
        
        

class DummyTimer:
    time = 100
    
    def currentTime(self):
        return self.time
        
    def sleep(self,x):
        self.time = self.time + x
        time.sleep(x/1000)
        
class JoystickImitator:
    _x = 0
    _x0 = 0
    _fac = 0
    _num = 0
    def __init__(self, x, x0, fac):
        self._x = x
        self._x0 = x0
        self._fac = fac
        
    def position(self):
        """Returns normalized (x,y)-coordinate in [-1,1]"""
        if self._num > 10:
            self._x = self._x0 + (self._x - self._x0) * self._fac + random.uniform(-1e-3, 1e-3)
        self._num += 1
        return (self._x, 0);

class ConsoleWriter:
    def write(self,a,b):
        print(str(a) + " " + str(b))

joy1 = JoystickImitator(-0.4, 0.2, 0.95)
joy2 = JoystickImitator(0.6, -0.4, 0.98)
test = RectangleTest(DummyDrawer())
writer = FileWriter("run2.txt~")
#test = RectangleTest(PygameDrawer())
controller = TestController(joy1, joy2, DummyTimer(), test, writer)
controller.requiredTime = 1000
controller.run()
print(controller.delta)