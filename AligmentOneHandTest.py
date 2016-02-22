import unittest
#from mock import MagicMock

class AligmentOneHandTest:
    eps = 1e-1
    needX1 = 0.5;
    needX2 = -0.5;

    def __init__(self, drawer):
        self.drawer = drawer

    def process(self, time, pos):
        x1, y1 = pos[0]
        delta1 = abs(x1 - self.needX1)
        ok = (delta1<self.eps)
        self.draw(time, x1 - self.needX1, ok)
        return (ok, delta1)
            
    def draw(self, curTime, x1, ok):
        self.drawer.reset()
        self.drawer.setState(ok)
        self.drawer.drawObject(0.5, False)
        self.drawer.drawObject((1+x1)/2, True)
        self.drawer.drawText(str(curTime/1000))
        self.drawer.show()
    
    def name(self):
        return "AlignmentOneHand"
