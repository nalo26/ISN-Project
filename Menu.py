import pygame
import settings as v
from ProcToPy import *
v.init()

def MenuMain():
	# from Game import ColorMaster, font, BackgMenu, screen, BalleR, BalleL
	background(0)
	v.ColorMaster = fill(101,149,99)
	v.font = textSize(20)
	# textAlign(CENTER)
	image(v.BackgMenu, 0, 0)
	text("Game", 125+30, 150+60)
	text("Editor", 125+30, 350+50)
	text("Options", 375-30, 150+60)
	text("Credits", 375-30, 350+50)
	v.font = textSize(15)
	text("Select with arrows and enter and press esc to back", 250, 515)
	if v.Menu == 1:
		image(v.BalleR, 25+30, 120+60)
		image(v.BalleL, 175+30, 120+60)
	if v.Menu == 2:
		image(v.BalleR, 25+30, 320+50)
		image(v.BalleL, 175+30, 320+50)
	if v.Menu == 3:
		image(v.BalleR, 275-30, 120+60)
		image(v.BalleL, 425-30, 120+60)
	if v.Menu == 4:
		image(v.BalleR, 275-30, 320+50)
		image(v.BalleL, 425-30, 320+50)
	delay(10)

def MenuPlay():
	# from Game import font, BackgMenu, BalleL, BalleR
	if v.Menu < 1:
		v.Menu=1
	if v.Menu > 4:
		v.Menu=4
	background(0)
	v.font = textSize(20)
	# textAlign(CENTER)
	image(v.BackgMenu,0,0)
	text("1 vs 1 Local", 250, 200)
	text("1 vs IA Local", 250, 270)
	text("Create Server", 250, 340)
	text("Join Server", 250, 410)
	v.font = textSize(15)
	text("Select with arrows and enter and press tab to back", 250, 515)
	image(v.BalleR, 100, v.Menu*70+100)
	image(v.BalleL, 350, v.Menu*70+100)
	delay(10)