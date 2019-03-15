import pygame
import settings as v
from ProcToPy import *
v.init()

def Options():
	image(v.BackOpt, 0, 0)
	fill(101, 149, 99)
	textAlign("LEFT")
	text("Music :", 100, 180)
	text("Sound effect :", 100, 244) #260
	text("Timer : ", 100, 308)
	text("Tank's Health :", 100, 372) #340
	text("Type of songs :", 100, 436) #420
	text("Season :", 100, 500) #500
	textSize(13)
	text("Back: Press Tab", 310, 105)
	text("OK: Press Right Arrow", 310, 85)
	# noStroke()


	#Sélection du paramètre

	if v.MenuOpt == 0:
		if v.keyCode == pygame.K_DOWN and v.SMenuOpt < 6:
			v.SMenuOpt += 1
		if v.keyCode == pygame.K_UP and v.SMenuOpt > 1:
			v.SMenuOpt -= 1
		image(v.BalleR, 40, 85+64*v.SMenuOpt)
		delay(100)

	#Fond des barres de volume

	fill(55, 77, 54)
	rect(318, 162, 104, 24)
	rect(318, 226, 104, 24)
	fill(55, 77, 54)
	rect(320, 164, 100, 20)
	rect(320, 228, 100, 20)

	#Interface Musique

	fill(101, 149, 99)
	if v.MenuOpt == 1:
		if v.keyCode == pygame.K_RIGHT and v.MusicVOL < 100:
			v.MusicVOL += 1
		if v.keyCode == pygame.K_LEFT and v.MusicVOL > 0:
			v.MusicVOL -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		#La Barre se colore lorsqu'elle est en stade de modification
		fill(247, 153, 0)
	#Affichage Barre de son
	rect(320, 164, v.MusicVOL, 20) # --------------------------------

	#Interface Effets Sonores

	fill(101, 149, 99)
	if v.MenuOpt == 2:
		if v.keyCode == pygame.K_RIGHT and v.SoundVOL < 100:
			v.SoundVOL += 1
		if v.keyCode == pygame.K_LEFT and v.SoundVOL > 0:
			v.SoundVOL -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		#La Barre se colore lorsqu'elle est en stade de modification
		fill(247, 153, 0)
	#Affichage Barre de son
	rect(320, 228, v.SoundVOL, 20) # --------------------------------


	# Interface timer

	fill(101, 149, 99)
	if v.MenuOpt == 3 and v.Link == 0:
		if v.keyCode == pygame.K_RIGHT:
			v.TSel = 2
		if v.keyCode == pygame.K_LEFT:
			v.TSel = 1
		fill(247, 153, 0)
		triangledeselction()

		if v.TSel == 1:
			triangle(327, 290, 337, 280, 347, 290)
			triangle(327, 315, 337, 325, 347, 315)
		if v.TSel == 2:
			triangle(380, 290, 390, 280, 400, 290)
			triangle(380, 315, 390, 325, 400, 315)

		if v.keyCode == pygame.K_DOWN:
			if v.TSel == 1 and v.DefaultMin > 0:
				v.DefaultMin -= 1
			if v.TSel == 2 and v.DefaultSec > 0:
				v.DefaultSec -= 1
			delay(100)
		if v.keyCode == pygame.K_UP:
			if v.TSel == 1 and v.DefaultMin < 60:
				v.DefaultMin += 1
			if v.TSel == 2 and v.DefaultSec < 60:
				v.DefaultSec += 1
			delay(100)

	textSize(15)
	textAlign("RIGHT")
	text(str(v.DefaultMin)+"   : ", 370, 308)
	textAlign("LEFT")
	text(v.DefaultSec, 380, 308)


	# Interface nombre de vie

	fill(101, 149, 99)
	#Dans le cas ou on arrive au menu option par le Menu principal
	if v.MenuOpt == 4 and v.Link == 0:
		if v.keyCode == pygame.K_RIGHT and v.DefaultVie < 10:
			v.DefaultVie += 1
		if v.keyCode == pygame.K_LEFT and v.DefaultVie > 1:
			v.DefaultVie -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		delay(100)

	for i in range(0, v.DefaultVie):
		image(v.Vies, 320+v.DefaultVie*i, 358)

	# Interface Type de son

	fill(101, 149, 99)
	if v.MenuOpt == 5:
		if v.keyCode == pygame.K_RIGHT and v.TypeDeSon < 2:
			v.TypeDeSon += 1
		if v.keyCode == pygame.K_LEFT and v.TypeDeSon > 1:
			v.TypeDeSon -= 1
		triangledeselction()
		fill(247, 153, 0)
	textSize(15)
	if v.TypeDeSon == 1:
		text("Default", 330, 436)
	if v.TypeDeSon == 2:
		text("Crazy", 330, 436)

	# Interface Design

	fill(101, 149, 99)
	if v.MenuOpt == 6 and v.Link == 0:
		if v.keyCode == pygame.K_RIGHT and v.Design < 4:
			v.Design += 1
			delay(100)
		if v.keyCode == pygame.K_LEFT and v.Design > 1:
			v.Design -= 1
			delay(100)
		triangledeselction()
		fill(247, 153, 0)

	if v.Design == 3 and v.MenuOpt == 6 and v.Link == 0:
		triangle(280, 470, 290, 460, 300, 470)
		triangle(280, 510, 290, 520, 300, 510)
		if v.keyCode == pygame.K_UP and v.SummerDay < 99:
			v.SummerDay += 1
			delay(100)
		if v.keyCode == pygame.K_DOWN and v.SummerDay > 1:
			SummerDay -= 1
			delay(100)

	if v.Design == 4 and v.MenuOpt == 6 and v.Link == 0:
		triangle(380, 470, 390, 460, 400, 470)
		triangle(380, 510, 390, 520, 400, 510)
		if v.keyCode == pygame.K_UP and v.WinterDay < 99:
			v.WinterDay += 1
			delay(100)
		if v.keyCode == pygame.K_DOWN and v.WinterDay > 1:
			v.WinterDay -= 1
			delay(100)

	if v.Design == 1 and v.Link == 0:
		text("Summer", 330, 500)
	if v.Design == 2 and v.Link == 0:
		text("Winter", 330, 500)
	if v.Design == 1 and v.Link == 0 or v.Design == 2 and v.Link == 0:
		v.Changementok = False
	if v.Design > 2 and v.Link == 0:
		text("Summer: "+str(v.SummerDay)+" & Winter: "+str(v.WinterDay), 243, 500)
		v.Changementok = True

	if v.Design == 1 and v.Link == 1 and v.Changementok == False:
		text("Summer", 330, 500)
	if v.Design == 2 and v.Link == 1 and v.Changementok == False:
		text("Winter", 330, 500)
	if v.Changementok == True:
		text("Summer: "+str(v.SummerDay)+" & Winter: "+str(v.WinterDay), 243, 500)

	#Dans le cas ou on arrive au menu option par le Jeu
	#if v.MenuOpt == 4 and v.Link == 1:
	#	fill(255, 0, 0)
	#	text("You can't change the number ", 280, 280+30)
	#	text("Tank's Health now", 310, 330+30)
	#	triangledeselction()
	if v.Link == 1 and (v.MenuOpt == 6 or v.MenuOpt == 4 or v.MenuOpt == 3):
		fill(255, 0, 0)
		textAlign("CENTER")
		text("You can't change this one in game", 250, 490+30)
		textAlign("LEFT")
		triangledeselction()

	#Affichage des Paramêtre
	fill(136, 222, 145)
	textSize(15)
	textAlign("RIGHT")

	text(v.MusicVOL, 420, 180)
	text(v.SoundVOL, 420, 244)
	text(v.DefaultVie, 420, 372)

def triangledeselction():
	if v.Design > 2 or v.Changementok == True:
		triangle(230, 90+64*v.SMenuOpt+20, 240, 80+64*v.SMenuOpt+20, 240, 100+64*v.SMenuOpt+20)
	else:
		triangle(300, 90+64*v.SMenuOpt+20, 310, 80+64*v.SMenuOpt+20, 310, 100+64*v.SMenuOpt+20)
	triangle(430, 80+64*v.SMenuOpt+20, 430, 100+64*v.SMenuOpt+20, 440, 90+64*v.SMenuOpt+20)