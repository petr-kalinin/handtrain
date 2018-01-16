from MovableObject import MovableObject


class AlignmentTraining:
    eps = 5e-2
    dt = 0.01

    def __init__(self, drawer, xa, ya, xb, yb):
        self.drawer = drawer
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.object1 = MovableObject(xa, ya, 0, 0, 1, 1)
        self.object2 = MovableObject(xb, yb, 0, 0, 1, 1)

    def process(self, time, pos):
        print("Positions: {} {}, {} {}".format(*pos[0], *pos[1]))
        self.object1.process(*pos[0], self.dt)
        self.object2.process(*pos[1], self.dt)
        delta1 = abs(self.object1.x - self.xb) + abs(self.object1.y - self.yb)
        delta2 = abs(self.object2.x - self.xa) + abs(self.object2.y - self.ya)
        ok1 = delta1<self.eps
        ok2 = delta2<self.eps
        self.draw(time, ok1, ok2)
        return (ok1 and ok2, delta1 + delta2)
            
    def draw(self, curTime, ok1, ok2):
        self.drawer.reset()
        self.drawer.drawObject(self.xa, self.ya, False)
        self.drawer.drawObject(self.xb, self.yb, False)
        self.drawer.setState(ok1)
        self.drawer.drawObject(self.object1.x, self.object1.y, True)
        self.drawer.setState(ok2)
        self.drawer.drawObject(self.object2.x, self.object2.y, True)
        self.drawer.drawText(str(curTime/1000))
        self.drawer.show()
    
    def name(self):
        return "AlignmentTraining"
