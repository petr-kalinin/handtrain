import pygameBridge

class PygameTimer:
    def currentTime(self):
        return pygameBridge.currentTime()
        
    def sleep(self,x):
        pygameBridge.sleep(x)
