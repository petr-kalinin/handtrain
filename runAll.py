#!/usr/bin/python3
import time
import random

from TestSequence import TestSequence
from AligmentTest import AligmentTest
from RectangleTest import RectangleTest
from FileWriter import FileWriter

class DummyDrawer:
    s = ''
    s1 = ''
    width = 80
    def reset(self):
        self.s1 = ''
        self.s = ''
        
    def drawObject(self, x, active):
        if active:
            ch = '*'
        else:
            ch = '.'
        if self.s1 == '':
            self.s1 = ' ' * self.width
        pos = int(self.width * (1+x)/2)
        self.s1 = self.s1[:pos] + ch + self.s1[pos+1:]

    def drawRectangle(self, width, height):
        self.s = self.s + " " + str(width) + " " + str(height)
        
    def drawText(self,s):
        self.s = self.s + s
        
    def setState(self, ok):
        self.ok = ok
#        if ok:
#            raise TestInterruptedError
        
    def show(self):
        print(self.s + self.s1 + str(self.ok) + '\r')
     

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
    def __init__(self, x0, fac):
        self._x0 = x0
        self._fac = fac
        self.reset()
        
    def position(self):
        """Returns normalized (x,y)-coordinate in [-1,1]"""
        if self._num > 10:
            self._x = self._x0 + (self._x - self._x0) * self._fac + random.uniform(-1e-3, 1e-3)
        self._num += 1
        return (self._x, 0);
        
    def reset(self):
        self._x = random.uniform(-1, 1)

class ConsoleWriter:
    def write(self,a,b):
        print(str(a) + " " + str(b))

joy1 = JoystickImitator(0.2, 0.95)
joy2 = JoystickImitator(-0.4, 0.98)
sequence = TestSequence(joy1, joy2, DummyTimer())

atest = AligmentTest(DummyDrawer())
awriter = FileWriter("runAll_al.txt~")
sequence.append(atest, awriter)

rtest = RectangleTest(DummyDrawer())
rwriter = FileWriter("runAll_rec.txt~")
sequence.append(rtest, rwriter)

sequence.run()
print(sequence.resDelta)