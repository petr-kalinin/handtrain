class TestController:
    requiredTime = 5000
    delay = 10

    def __init__(self, joystick1, joystick2, timer, test):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.timer = timer
        self.test = test

    def run(self):
        startTime = self.timer.currentTime()
        lastBadTime = 0
        while True:
            curTime = self.timer.currentTime() - startTime
            pos1 = self.joystick1.position()
            pos2 = self.joystick2.position()
            ok = self.test.process(curTime, pos1, pos2)
            if not ok:
                lastBadTime = curTime
            if lastBadTime < curTime-self.requiredTime:
                break
            if self.test.interrupted:
                break
            self.timer.sleep(self.delay)
        self.elapsedTime = curTime
            