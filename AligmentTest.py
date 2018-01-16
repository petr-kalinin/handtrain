import unittest
#from mock import MagicMock

class AligmentTest:
    eps = 1e-1
    needX1 = 0.5;
    needX2 = -0.5;

    def __init__(self, drawer):
        self.drawer = drawer

    def process(self, time, pos):
        x1, y1 = pos[0]
        x2, y2 = pos[1]
        delta1 = abs(x1 - self.needX1)
        delta2 = abs(x2 - self.needX2)
        ok = (delta1<self.eps) and (delta2<self.eps)
        self.draw(time, x1 - self.needX1, x2 - self.needX2, ok)
        return (ok, delta1 + delta2)
            
    def draw(self,curTime,x1,x2, ok):
        self.drawer.reset()
        self.drawer.setState(ok)
        self.drawer.drawObject(0.5, 0.5, False)
        self.drawer.drawObject((1+x1)/2, 0.5, True)
        self.drawer.drawObject((1+x2)/2, 0.5, True)
        self.drawer.drawText(str(curTime/1000))
        self.drawer.show()
    
    def name(self):
        return "Alignment"

            
class AligmentTestTest(unittest.TestCase):
    def test_name(self):
        test = AligmentTest(None)
        self.assertEqual(test.name(), "Alignment")
        
    def test_process(self):
        drawerMock = MagicMock()
        test = AligmentTest(drawerMock)
        res = test.process(10, 1, -1)
        self.assertEqual(res, (False, 1))
        pass
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()