class AligmentTest:
    eps = 1e-3

    def __init__(self, drawer):
        self.drawer = drawer

    def process(self, time, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        ok = (abs(x1)<self.eps) and (abs(x2)<self.eps)
        self.draw(time, x1, x2, ok)
        return ok
            
    def draw(self,curTime,x1,x2, ok):
        self.drawer.reset()
        self.drawer.setState(ok)
        self.drawer.drawObject(0, False)
        self.drawer.drawObject(x1, True)
        self.drawer.drawObject(x2, True)
        self.drawer.drawText(str(curTime))
        self.drawer.show()
    
            
