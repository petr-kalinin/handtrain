import pygame, sys, os
import atexit
from pygame.locals import * # This module contains various constants used by Pygame
import pygame.event
from pygame import time

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
    
def drawRectangle(color, pos1, pos2, flags=0):
    x1, y1 = posToCoordinates(pos1)
    x2, y2 = posToCoordinates(pos2)
    w = x2 - x1
    h = y2 - y1
    screen.fill(color, pygame.Rect((x1,y1), (w,h)), flags)
    
def drawText(color, pos, s):
    bmp = font.render(s, True, color)
    x,y = posToCoordinates(pos)
    screen.blit(bmp, pos)
    
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

@atexit.register
def quit():
    pygame.quit()
