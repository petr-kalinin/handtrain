import pygameBridge

class PygameJoystick:
    
    def __init__(self, id):
        self.id = id
        
    def position(self):
        return pygameBridge.getJoystickPosition(self.id)
        
    def reset(self):
        while True:
            pos = self.position()
            x = pos[0];
            y = pos[1];
            print(x,y)
            if (abs(x)<0.1) and (abs(y)<0.1):
                break
            pygameBridge.requestNewEvents()
            pygameBridge.sleep(100)
