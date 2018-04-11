#!/usr/bin/python3
# coding: utf8
import time
import random
import math

from TestSequence import TestSequence
from AlignmentTraining import AlignmentTraining
from CupTraining import CupTraining

from PygameDrawer import PygameDrawer
from PygameJoystick import PygameJoystick
from PygameTimer import PygameTimer

from JoystickImitator import JoystickImitator

def getTimePoints(time, delta):
    MIN_TIME = 20 * 1000
    SIGMA = 20 * 1000
    if delta < 0:  # did not finish
        return -1e20
    if time < MIN_TIME:
        return 1
    return math.exp(-((time - MIN_TIME) ** 2) / SIGMA ** 2)

reqTime = 1000

# drawer = DummyDrawer()
drawer = PygameDrawer("car_150px.png", bgColor=(255, 255, 255), activeColor=(128, 128, 128), okColor=(0, 255, 0))
cup_drawer = PygameDrawer("cup_500px.png", bgColor=(255, 255, 255), activeColor=(128, 128, 128), okColor=(0, 255, 0))
letter_drawer = PygameDrawer("letter_150px.png", bgColor=(255, 255, 255), activeColor=(128, 128, 128), okColor=(0, 255, 0))

#joy1 = JoystickImitator(0, 0.95, 0, 0.95)
#joy2 = JoystickImitator(0, 0.95, 0, 0.95)
joy1 = PygameJoystick(0, drawer)
joy2 = PygameJoystick(1, drawer)

# timer = DummyTimer()
timer = PygameTimer()

sequence = TestSequence([joy1, joy2], timer, None, reqTime)

"""
sequence.append(AlignmentTraining(drawer,
                                  (0.1, 0.45, 0.9, 0.45),
                                  (0.9, 0.55, 0.1, 0.55)))
sequence.append(AlignmentTraining(drawer,
                                  (0.45, 0.1, 0.45, 0.9),
                                  (0.55, 0.9, 0.55, 0.1)))
sequence.append(AlignmentTraining(drawer,
                                  (0.15, 0.05, 0.95, 0.85),
                                  (0.85, 0.95, 0.05, 0.15)))
sequence.append(AlignmentTraining(drawer,
                                  (0.95, 0.15, 0.15, 0.95),
                                  (0.05, 0.85, 0.85, 0.05)))
"""
sequence.append(CupTraining(cup_drawer,
                            (0.7, 0.5),
                            (0.3, 0.5),
                            math.pi/4))
sequence.append(AlignmentTraining(letter_drawer,
                                  (0.95, 0.15, 0.15, 0.95),
                                  (0.05, 0.85, 0.85, 0.05)))

sequence.run()

print(sequence.resDelta)

points = 0
for res in sequence.resDelta:
    points += getTimePoints(*res)
points *= 100.0 / len(sequence.resDelta)
if points > -1:
    while True:
        letter_drawer.drawCenterText("Баллы: {:0.0f}".format(points))
        letter_drawer.show()
        timer.sleep(10)