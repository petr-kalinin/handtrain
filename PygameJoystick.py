import pygameBridge

class PygameJoystick:
    
    def __init__(self, id):
        self.id = id
        
    def position(self):
        return pygameBridge.getJoystickPosition(self.id)
        
    def reset(self):
        pass
