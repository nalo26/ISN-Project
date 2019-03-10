import pygame, Game, ProcToPy


def Menu():
	fill(255)
	background(0)
	fill(101,149,99)
	textSize(20)
	textAlign(CENTER)
	ProcToPy.image(BackgMenu, screen, 0, 0)
	text("Game", 125+30, 150+60)
	text("Editor", 125+30, 350+50)
	text("Options", 375-30, 150+60)
	text("Credits", 375-30, 350+50)
	textSize(15)
	text("Select with arrows and enter and press esc to back", 250, 515)
	if Menu == 1:
		ProcToPy.image(BalleR, screen, 25+30, 120+60)
		ProcToPy.image(BalleL, screen, 175+30, 120+60)
	if Menu == 2:
		ProcToPy.image(BalleR, screen, 25+30, 320+50)
		ProcToPy.image(BalleL, screen, 175+30, 320+50)
	if Menu == 3:
		ProcToPy.image(BalleR, screen, 275-30, 120+60)
		ProcToPy.image(BalleL, screen, 425-30, 120+60)
	if Menu == 4:
		ProcToPy.image(BalleR, screen, 275-30, 320+50)
		ProcToPy.image(BalleL, screen, 425-30, 320+50)
	delay(10)

def MenuPlay():
	if Menu < 1:
		Menu=1
	if Menu > 4:
		Menu=4
	background(0)
	textSize(20)
	textAlign(CENTER)
	ProcToPy.image(BackgMenu, screen,0,0)
	text("1 vs 1 Local", 250, 200)
	text("1 vs IA Local", 250, 270)
	text("Create Server", 250, 340)
	text("Join Server", 250, 410)
	textSize(15)
	text("Select with arrows and enter and press tab to back", 250, 515)
	ProcToPy.image(BalleR, screen, 100, Menu*70+100)
	ProcToPy.image(BalleL, screen, 350, Menu*70+100)
	delay(10)