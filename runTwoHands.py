#!/usr/bin/python3
import time
import random

from TestSequence import TestSequence
from AligmentTest import AligmentTest
from RectangleTest import RectangleTest
from FileWriterProvider import FileWriterProvider
from Patient import Patient
from TkPatient import TkPatient

from PygameDrawer import PygameDrawer
from PygameJoystick import PygameJoystick
from PygameTimer import PygameTimer

from TkRequiredTime import tkRequiredTime

from JoystickImitator import JoystickImitator

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

class ConsoleWriter:
    def write(self,a,b):
        print(str(a) + " " + str(b))

patient = TkPatient()
#patient = Patient()
        
reqTime = tkRequiredTime()

#drawer = DummyDrawer()
#drawer = PygameDrawer("hedgehog.png")
drawer = PygameDrawer("circle-200x20px.png", (255,255,255))
#drawer = PygameDrawer("circle-200x20px.png", (0,0,0))

#joy1 = JoystickImitator(0.5, 0.95)
#joy2 = JoystickImitator(-0.5, 0.98)
joy1 = PygameJoystick(0, drawer)
joy2 = PygameJoystick(1, drawer)


#timer = DummyTimer()
timer = PygameTimer()

sequence = TestSequence([joy1, joy2], timer, FileWriterProvider(patient.name), reqTime)

atest = AligmentTest(drawer)
sequence.append(atest)

#rtest = RectangleTest(drawer)
#sequence.append(rtest)

sequence.run()
print(sequence.resDelta)