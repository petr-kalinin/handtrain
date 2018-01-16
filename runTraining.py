#!/usr/bin/python3
import time
import random

from TestSequence import TestSequence
from AlignmentTraining import AlignmentTraining

from PygameDrawer import PygameDrawer
from PygameJoystick import PygameJoystick
from PygameTimer import PygameTimer

from JoystickImitator import JoystickImitator

reqTime = 3000

# drawer = DummyDrawer()
drawer = PygameDrawer("hedgehog_140px.png", activeColor=(128, 128, 128), okColor=(0, 255, 0))

#joy1 = JoystickImitator(0, 0.95, 0, 0.95)
#joy2 = JoystickImitator(0, 0.95, 0, 0.95)
joy1 = PygameJoystick(0, drawer)
joy2 = PygameJoystick(1, drawer)

# timer = DummyTimer()
timer = PygameTimer()

sequence = TestSequence([joy1, joy2], timer, None, reqTime)

sequence.append(AlignmentTraining(drawer, 0.1, 0.5, 0.9, 0.5))
sequence.append(AlignmentTraining(drawer, 0.5, 0.1, 0.5, 0.9))
sequence.append(AlignmentTraining(drawer, 0.1, 0.1, 0.9, 0.9))


sequence.run()
print(sequence.resDelta)

