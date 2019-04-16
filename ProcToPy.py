import pygame
from random import *
import settings as v
v.init()

def fill(r, g=-1, b=-1, a=0): #Red color, Green color, blue color, alpha (transparency)
	if g == -1 and b == -1:
		g = r
		b = r
	v.ColorMaster = (r, g, b, a)

def rect(x, y, w, h): #x position, y position, width, height
	return pygame.draw.rect(v.screen, v.ColorMaster, [x, y, w, h], 0)

def triangle(a, b, c, d, e, f): #x1, y1, x2, y2, x3, y3 positions
	return pygame.draw.polygon(v.screen, v.ColorMaster, [(a, b), (c, d), (e, f)], 0)

def ellipse(x, y, w, h): #x position, y position, width, height
	return pygame.draw.ellipse(v.screen, v.ColorMaster, [x-(w/2), y-(h/2), w, h], 0)

def image(i, x, y, w=0, h=0): #image name, x position, y position, width, height
	if w == 0 and h == 0:
		w = i.get_width()
		h = i.get_height()
	i = pygame.transform.scale(i, (w, h))
	return v.screen.blit(i, (x, y))

def text(t, x, y): #text, x position, y position
	y_add = v.fontSize * -1
	if v.textAlignMaster == 'LEFT':
		x_add = 0
	if v.textAlignMaster == 'CENTER':
		x_add = int(((int(len(str(t)))*v.fontSize/2) / 2) * -1 + v.fontSize/2)
	if v.textAlignMaster == 'RIGHT':
		x_add = int((int(len(str(t)))*v.fontSize/2) * -1 + v.fontSize/2)

	return v.screen.blit(v.font.render(str(t), v.fontSize, v.ColorMaster), (x+x_add , y+y_add))

def textAlign(a): #align position needed
	if a.upper() == 'LEFT' or a.upper() == 'CENTER' or a.upper() == 'RIGHT':
		v.textAlignMaster = str(a.upper())
	else:
		print('The Align method \''+a.upper()+'\' doesn\'t exist !')
		v.textAlignMaster = 'LEFT'
		return pygame.quit()


def textSize(s): #size needed
	v.font = pygame.font.SysFont(v.fontName, s)
	v.fontSize = s

def random(min, max): #minimum value, maximum value
	return randint(min, max)

def delay(t): #time (ms)
	return pygame.time.delay(t)

def background(r, g=-1, b=-1): #Red color, Green color, blue color
	if g == -1 and b == -1:
		g = r
		b = r
	return v.screen.fill((r, g, b))

def noStroke():
	pass