from TestInterruptedError import TestInterruptedError

class TestController:
    delay = 10
    maxTime = 5 * 60 * 1000

    def __init__(self, joysticks, timer, test, writer, requiredTime = 5000):
        self.joysticks = joysticks
        self.timer = timer
        self.test = test
        self.writer = writer
        self.requiredTime = requiredTime

    def run(self):
        for j in self.joysticks:
            j.reset()
        startTime = self.timer.currentTime()
        lastBadTime = 0
        deltaSum = 0
        deltaN = 0
        initialDelta = -1
        try:
            while True:
                curTime = self.timer.currentTime() - startTime
                pos = list(j.position() for j in self.joysticks)
                ok, delta = self.test.process(curTime, pos)
                deltaSum += delta
                deltaN += 1
                if initialDelta < 0:
                    initialDelta = delta
                if (abs(delta - initialDelta) < 1e-3) and (abs(initialDelta) > 1e-1):
                    startTime = curTime + startTime
                    curTime = 0
                if not ok:
                    lastBadTime = curTime
                    deltaSum = 0
                    deltaN = 0
                if lastBadTime < curTime-self.requiredTime:
                    break
                if curTime > self.maxTime:
                    raise TestInterruptedError
                self.writer.write(curTime, delta)
                self.timer.sleep(self.delay)
        except TestInterruptedError:
            pass
        self.elapsedTime = curTime
        if deltaN > 0:
            self.delta = deltaSum / deltaN
        else:
            self.delta = -1
        return self.delta
            