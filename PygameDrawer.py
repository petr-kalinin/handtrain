import pygameBridge
import pygame
from pygame.locals import * # This module contains various constants used by Pygame

class PygameDrawer:
    interrupted = False
    
    def __init__(self):
        pygameBridge.createScreen('Test')
        
    def reset(self):
        pygameBridge.fillBackground((0,0,0))
        
    def drawRectangle(self, width, height):
        pygameBridge.drawRectangle((255,255,255), 
                                (0.5-width/2, 0.5-height/2),
                                (0.5+width/2, 0.5+height/2)
                            )
        
    def drawObject(self, x, active):
        print("object @" + str(x))
        color = (128,128,128)
        if active:
            color = (255,255,255)
        pygameBridge.drawRectangle(color, (x-0.05, 0.45), (x+0.05, 0.55))
        
    def drawText(self, s):
        pygameBridge.drawText((255,255,255), (0.05, 0.05), s)
        
    def setState(self, ok):
        pass
        
    def show(self):
        pygameBridge.show()
        pygameBridge.requestNewEvents()
        events = pygameBridge.getEvents()
        for event in events:
            if event.type == QUIT:
                self.interrupted = True
            if (event.type == KEYUP) and (event.key == pygame.K_ESCAPE):
                self.interrupted = True
