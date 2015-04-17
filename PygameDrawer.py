import pygameBridge
import pygame
from pygame.locals import * # This module contains various constants used by Pygame

from TestInterruptedError import TestInterruptedError

class PygameDrawer:
    interrupted = False
    okState = False
    
    def __init__(self):
        pygameBridge.createScreen('Test')
        
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
        dx = 0.05
        if not active:
            dx = 0.06
        pygameBridge.drawRectangle(color, (x-dx, 0.5-dx), (x+dx, 0.5+dx), BLEND_ADD)
        
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
