import random

class JoystickImitator:
    _x = 0
    _x0 = 0
    _xfac = 0
    _num = 0
    def __init__(self, x0, xfac, y0=0, yfac=0):
        self._x0 = x0
        self._xfac = xfac
        self._y0 = y0
        self._yfac = yfac
        self.reset()
        
    def position(self):
        """Returns normalized (x,y)-coordinate in [-1,1]"""
        if self._num > 10:
            self._x = self._x0 + (self._x - self._x0) * self._xfac + random.uniform(-1e-3, 1e-3)
            self._y = self._y0 + (self._y - self._y0) * self._yfac + random.uniform(-1e-3, 1e-3)
        self._num += 1
        return (self._x, self._y);
        
    def reset(self):
        self._x = random.uniform(-1, 1)
        self._y = random.uniform(-1, 1)
