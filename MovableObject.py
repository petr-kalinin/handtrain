class MovableObject:
    def __init__(self, x0, y0, minx, miny, maxx, maxy):
        self.x = x0
        self.y = y0
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, dx, dy, dt):
        self.x += dx * dt
        self.y += dy * dt
        if self.minx is not None and self.x < self.minx:
            self.x = self.minx
        if self.maxx is not None and self.x > self.maxx:
            self.x = self.maxx
        if self.miny is not None and self.y < self.miny:
            self.y = self.miny
        if self.maxy is not None and self.y > self.maxy:
            self.y = self.maxy
