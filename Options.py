from ProcToPy import *

def Options():
	from Game import *
	image(BackOpt, screen, 0, 0)
	ColorMaster = fill(101, 149, 99)
	textAlign(LEFT)
	text("Music :", 100, 180)
	text("Sound effect :", 100, 244) #260
	text("Timer : ", 100, 308)
	text("Tank's Health :", 100, 372) #340
	text("Type of songs :", 100, 436) #420
	text("Season :", 100, 500) #500
	font = textSize(13)
	text("Back: Press Tab", 310, 105)
	text("OK: Press Right Arrow", 310, 85)
	noStroke()


	#Sélection du paramètre

	if MenuOpt == 0:
		if keyPressed == True and keyCode == DOWN and SMenuOpt < 6:
			SMenuOpt += 1
		if keyPressed == True and keyCode == UP and SMenuOpt > 1:
			SMenuOpt -= 1
		image(BalleR, screen, 40, 85+64*SMenuOpt)
		delay(100)

	#Fond des barres de volume

	ColorMaster = fill(55, 77, 54)
	rect(318, 162, 104, 24)
	rect(318, 226, 104, 24)
	ColorMaster = fill(55, 77, 54)
	rect(320, 164, 100, 20)
	rect(320, 228, 100, 20)

	#Interface Musique

	ColorMaster = fill(101, 149, 99)
	if MenuOpt == 1:
		if keyPressed == True and keyCode == RIGHT and MusicVOL < 100:
			MusicVOL += 1
		if keyPressed == True and keyCode == LEFT and MusicVOL > 0:
			MusicVOL -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		#La Barre se colore lorsqu'elle est en stade de modification
		ColorMaster = fill(247, 153, 0)
	#Affichage Barre de son
	rect(320, 164, float(MusicVOL), 20)

	#Interface Effets Sonores

	ColorMaster = fill(101, 149, 99)
	if MenuOpt == 2:
		if keyPressed == True and keyCode == RIGHT and SoundVOL < 100:
			SoundVOL += 1
		if keyPressed == True and keyCode == LEFT and SoundVOL > 0:
			SoundVOL -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		#La Barre se colore lorsqu'elle est en stade de modification
		ColorMaster = fill(247, 153, 0)
	#Affichage Barre de son
	rect(320, 228, float(SoundVOL), 20)


	# Interface timer

	ColorMaster = fill(101, 149, 99)
	if MenuOpt == 3 and Link == 0:
		if keyPressed == True and keyCode == RIGHT:
			TSel = 2
		if keyPressed == True and keyCode == LEFT:
			TSel = 1
		ColorMaster = fill(247, 153, 0)
		triangledeselction()

		if TSel == 1:
			triangle(327, 290, 337, 280, 347, 290)
			triangle(327, 315, 337, 325, 347, 315)
		if TSel == 2:
			triangle(380, 290, 390, 280, 400, 290)
			triangle(380, 315, 390, 325, 400, 315)

		if keyPressed == True and keyCode == DOWN:
			if TSel == 1 and DefaultMin > 0:
				DefaultMin -= 1
			if TSel == 2 and DefaultSec > 0:
				DefaultSec -= 1
			delay(100)
		if keyPressed == True and keyCode == UP:
			if TSel == 1 and DefaultMin < 60:
				DefaultMin += 1
			if TSel == 2 and DefaultSec < 60:
				DefaultSec += 1
			delay(100)

	font = textSize(15)
	textAlign(RIGHT)
	text(DefaultMin+"   : ", 370, 308)
	textAlign(LEFT)
	text(DefaultSec, 380, 308)


	# Interface nombre de vie

	ColorMaster = fill(101, 149, 99)
	#Dans le cas ou on arrive au menu option par le Menu principal
	if MenuOpt == 4 and Link == 0:
		if keyPressed == True and keyCode == RIGHT and DefaultVie < 10:
			DefaultVie += 1
		if keyPressed == True and keyCode == LEFT and DefaultVie > 1:
			DefaultVie -= 1
		#Triangle de pour montrer comment régler le son
		triangledeselction()
		delay(100)

	for i in range(0, DefaultVie):
		image(Vies, screen, 320+DefaultVie*i, 358)

	# Interface Type de son

	ColorMaster = fill(101, 149, 99)
	if MenuOpt == 5:
		if keyPressed == True and keyCode == RIGHT and TypeDeSon < 2:
			TypeDeSon += 1
		if keyPressed == True and keyCode == LEFT and TypeDeSon > 1:
			TypeDeSon -= 1
		triangledeselction()
		ColorMaster = fill(247, 153, 0)
	font = textSize(15)
	if TypeDeSon == 1:
		text("Default", 330, 436)
	if TypeDeSon == 2:
		text("Crazy", 330, 436)

	# Interface Design

	ColorMaster = fill(101, 149, 99)
	if MenuOpt == 6 and Link == 0:
		if keyPressed == True and keyCode == RIGHT and Design < 4:
			Design += 1
			delay(100)
		if keyPressed == True and keyCode == LEFT and Design > 1:
			Design -= 1
			delay(100)
		triangledeselction()
		ColorMaster = fill(247, 153, 0)

	if Design == 3 and MenuOpt == 6 and Link == 0:
		triangle(280, 470, 290, 460, 300, 470)
		triangle(280, 510, 290, 520, 300, 510)
		if keyPressed == True and keyCode == UP and SummerDay < 99:
			SummerDay += 1
			delay(100)
		if keyPressed == True and keyCode == DOWN and SummerDay > 1:
			SummerDay -= 1
			delay(100)

	if Design == 4 and MenuOpt == 6 and Link == 0:
		triangle(380, 470, 390, 460, 400, 470)
		triangle(380, 510, 390, 520, 400, 510)
		if keyPressed == True and keyCode == UP and WinterDay < 99:
			WinterDay += 1
			delay(100)
		if keyPressed == True and keyCode == DOWN and WinterDay > 1:
			WinterDay -= 1
			delay(100)

	if Design == 1 and Link == 0:
		text("Summer", 330, 500)
	if Design == 2 and Link == 0:
		text("Winter", 330, 500)
	if Design == 1 and Link == 0 or Design == 2 and Link == 0:
		Changementok = False
	if Design > 2 and Link == 0:
		text("Summer: "+SummerDay+" & Winter: "+WinterDay, 243, 500)
		Changementok = True

	if Design == 1 and Link == 1 and Changementok == False:
		text("Summer", 330, 500)
	if Design == 2 and Link == 1 and Changementok == False:
		text("Winter", 330, 500)
	if Changementok == True:
		text("Summer: "+SummerDay+" & Winter: "+WinterDay, 243, 500)

	#Dans le cas ou on arrive au menu option par le Jeu
	#if MenuOpt == 4 and Link == 1:
	#	ColorMaster = fill(255, 0, 0)
	#	text("You can't change the number ", 280, 280+30)
	#	text("Tank's Health now", 310, 330+30)
	#	triangledeselction()
	if Link == 1 and (MenuOpt == 6 or MenuOpt == 4 or MenuOpt == 3):
		ColorMaster = fill(255, 0, 0)
		textAlign(CENTER)
		text("You can't change this one in game", 250, 490+30)
		textAlign(LEFT)
		triangledeselction()

	#Affichage des Paramêtre
	ColorMaster = fill(136, 222, 145)
	font = textSize(15)
	textAlign(RIGHT)

	text(MusicVOL, 420, 180)
	text(SoundVOL, 420, 244)
	text(DefaultVie, 420, 372)

def triangledeselction():
	if Design > 2 or Changementok == True:
		triangle(230, 90+64*SMenuOpt+20, 240, 80+64*SMenuOpt+20, 240, 100+64*SMenuOpt+20)
	else:
		triangle(300, 90+64*SMenuOpt+20, 310, 80+64*SMenuOpt+20, 310, 100+64*SMenuOpt+20)
	triangle(430, 80+64*SMenuOpt+20, 430, 100+64*SMenuOpt+20, 440, 90+64*SMenuOpt+20)