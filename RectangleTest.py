class RectangleTest:
    eps = 1e-1
    needX1 = 0.5;
    needX2 = 0.5;

    def __init__(self, drawer):
        self.drawer = drawer

    def process(self, time, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        x1 = (1+x1)/2 # joystick returns in [-1,1], we need in [0,1]
        x2 = (1+x2)/2
        dx = abs(x1 - self.needX1)
        dy = abs(x2 - self.needX2)
        ok = (dx<self.eps) and (dy<self.eps)
        self.draw(time, x1, x2, ok)
        return (ok, dx + dy)

            
    def draw(self,curTime,x1,x2,ok):
        self.drawer.reset()
        self.drawer.setState(ok)
        self.drawer.drawRectangle(self.needX1, self.needX2, False)
        self.drawer.drawRectangle(x1, x2, True)
        self.drawer.drawText(str(curTime))
        self.drawer.show()
    
    def name(self):
        return "Rectangle"
            
