class RectangleTest:
    eps = 1e-3
    needX1 = 0.6;
    needX2 = 0.3;
    interrupted = False

    def __init__(self, drawer):
        self.drawer = drawer

    def process(self, time, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        x1 = (1+x1)/2 # joystick returns in [-1,1], we need in [0,1]
        x2 = (1+x2)/2
        ok = (abs(x1 - self.needX1)<self.eps) and (abs(x2 - self.needX2)<self.eps)
        self.draw(time, x1, x2, ok)
        if self.drawer.interrupted:
            self.interrupted = True
        return ok
            
    def draw(self,curTime,x1,x2, ok):
        self.drawer.reset()
        self.drawer.setState(ok)
        self.drawer.drawRectangle(x1, x2)
        self.drawer.drawText(str(curTime))
        self.drawer.show()
    
            
