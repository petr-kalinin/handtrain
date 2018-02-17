import math

from RotateableObject import RotateableObject


class CupTraining:
    eps = 5e-2
    dt = 0.02

    def __init__(self, drawer, pos1, pos2, neededAngle):
        self.drawer = drawer
        self.pos1 = pos1
        self.pos2 = pos2
        self.neededAngle = neededAngle
        self.object1 = RotateableObject(0, 0, math.pi)
        self.object2 = RotateableObject(0, 0, math.pi)

    def process(self, time, pos):
        print("Positions: {} {}, {} {}".format(*pos[0], *pos[1]))
        delta1 = abs(self.object1.angle - self.neededAngle)
        ok1 = delta1<self.eps
        #if not ok1:
        self.object1.process(pos[0][0], self.dt)
        delta2 = abs(self.object2.angle - self.neededAngle)
        ok2 = delta2<self.eps
        #if not ok2:
        self.object2.process(pos[1][0], self.dt)
        delta1 = abs(self.object1.angle - self.neededAngle)
        delta2 = abs(self.object2.angle - self.neededAngle)
        ok1 = delta1<self.eps
        ok2 = delta2<self.eps
        self.draw(time, ok1, ok2)
        return (ok1 and ok2, delta1 + delta2)
            
    def draw(self, curTime, ok1, ok2):
        self.drawer.reset()
        self.drawObject(ok1, self.pos1, self.object1, False)
        self.drawObject(ok2, self.pos2, self.object2, True)
        self.drawer.drawText(str(curTime/1000))
        self.drawer.show()

    def drawObject(self, ok, pos, object, mirror):
        self.drawer.setState(ok)
        self.drawer.drawObject(*pos, True, angle=object.angle, mirror=mirror)

    def name(self):
        return "CupTraining"
