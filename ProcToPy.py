import pygame
from random import *
import settings as v
v.init()

ColorMaster = (255, 255, 255)

def fill(r, g=-1, b=-1, a=0): #Red color, Green color, blue color, alpha (transparency)
	if g == -1 and b == -1:
		g = r
		b = r
	return (r, g, b, a)


def rect(x, y, w, h): #x position, y position, width, height
	# from Game import screen, ColorMaster
	return pygame.draw.rect(v.screen, v.ColorMaster, [x, y, w, h], 0)

def triangle(a, b, c, d, e, f): #x1, y1, x2, y2, x3, y3 positions
	# from Game import screen, ColorMaster
	return pygame.draw.polygon(v.screen, v.ColorMaster, [(a, b), (c, d), (e, f)], 0)

def ellipse(x, y, w, h): #x position, y position, width, height
	# from Game import screen, ColorMaster
	return pygame.draw.ellipse(v.screen, v.ColorMaster, [x, y, x+w, y+h], 0)

def image(i, x, y): #image name, screen, x position, y position
	# from Game import screen
	return v.screen.blit(i, (x, y))

def text(t, x, y): #text, font, screen, size, color, x position, y position
	# from Game import screen, font, fontSize, ColorMaster
	# print(t, ColorMaster)
	return v.screen.blit(v.font.render(str(t), v.fontSize, v.ColorMaster), (x , y))

def textAlign(a): #align position needed
	pass

def textSize(s): #size needed
	# from Game import fontName
	v.font = pygame.font.SysFont(v.fontName, s)
	return v.font

def random(min, max): #minimum value, maximum value
	return randint(min, max)

def delay(t): #time (ms)
	return pygame.time.delay(t)

def background(r, g=-1, b=-1): #Red color, Green color, blue color
	# from Game import screen
	if g == -1 and b == -1:
		g = r
		b = r
	return v.screen.fill((r, g, b))

def noStroke():
	pass