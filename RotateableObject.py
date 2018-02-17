class RotateableObject:
    def __init__(self, angle0, minAngle, maxAngle):
        self.angle = angle0
        self.minAngle = minAngle
        self.maxAngle = maxAngle

    def process(self, dAngle, dt):
        self.angle += dAngle * dt
        if self.minAngle is not None and self.angle < self.minAngle:
            self.angle = self.minAngle
        if self.maxAngle is not None and self.angle > self.maxAngle:
            self.angle = self.maxAngle
