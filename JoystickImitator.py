import random

class JoystickImitator:
    _x = 0
    _x0 = 0
    _fac = 0
    _num = 0
    def __init__(self, x0, fac):
        self._x0 = x0
        self._fac = fac
        self.reset()
        
    def position(self):
        """Returns normalized (x,y)-coordinate in [-1,1]"""
        if self._num > 10:
            self._x = self._x0 + (self._x - self._x0) * self._fac + random.uniform(-1e-3, 1e-3)
        self._num += 1
        return (self._x, 0);
        
    def reset(self):
        self._x = random.uniform(-1, 1)
