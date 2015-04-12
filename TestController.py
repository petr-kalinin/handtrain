from TestInterruptedError import TestInterruptedError

class TestController:
    requiredTime = 15000
    delay = 10

    def __init__(self, joystick1, joystick2, timer, test, writer):
        self.joystick1 = joystick1
        self.joystick2 = joystick2
        self.timer = timer
        self.test = test
        self.writer = writer

    def run(self):
        startTime = self.timer.currentTime()
        lastBadTime = 0
        deltaSum = 0
        deltaN = 0
        initialDelta = -1
        try:
            while True:
                curTime = self.timer.currentTime() - startTime
                pos1 = self.joystick1.position()
                pos2 = self.joystick2.position()
                ok, delta = self.test.process(curTime, pos1, pos2)
                deltaSum += delta
                deltaN += 1
                if initialDelta < 0:
                    initialDelta = delta
                if abs(delta - initialDelta) < 1e-3:
                    startTime = curTime + startTime
                    curTime = 0
                if not ok:
                    lastBadTime = curTime
                    deltaSum = 0
                    deltaN = 0
                if lastBadTime < curTime-self.requiredTime:
                    break
                self.writer.write(curTime, delta)
                self.timer.sleep(self.delay)
        except TestInterruptedError:
            pass
        self.elapsedTime = curTime
        if deltaN > 0:
            self.delta = deltaSum / deltaN
        else:
            self.delta = -1
            