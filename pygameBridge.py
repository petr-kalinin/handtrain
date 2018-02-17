import pygame, sys, os
import atexit
from pygame.locals import * # This module contains various constants used by Pygame
import pygame.event
from pygame import time
import math

pygame.init()
pygame.joystick.init()

num_joysticks = pygame.joystick.get_count()
joysticks = []
for i in range(num_joysticks):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
    
clock = pygame.time.Clock()
screen = None

dimensions = (800, 600)

font = pygame.font.Font(None, 60)

events = ()

def posToCoordinates(pos):
    x = int(pos[0] * dimensions[0])
    y = int(pos[1] * dimensions[1])
    return (x,y)

def createScreen(caption):
    global screen, dimensions
    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption(caption)
    screen = pygame.display.get_surface()
    dimensions = screen.get_size()

def fillBackground(color):
    background = pygame.Surface(screen.get_size()).convert()
    background.fill(color)
    screen.blit(background, (0,0))
    
def drawRectangle(color, pos1, pos2, flags=0, pixelCoord = False, pixelSizeCorr = (0, 0)):
    x1, y1 = posToCoordinates(pos1)
    x2, y2 = posToCoordinates(pos2)
    x1 -= pixelSizeCorr[0] / 2
    y1 -= pixelSizeCorr[1] / 2
    x2 += pixelSizeCorr[0] / 2
    y2 += pixelSizeCorr[1] / 2
    w = x2 - x1
    h = y2 - y1
    #screen.fill(color, pygame.Rect((x1,y1), (w,h)), flags)
    pygame.draw.ellipse(screen, color, pygame.Rect((x1,y1), (w,h)), 5)

def drawMark(color, pos1, flags=0):
    x, y = posToCoordinates(pos1)
    pygame.draw.line(screen, color, (x-10, y), (x+10, y))
    pygame.draw.line(screen, color, (x, y-10), (x, y+10))

def drawLine(color, pos1, pos2):
    c1 = posToCoordinates(pos1)
    c2 = posToCoordinates(pos2)
    pygame.draw.line(screen, color, c1, c2)

def drawImage(color, pos, image, flags=0):
    pic = pygame.Surface(image.get_size()).convert_alpha()
    color = list(color)
    color.append(255)
    pic.fill(color)
    pic.blit(image, (0,0), None, BLEND_RGBA_MULT)
    screen.blit(pic, posToCoordinates(pos), None, flags)
    
def drawText(color, pos, s, center = False):
    bmp = font.render(s, True, color)
    x,y = posToCoordinates(pos)
    if center:
        x = x - bmp.get_width()/2
    screen.blit(bmp, (x,y))
    
def show():
    pygame.display.flip()
    
def getJoystickPosition(i):
    return (joysticks[i].get_axis(0), joysticks[i].get_axis(1))

def getEvents():
    return events

def requestNewEvents():
    global events
    events = pygame.event.get()
    
def sleep(time):
    fps = int(1000/time)
    clock.tick(fps)
    
def currentTime():
    return pygame.time.get_ticks()

def square(size):
    w,h = posToCoordinates((size, size))
    res = pygame.Surface((w,h)).convert()
    res.fill((255,255,255))
    return res

def imageFromFile(fileName):
    res = pygame.image.load(fileName).convert_alpha()
    x, y = res.get_size()
    return res, (x/dimensions[0], y/dimensions[1])

def rotateImage(image, angle):
    return pygame.transform.rotate(image, math.degrees(angle))

def mirrorImage(image):
    return pygame.transform.flip(image, True, False)

@atexit.register
def quit():
    pygame.quit()
