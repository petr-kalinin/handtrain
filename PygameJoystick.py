import pygameBridge

class PygameJoystick:
    
    def __init__(self, id, drawer):
        self.id = id
        self.drawer = drawer
        
    def position(self):
        return pygameBridge.getJoystickPosition(self.id)
        
    def reset(self):
        while True:
            self.drawer.reset()
            self.drawer.drawCenterText('Отпустите джойстики')
            self.drawer.show()
            pos = self.position()
            x = pos[0];
            y = pos[1];
            print(x,y)
            if (abs(x)<0.1) and (abs(y)<0.1):
                break
            pygameBridge.sleep(100)
