import math

from MovableObject import MovableObject


class AlignmentTraining:
    eps = 5e-2
    dt = 0.002

    def __init__(self, drawer, line1, line2):
        self.drawer = drawer
        self.line1 = line1
        self.line2 = line2
        self.object1 = MovableObject(line1[0], line1[1], 0, 0, 1, 1)
        self.object2 = MovableObject(line2[0], line2[1], 0, 0, 1, 1)

    def process(self, time, pos):
        print("Positions: {} {}, {} {}".format(*pos[0], *pos[1]))
        delta1 = abs(self.object1.x - self.line1[2]) + abs(self.object1.y - self.line1[3])
        ok1 = delta1<self.eps
        if not ok1:
            self.object1.process(*pos[0], self.dt)
        delta2 = abs(self.object2.x - self.line2[2]) + abs(self.object2.y - self.line2[3])
        ok2 = delta2<self.eps
        if not ok2:
            self.object2.process(*pos[1], self.dt)
        delta1 = abs(self.object1.x - self.line1[2]) + abs(self.object1.y - self.line1[3])
        delta2 = abs(self.object2.x - self.line2[2]) + abs(self.object2.y - self.line2[3])
        ok1 = delta1<self.eps
        ok2 = delta2<self.eps
        self.draw(time, ok1, ok2)
        return (ok1 and ok2, delta1 + delta2)
            
    def draw(self, curTime, ok1, ok2):
        self.drawer.reset()
        self.drawObject(ok1, self.line1, self.object1)
        self.drawObject(ok2, self.line2, self.object2)
        self.drawer.drawText(str(curTime/1000))
        self.drawer.show()

    def drawObject(self, ok, line, object):
        angle = math.atan2(line[3] - object.y, -line[2] + object.x)
        self.drawer.drawObject(line[2], line[3], False)
        self.drawer.setState(ok)
        print("angle=", angle)
        self.drawer.drawObject(object.x, object.y, True, angle=angle)
        self.drawer.drawLine((object.x, object.y), (line[2], line[3]))

    def name(self):
        return "AlignmentTraining"
