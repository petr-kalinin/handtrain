class AligmentTest:
    eps = 1e-3
    requiredTime = 5000
    delay = 10

    def __init__(self, joystick1, joystick2, timer, drawer):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.timer = timer
        self.drawer = drawer

    def run(self):
        startTime = self.timer.currentTime()
        lastBadTime = 0
        while True:
            curTime = self.timer.currentTime() - startTime
            x1 = self.joystick1.x()
            x2 = self.joystick2.x()
            self.draw(curTime,x1,x2)
            if (abs(x1)>self.eps) or (abs(x2)>self.eps):
                lastBadTime = curTime
            if lastBadTime < curTime-self.requiredTime:
                break
            self.timer.sleep(self.delay)
        self.elapsedTime = curTime
            
    def draw(self,curTime,x1,x2):
        self.drawer.reset()
        self.drawer.drawObject(0, False)
        self.drawer.drawObject(x1, True)
        self.drawer.drawObject(x2, True)
        self.drawer.drawText(str(curTime))
        self.drawer.show()
    
            
