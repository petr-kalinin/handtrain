import pygameBridge
import pygame
from pygame.locals import * # This module contains various constants used by Pygame
import math

from TestInterruptedError import TestInterruptedError

class PygameDrawer:
    interrupted = False
    okState = False
    
    def __init__(self, imageFile = None, bgColor = (0,0,0), okColor = (128, 128, 128), activeColor = (0, 0, 0), targetColor = (128, 128, 128)):
        self.bgColor = bgColor
        self.mode = self.getMode()
        self.okColor = okColor
        self.activeColor = activeColor
        self.targetColor = targetColor
        pygameBridge.createScreen('Test')
        if imageFile is None:
            self.image = pygameBridge.square(0.05)
            self.imageSize = (0.05, 0.05)
        else:
            self.image, self.imageSize = pygameBridge.imageFromFile(imageFile)
            
    def getMode(self):
        avgBg = sum(self.bgColor)
        if avgBg > 255 * 3 / 2:
            return 0#BLEND_SUB
        else:
            return 0#BLEND_ADD
        
    def reset(self):
        pygameBridge.fillBackground(self.bgColor)
        
    def textColor(self):
        return list((255-x for x in self.bgColor))
        
    def color(self, active, ok):
        if active:
            if ok:
                #return (64,255,64)
                return self.okColor
            else:
                #return (255,64,64)
                return self.activeColor
        else:
            return self.targetColor
        
    def drawRectangle(self, width, height, active):
        color = self.color(active, self.okState)
        pygameBridge.drawRectangle(color, 
                                (0.5-width/2, 0.5-height/2),
                                (0.5+width/2, 0.5+height/2),
                                self.mode
                            )

    def drawLine(self, pos1, pos2):
        pygameBridge.drawLine(self.targetColor, pos1, pos2)
        
    def drawObject(self, x, y, active, angle=None, mirror=False):
        print("object @{},{}".format(x, y))
        color = self.color(active, self.okState)
        w, h = self.imageSize
        if not active:
            pygameBridge.drawRectangle(color, (x-w*0.5, y-h*0.5), (x+w*0.5, y+h*0.5), self.mode, False, (-10, -10))
            pygameBridge.drawMark(color, (x, y), self.mode)
        else:
            if isinstance(angle, float):
                pass
            elif angle:
                size = pygameBridge.posToCoordinates((1, 1))
                angle = math.atan2(angle[1] * size[1], angle[0] * size[0])
            else:
                angle = 0
            image = pygameBridge.rotateImage(self.image, angle)
            if mirror:
                image = pygameBridge.mirrorImage(image)
            new_size = image.get_size()
            old_size = self.image.get_size()
            w *= new_size[0] / old_size[0]
            h *= new_size[1] / old_size[1]
            pygameBridge.drawImage(color, (x-w*0.5, y-h*0.5), image, self.mode)
            pygameBridge.drawMark(color, (x, y), self.mode)

        
    def drawText(self, s):
        pygameBridge.drawText(self.textColor(), (0.01, 0.01), s)

    def drawCenterText(self, s):
        pygameBridge.drawText(self.textColor(), (0.5, 0.5), s, True)
        
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
