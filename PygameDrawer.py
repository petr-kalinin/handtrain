import pygameBridge
import pygame
from pygame.locals import * # This module contains various constants used by Pygame

from TestInterruptedError import TestInterruptedError

class PygameDrawer:
    interrupted = False
    okState = False
    
    def __init__(self, imageFile = None):
        pygameBridge.createScreen('Test')
        if imageFile is None:
            self.image = pygameBridge.square(0.05)
            self.imageSize = (0.05, 0.05)
        else:
            self.image, self.imageSize = pygameBridge.imageFromFile(imageFile)
        
    def reset(self):
        pygameBridge.fillBackground((0,0,0))
        
    def color(self, active, ok):
        if active:
            if ok:
                return (64,255,64)
            else:
                return (255,64,64)
        else:
            return(128,128,128)
        
    def drawRectangle(self, width, height, active):
        color = self.color(active, self.okState)
        pygameBridge.drawRectangle(color, 
                                (0.5-width/2, 0.5-height/2),
                                (0.5+width/2, 0.5+height/2),
                                BLEND_ADD
                            )
        
    def drawObject(self, x, active):
        print("object @" + str(x))
        color = self.color(active, self.okState)
        w, h = self.imageSize
        if not active:
            pygameBridge.drawRectangle(color, (x-w*0.55, 0.5-h*0.55), (x+w*0.55, 0.5+h*0.55), BLEND_ADD)
        else:
            pygameBridge.drawImage(color, (x-w*0.5, 0.5-h*0.5), self.image, BLEND_ADD)

        
    def drawText(self, s):
        pygameBridge.drawText((255,255,255), (0.01, 0.01), s)

    def drawCenterText(self, s):
        pygameBridge.drawText((255,255,255), (0.5, 0.5), s, True)
        
    def setState(self, ok):
        self.okState = ok
        
    def show(self):
        pygameBridge.show()
        pygameBridge.requestNewEvents()
        events = pygameBridge.getEvents()
        for event in events:
            if event.type == QUIT:
                raise TestInterruptedError()
            if (event.type == KEYUP) and (event.key == pygame.K_ESCAPE):
                raise TestInterruptedError()
