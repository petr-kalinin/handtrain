class JoystickImitator:
    _x = 0
    _fac = 0
    def __init__(self, x, fac):
        self._x = x
        self._fac = fac
        
    def x(self):
        """Returns normalized x-coordinate in [-1,1]"""
        self._x = self._x * self._fac
        return self._x;
        
    def y(self):
        """Returns normalized y-coordinate in [-1,1]"""
        return 0;