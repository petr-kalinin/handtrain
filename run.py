#!/usr/bin/python3
import time
import random

from AligmentTest import AligmentTest
from TestController import TestController
from FileWriter import FileWriter
#from PygameDrawer import PygameDrawer

class DummyDrawer:
    s = ''
    width = 80
    def reset(self):
        self.s = ' ' * self.width
        
    def drawObject(self, x, active):
        if active:
            ch = '*'
        else:
            ch = '.'
        pos = int(self.width * (1+x)/2)
        self.s = self.s[:pos] + ch + self.s[pos+1:]
        
    def drawText(self,s):
        self.s = self.s + s
        
    def setState(self, ok):
        self.ok = ok
        
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
    _fac = 0
    def __init__(self, x, fac):
        self._x = x
        self._fac = fac
        
    def position(self):
        """Returns normalized (x,y)-coordinate in [-1,1]"""
        self._x = self._x * self._fac + random.uniform(-1e-3, 1e-3)
        return (self._x, 0);

class ConsoleWriter:
    def write(self,a,b):
        print(str(a) + " " + str(b))

joy1 = JoystickImitator(-0.4, 0.95)
joy2 = JoystickImitator(0.6, 0.98)
test = AligmentTest(DummyDrawer())
writer = FileWriter("run.txt~")
#test = AligmentTest(PygameDrawer())
controller = TestController(joy1, joy2, DummyTimer(), test, writer)
controller.requiredTime = 1000
controller.run()
print(controller.delta)