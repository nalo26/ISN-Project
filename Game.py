import os, pygame
from ProcToPy import *
import settings as v

from Credits import * # Charger les autres fenêtres 
from Getkey import *
from IA import *
from Menu import *
from MenuEditeur import *
from MenuMaps import *
from Options import *
from Client import *
v.init()

MainGameMaster = True

# import processing.sound.*
# SoundFile Fire
# SoundFile Move
# SoundFile MusicBackground

pygame.init()
v.screen = pygame.display.set_mode((500, 550)) # Définir la taille de l'écran
pygame.font.SysFont(v.fontName, v.fontSize)
v.width, v.height = pygame.display.get_surface().get_size()

#Chargement des images du jeu
v.BackgMenu = pygame.image.load("data/BackMenu.png").convert()
v.BackOpt = pygame.image.load("data/Options.png").convert()
v.Credits = pygame.image.load("data/Crédits.png").convert()

v.arbre = pygame.image.load("data/arbre.png").convert_alpha()
v.Montagne = pygame.image.load("data/Montagne.png").convert_alpha()
v.Eau = pygame.image.load("data/Eau.png").convert()
v.Lave = pygame.image.load("data/Lave.png").convert()
v.ContH = pygame.image.load("data/Lavehaut.png").convert_alpha()
v.ContB = pygame.image.load("data/Lavebas.png").convert_alpha()
v.ContG = pygame.image.load("data/Lavegauche.png").convert_alpha()
v.ContD = pygame.image.load("data/Lavedroite.png").convert_alpha()
v.ContHD = pygame.image.load("data/Lavehaut+droite.png").convert_alpha()
v.ContHG = pygame.image.load("data/Lavehaut+gauche.png").convert_alpha()
v.ContBD = pygame.image.load("data/Lavebas+droite.png").convert_alpha()
v.ContBG = pygame.image.load("data/Lavebas+gauche.png").convert_alpha()

v.arbreW = pygame.image.load("data/arbreW.png").convert_alpha()
v.MontagneW = pygame.image.load("data/MontagneW.png").convert_alpha()
v.EauW = pygame.image.load("data/EauW.png").convert()
v.LaveW = pygame.image.load("data/LaveW.png").convert()
v.ContHW = pygame.image.load("data/LavehautW.png").convert_alpha()
v.ContBW = pygame.image.load("data/LavebasW.png").convert_alpha()
v.ContGW = pygame.image.load("data/LavegaucheW.png").convert_alpha()
v.ContDW = pygame.image.load("data/LavedroiteW.png").convert_alpha()
v.ContHDW = pygame.image.load("data/Lavehaut+droiteW.png").convert_alpha()
v.ContHGW = pygame.image.load("data/Lavehaut+gaucheW.png").convert_alpha()
v.ContBDW = pygame.image.load("data/Lavebas+droiteW.png").convert_alpha()
v.ContBGW = pygame.image.load("data/Lavebas+gaucheW.png").convert_alpha()

v.STank1 = pygame.image.load("data/Selection Tank1.png").convert_alpha()
v.STank2 = pygame.image.load("data/Selection Tank2.png").convert_alpha()
v.Tank1 = pygame.image.load("data/Tank1u.png").convert_alpha()
v.Tank1u = pygame.image.load("data/Tank1u.png").convert_alpha()
v.Tank1d = pygame.image.load("data/Tank1d.png").convert_alpha()
v.Tank1r = pygame.image.load("data/Tank1r.png").convert_alpha()
v.Tank1l = pygame.image.load("data/Tank1l.png").convert_alpha()
v.Tank2 = pygame.image.load("data/Tank2d.png").convert_alpha()
v.Tank2u = pygame.image.load("data/Tank2u.png").convert_alpha()
v.Tank2d = pygame.image.load("data/Tank2d.png").convert_alpha()
v.Tank2r = pygame.image.load("data/Tank2r.png").convert_alpha()
v.Tank2l = pygame.image.load("data/Tank2l.png").convert_alpha()
v.Vies = pygame.image.load("data/Vies.png").convert_alpha()
v.BalleU = pygame.image.load("data/BalleU.png").convert_alpha()
v.BalleD = pygame.image.load("data/BalleD.png").convert_alpha()
v.BalleR = pygame.image.load("data/BalleR.png").convert_alpha()
v.BalleL = pygame.image.load("data/BalleL.png").convert_alpha()
v.BalleExplosion = pygame.image.load("data/Explosion.png").convert_alpha()

def CDD():
	# Cadrillage Des Déplacements (Tanks)
	CDDx = v.xbase/50
	CDDy = v.ybase/50*10
	CDD = CDDx + CDDy
	# Permet de fixer des limites pour la glisse sur la glace
	v.bord = False

	# Colisions cotés de terrain (Déplacements), si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
	if CDDx < 0:
		CDD += 1
		v.xbase += 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDy < 0:
		CDD += 10
		v.ybase += 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDx > 9:
		CDD -= 1
		v.xbase -= 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDy > 90:
		CDD -= 10
		v.ybase += 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	# Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if v.Collision[int(CDD)] == 1:
		v.TestCadriD = 0
		v.TD2 = 1
	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
	if v.Collision[int(CDD)] == 3 and v.Design == 1:
		v.TestCadriD=0
		v.TD2=1
	if v.Collision[int(CDD)] == 3 and v.Design == 2:
		v.TestCadriD = 1
		v.TD2 = 1
		v.vietank1 -= 1
		v.DegatsLaveTank = True
	else:
		v.DegatsLaveTank = False
	#Si le tank va dans l'eau (Il est alors ralenti)
	if v.Collision[int(CDD)] == 2 and v.Design == 1:
		v.CP -= 1
	#Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
	if v.Collision[int(CDD)] == 2 and v.Design == 2:

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_RIGHT and v.bord == False:
			v.xbase += 50
			if v.xbase <= 450:
				CDDx = v.xbase/50
			else:
				v.bord = True 
				v.xbase -= 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.xbase -= 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_LEFT and v.bord == False:
			v.xbase -= 50
			if v.xbase >= 0:
				CDDx = v.xbase/50
			else:
				v.bord = True 
				v.xbase += 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.xbase += 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_UP and v.bord == False:
			v.ybase -= 50
			if v.ybase >= 0:
				CDDy = v.ybase/50*10
			else:
				v.bord = True 
				v.ybase += 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.ybase += 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_DOWN and v.bord == False:
			v.ybase += 50
			if v.ybase <= 450:
				CDDy = v.ybase/50*10
			else:
				v.bord = True 
				v.ybase -= 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.ybase -= 50
			AffTank()

def CDD2():
	#Cadrillage Des Déplacements (Tanks)
	CDDx = v.xbase2/50
	CDDy = v.ybase2/50*10
	CDD = CDDx + CDDy
	#Permet de fixer les bug sur les déplacements avec la glace
	v.bord = False

	#Colisions cotés de terrain (Déplacements), si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
	if CDDx < 0:
		CDD += 1
		v.xbase2 += 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDy < 0:
		CDD += 10
		v.base2 += 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDx > 9: 
		CDD -= 1
		v.xbase2 -= 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1
	if CDDy > 90:
		CDD -= 10
		v.ybase2 -= 50
		v.CP += 1
		if v.Collision[int(CDD)] == 2:
			v.CP += 1

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if v.Collision[int(CDD)] == 1:
		v.TestCadriD = 0
		v.TD2 = 1

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
	if v.Collision[int(CDD)] == 3 and v.Design == 1:
		v.TestCadriD = 0
		v.TD2 = 1

	if v.Collision[int(CDD)] == 3 and v.Design == 2:
		v.TestCadriD = 1
		v.TD2 = 1
		v.vietank2 -= 1
		v.DegatsLaveTank = True
	else:
		v.DegatsLaveTank = False
	#Si le tank va dans l'eau (Il est alors ralenti)
	if v.Collision[int(CDD)] == 2 and v.Design == 1:
		v.CP -= 1
	#Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
	if v.Collision[int(CDD)] == 2 and v.Design == 2:

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_RIGHT and v.bord == False:
			v.xbase2 += 50
			if v.xbase2 <= 450:
				CDDx = v.xbase2/50
			else:
				v.bord = True 
				v.xbase2 -= 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.xbase2 -= 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_LEFT and v.bord == False:
			v.xbase2 -= 50
			if v.xbase2 >= 0:
				CDDx = v.xbase2/50
			else:
				v.bord = True 
				v.xbase2 += 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.xbase2 += 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_UP and v.bord == False:
			v.ybase2 -= 50
			if v.ybase2 >= 0:
				CDDy = v.ybase2/50*10
			else:
				v.bord = True 
				v.ybase2 += 50
			CDD = CDDx + CDDy
			if Collision[int(CDD)] == 1:
				v.bord = True
				v.ybase2 += 50
			AffTank()

		while v.Collision[int(CDD)] == 2 and v.keyCode==pygame.K_DOWN and v.bord == False:
			v.ybase2 += 50
			if v.ybase2 <= 450:
				CDDy = v.ybase2/50*10
			else:
				v.bord = True 
				v.ybase2 -= 50
			CDD = CDDx + CDDy
			if v.Collision[int(CDD)] == 1:
				v.bord = True
				v.ybase2 -= 50
			AffTank()

def CDA():
	#Cadrillage Des Attaques (Bullets)
	CDAx = v.xbasem / 50
	CDAy = v.ybasem / 50 * 10
	CDA = CDAx + CDAy

	#Colisions cotés de terrain (Attaque)
	if CDAx < 0:
		CDA += 1
		v.CB = 0
	if CDAy < 0:
		CDA += 10
		v.CB = 0
	if CDAx > 9:
		CDA -= 1
		v.CB = 0
	if CDAy > 90:
		CDA -= 10
		v.CB = 0

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if v.Collision[int(CDA)] == 1:
		v.CB=0
	if v.Collision[int(CDA)] == 1 and v.Design==2:
		v.Collision[int(CDA)] = 0
	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
	if v.Collision[int(CDA)] == 4:
		v.CB=0


def AffTank(): #Affiche le tank et la map
	# toPrint = '\n'
	# for l in range(10):
	# 	for j in range(10):
	# 		toPrint += str(v.Collision[j+l*10])+" "
	# 	toPrint += "\n"
	# print(toPrint)

	delay(50)
	if v.Design == 1:
		background(45, 139, 97)
	if v.Design == 2:
		background(196, 247, 255)
	#Affichage barre d'info
	fill(0)
	rect(0, 500, 500, 50)
	fill(200)
	rect(0, 500, 500, 3)
	# noStroke()

	for x in range(10):
		for y in range(10):
			Ax = x
			Ay = y * 10
			A = Ax + Ay

			if v.Collision[int(A)] == 1 and v.Design==1:
				image(v.Montagne, x*50, y*50)
			if v.Collision[int(A)] == 1 and v.Design==2:
				image(v.MontagneW, x*50, y*50)
			#Couleur Roche
			if v.Collision[int(A)] == 2:
				#Eau
				if v.Design == 1:
					image(v.Eau, x*50, y*50)
				if v.Design == 2:
					image(v.EauW, x*50, y*50)
				#rebors eau
				if A>10 and v.Collision[int(A-10)] !=2:
					if v.Design == 1:
						image(v.ContH, x*50, y*50)
					if v.Design == 2:
						image(v.ContHW, x*50, y*50)
					v.Haut = True
				if A<90 and v.Collision[int(A+10)] !=2:
					if v.Design == 1:
						image(v.ContB, x*50, y*50)
					if v.Design == 2:
						image(v.ContBW, x*50, y*50)
					v.Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and v.Collision[int(A-1)] !=2:
					if v.Design == 1:
						image(v.ContG, x*50, y*50)
					if v.Design == 2:
						image(v.ContGW, x*50, y*50)
					v.Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and v.Collision[int(A+1)] !=2:
					if v.Design == 1:
						image(v.ContD, x*50, y*50)
					if v.Design == 2:
						image(v.ContDW, x*50, y*50)
					v.Droite = True
				#Coins/angles lave
				#Eté
				if v.Haut == True and v.Droite == True and v.Design == 1:
					image(v.ContHD, x*50, y*50)
				if v.Haut == True and v.Gauche == True and v.Design == 1:
					image(v.ContHG, x*50, y*50)
				if v.Bas == True and v.Droite == True and v.Design == 1:
					image(v.ContBD, x*50, y*50)
				if v.Bas == True and v.Gauche == True and v.Design == 1:
					image(v.ContBG, x*50, y*50)

				if v.Haut == True and v.Droite==True and v.Design == 2:
					image(v.ContHDW, x*50, y*50)
				if v.Haut == True and v.Gauche==True and v.Design == 2:
					image(v.ContHGW, x*50, y*50)
				if v.Bas == True and v.Droite==True and v.Design == 2:
					image(v.ContBDW, x*50, y*50)
				if v.Bas == True and v.Gauche==True and v.Design == 2:
					image(v.ContBGW, x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				v.Bas = False
				v.Haut = False
				v.Droite = False
				v.Gauche = False

			if v.Collision[int(A)] == 3:
				#Lave
				if v.Design == 1:
					image(v.Lave, x*50, y*50)
				if v.Design == 2:
					image(v.LaveW, x*50, y*50)
				#rebors lave
				if A>10 and v.Collision[int(A-10)] != 3:
					if v.Design == 1:
						image(v.ContH, x*50, y*50)
					if v.Design == 2:
						image(v.ContHW, x*50, y*50)
					v.Haut = True
				if A<90 and v.Collision[int(A+10)] !=3:
					if v.Design == 1:
						image(v.ContB, x*50, y*50)
					if v.Design == 2:
						image(v.ContBW, x*50, y*50)
					v.Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and v.Collision[int(A-1)] != 3:
					if v.Design == 1:
						image(v.ContG, x*50, y*50)
					if v.Design == 2:
						image(v.ContGW, x*50, y*50)
					v.Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and v.Collision[int(A+1)] != 3:
					if v.Design == 1:
						image(v.ContD, x*50, y*50)
					if v.Design == 2:
						image(v.ContDW, x*50, y*50)
					v.Droite = True

	        #Coins/angles lave
				if v.Haut == True and v.Droite == True and v.Design == 1:
					image(v.ContHD, x*50, y*50)
				if v.Haut == True and v.Gauche == True and v.Design == 1:
					image(v.ContHG, x*50, y*50)
				if v.Bas == True and v.Droite == True and v.Design == 1:
					image(v.ContBD, x*50, y*50)
				if v.Bas == True and v.Gauche == True and v.Design == 1:
					image(v.ContBG, x*50, y*50)

				if v.Haut == True and v.Droite == True and v.Design == 2:
					image(v.ContHDW, x*50, y*50)
				if v.Haut == True and v.Gauche == True and v.Design == 2:
					image(v.ContHGW, x*50, y*50)
				if v.Bas == True and v.Droite == True and v.Design == 2:
					image(v.ContBDW, x*50, y*50)
				if v.Bas == True and v.Gauche == True and v.Design == 2:
					image(v.ContBGW, x*50, y*50)

				#Remise a 0 de la détection des tiles autours du blocs de lave
				v.Bas = False
				v.Haut = False
				v.Droite = False
				v.Gauche = False
				#Couleur Lave

			#Foret/arbre en bas pour recouvrir les tank
			if v.Collision[int(A)] == 4 and v.Design == 1:
				image(v.arbre, x*50, y*50)
			if v.Collision[int(A)] == 4 and v.Design == 2:
				image(v.arbreW, x*50, y*50)
			#Couleur Foret

	#Affichage dégats lave
	if v.DegatsLaveTank == True:
		fill(255, 0, 0, 100)
		rect(0, 0, 500, 500)

	#Selection entourage tank
	if v.Player == 1:
		image(v.STank1, v.xbase, v.ybase)
	if v.Player == 2:
		image(v.STank2, v.xbase2,v. ybase2)

	#Affichage Tank
	if v.Collision[int(v.xbase/50+v.ybase/50*10)] == 4 and v.Design == 2:
		pass
	else:
		if v.Direction == 1:
			Tank1 = v.Tank1u 
			image(Tank1, v.xbase, v.ybase)
		if v.Direction == 2:
			Tank1 = v.Tank1d 
			image(Tank1, v.xbase, v.ybase)
		if v.Direction == 3:
			Tank1 = v.Tank1l 
			image(Tank1, v.xbase, v.ybase)
		if v.Direction == 4:
			Tank1 = v.Tank1r 
			image(Tank1, v.xbase, v.ybase)

	if v.Collision[int(v.xbase2/50+v.ybase2/50*10)] == 4 and v.Design == 2:
		pass
	else:
		if v.Direction2 == 1:
			Tank2 = v.Tank2u 
			image(Tank2, v.xbase2, v.ybase2)
		if v.Direction2 == 2:
			Tank2 = v.Tank2d 
			image(Tank2, v.xbase2, v.ybase2)
		if v.Direction2 == 3: 
			Tank2 = v.Tank2l 
			image(Tank2, v.xbase2, v.ybase2)
		if v.Direction2 == 4:
			Tank2 = v.Tank2r 
			image(Tank2, v.xbase2, v.ybase2)

	#Affichage des vies
	fill(255)
	textSize(14)
	text("V1:", 20, 530)
	text(":V2", 460, 530)
	for viebarre1 in range(v.vietank1):
		fill(150, 32, 32)
		image(v.Vies, 12*viebarre1+40, 523, 8, 8)
	for viebarre2 in range(v.vietank2):
		fill(150, 32, 32)
		image(v.Vies, -12*viebarre2+460, 523, 8, 8)

	#Affichage de la Commande pour accéder aux options en jeu
	textAlign("CENTER")
	fill(255)
	text("Press Shift", 250, 520)
	text("For Options", 250, 540)
	textAlign("LEFT")

def Compteur():
	if v.ComptTimer >= 60 : #S'il s'est écoulé une minute
		v.ComptTimer = 0
		v.TimerSec -= 1         #Réduire le timer d'une seconde
		if v.TimerSec == -1:    #Si une minute s'est écoulée
			v.TimerSec = 59     #Remettre les secondes par défaut
			v.TimerMin -= 1     #Réduire les minutes

def MusicBackground():
	# MusicBackground.amp(float(v.MusicVOL)/1000) #Volume du son
	v.DecompteMusique -= 1
	if v.DecompteMusique < 0 or v.DecompteMusique == 19 * 60: #Boucle musique de fond
		# MusicBackground.play()
		v.DecompteMusique = 19*60

def Reset():
	v.vietank1 = v.DefaultVie
	v.vietank2 = v.DefaultVie
	v.xbase = 0
	v.ybase = 0
	v.xbase2 = 450
	v.ybase2 = 450
	v.Menu = 1
	v.Player = 0
	v.TimerSec = v.DefaultSec
	v.TimerMin = v.DefaultMin
	v.Winner = 0
	v.toshow = "Menu"

def Game():
	# print(v.WhoIAm, v.Player, v.Act, v.Player1IG, v.Player2IG)

	if v.Act == 0:
		v.Act = 3
		v.Player1IG = False
		v.Player2IG = False
		v.Player += 1
		if v.Player > 2:
			v.Player = 1
	v.ComptTimer += 1
	Compteur() #Ajouter du temps au compteur dès que nous somme en jeu
	# Move.amp((float)SoundVOL/1000)
	# Fire.amp((float)SoundVOL/1000)
	textAlign("LEFT")
	if v.IsMulti == False or v.IsMulti == True and v.state == 'ingame' and v.WhoIAm == 1:
		if v.Player == 1 and v.Act == 3 and v.Player1IG == False and v.vietank1 > 0 and v.vietank2 > 0:
			background(0)
			# stroke(0)
			fill(0, 0, 255)
			textSize(40)
			text("Player 1", 160, 220)
			text("Press Down", 130, 270)
			if v.keyCode == pygame.K_DOWN:
				v.Player1IG = True
				# v.Player = 1
				# v.Act = 3
				v.MaxDepl = 0
				v.needed = 1

	if v.IsMulti == False or v.IsMulti == True and v.state == 'ingame' and v.WhoIAm == 2:
		print('step 1', v.Player, v.Act, v.Player2IG, v.vietank1, v.vietank2)
		if v.Player == 2 and v.Act == 3 and v.Player2IG == False and v.vietank1 > 0 and v.vietank2 > 0:
			# print('step 2')
			background(0)  
			fill(255, 0, 0)
			textSize(40)
			text("Player 2", 160, 220)
			text("Press Down", 130, 270)
			if v.IA == False and v.keyCode == pygame.K_DOWN or v.IA == True:
				v.Player2IG = True
		print('step 1', v.Player, v.Act, v.Player2IG, v.vietank1, v.vietank2)
  #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	if v.Winner == 0 and (v.IsMulti == False or v.IsMulti == True and (v.WhoIAm == 1 and v.Player == 1 or v.WhoIAm == 2 and v.Player == 2)):
		if v.Act > 0 and ((v.Player == 1 and v.Player1IG == True) or (v.Player == 2 and v.Player2IG == True)):

			AffTank()

			if v.choix == 0: #Choix des actions (Left = Shoot / Right = Move)
				if v.IA == False or v.IA == True and v.Player == 1: #Si nous sommes en 1v1 contre l'IA et que c'est à nous de jouer

					if v.keyCode == pygame.K_LEFT:#Lorsque le curseur est sur Shoot
						v.choix2 = 1
						v.choix3 = 1
					if v.keyCode == pygame.K_RIGHT: #Lorsque le curseur est sur Move
						v.choix2 = 2
						v.choix3 = 1
					if v.choix3 == 1 and v.keyCode == pygame.K_RETURN: #Lorsque l'action est choisie par Enter
						v.choix = v.choix2
						v.choix3 = 0


					#Affichage du choix des Actions (shoot ou move)
					
					fill(0)
					rect(0, 175, 500, 140)
					fill(255)
					rect(0, 172, 500, 3)
					rect(0, 315, 500, 3)
					fill(100)
					if v.choix2 == 1: #Met en surbrillance le choix Left
						rect(50, 227, 185, 30)
					if v.choix2 == 2: #Met en surbrillance le choix Right
						rect(270, 227, 190, 30)

					textAlign("CENTER")
					textSize(45)
					fill(255, 255, 255, 200)
					ellipse(480, 190, 15, 15)
					if v.Player == 1:
						fill(0, 0, 255)
					if v.Player == 2:
						fill(255, 0, 0)
					ellipse(480-1, 190-1, 12, 12)

					textSize(23)
					fill(250, 250, 250, 255)
					text("Left(for Attack)     Right(for move)", 250, 250)
					fill(255)
					textSize(20)
					text("Press arrow", 250, 200)
					text("And then press Enter", 250, 300)
					textAlign("LEFT")
				elif v.IA == True and v.Player == 2:
					v.choix = IA("choix") #Si nous jouons contre l'IA et que c'est à elle de jouer, nous lui demandons son choix

			if v.choix == 1: #Shoot

				if v.CB < 1 or v.lock == 0:
					v.CB = int(random(0, 10))
					# println(CB)
					if v.Player == 1:
						v.DistFeu1 = v.CB
						v.xbasem = v.xbase
						v.ybasem = v.ybase
					if v.Player == 2:
						v.DistFeu2 = v.CB
						v.xbasem = v.xbase2
						v.ybasem = v.ybase2

					AffTank()

					if v.IsMulti == False or v.IsMulti == True and (v.WhoIAm == 1 and v.Player == 1 or v.WhoIAm == 2 and v.Player == 2) or v.IA == True and v.Player == 1:
						fill(200)
						textSize(20)
						text("Press arrows to shoot your bullet in a direction", 30, 430)
						text("Then press Enter", 180, 480)

					if v.IA == True and v.Player == 2:
						v.Direction2 = IA("shoot") #Si nous jouons contre l'IA, elle décide dans quelle direction elle veut tirer

					if v.IA == False and v.keyCode == pygame.K_UP or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_UP or v.Player == 2 and v.Direction2 == 1):
						v.lock2 = 1
						v.lock3 = 1
						if v.Player == 1:
							triangle(v.xbase+10, v.ybase-10, v.xbase+40, v.ybase-10, v.xbase+25, v.ybase-30)
							v.Direction = 1
						if v.Player == 2:
							triangle(v.xbase2+10, v.ybase2-10, v.xbase2+40, v.ybase2-10, v.xbase2+25, v.ybase2-30)
							Direction2 = 1
					if v.IA == False and v.keyCode == pygame.K_DOWN or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_DOWN or v.Player == 2 and v.Direction2 == 2):
						v.lock2 = 2
						v.lock3 = 1
						if v.Player == 1:
							triangle(v.xbase+10, v.ybase+60, v.xbase+40, v.ybase+60, v.xbase+25, v.ybase+80)
							v.Direction = 2
						if v.Player == 2:
							triangle(v.xbase2+10, v.ybase2+60, v.xbase2+40, v.ybase2+60, v.xbase2+25, v.ybase2+80)
							v.Direction2 = 2
					if v.IA == False and v.keyCode == pygame.K_LEFT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_LEFT or v.Player == 2 and v.Direction2 == 3):
						v.lock2 = 3
						v.lock3 = 1
						if v.Player == 1:
							triangle(v.xbase-10, v.ybase+10, v.xbase-10, v.ybase+40, v.xbase-30, v.ybase+25)
							v.Direction = 3
						if v.Player == 2:
							triangle(v.xbase2-10, v.ybase2+10, v.xbase2-10, v.ybase2+40, v.xbase2-30, v.ybase2+25)
							v.Direction2 = 3
					if v.IA == False and v.keyCode == pygame.K_RIGHT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_RIGHT or v.Player == 2 and v.Direction2 == 4):
						v.lock2 = 4
						v.lock3 = 1
						if v.Player == 1:
							triangle(v.xbase+60, v.ybase+10, v.xbase+60, v.ybase+40, v.xbase+80, v.ybase+25)
							v.Direction = 4
						if v.Player == 2:
							triangle(v.xbase2+60, v.ybase2+10, v.xbase2+60, v.ybase2+40, v.xbase2+80, v.ybase2+25)
							v.Direction2 = 4
					if v.lock3 == 1 and (v.IA == False and v.keyCode == pygame.K_RETURN or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_RETURN or v.Player == 2 and v.IsFire2 == 1)):
						# Fire.play(3)
						v.lock = v.lock2
						v.lock3 = 0
						if v.Player == 1:
							v.IsFire1 = 1
						if v.Player == 2:
							v.IsFire2 = 1

				if v.CB > 0 and v.lock != 0:

					v.CB -= 1
					AffTank()
					if v.lock == 1:
						v.ybasem -= 50
						CDA()
						Balle = v.BalleU
						image(Balle, v.xbasem, v.ybasem)
					if v.lock == 2:
						v.ybasem += 50
						CDA()
						Balle = v.BalleD
						image(Balle, v.xbasem, v.ybasem)
					if v.lock == 3:
						v.xbasem -= 50
						CDA()
						Balle = v.BalleL
						image(Balle, v.xbasem, v.ybasem)
					if v.lock == 4:
						v.xbasem += 50
						CDA()
						Balle = v.BalleR
						image(Balle, v.xbasem, v.ybasem)
					if v.Player == 1 and v.xbasem == v.xbase2 and v.ybasem == v.ybase2:
						v.CB = 0
						v.vietank2 -= 1
					if v.Player == 2 and v.xbasem == v.xbase and v.ybasem == v.ybase:
						v.CB = 0
						v.vietank1 -= 1

					fill(200)
					textSize(50)
					text(v.CB, 450, 490)

				if v.CB < 1 and v.lock != 0:
					v.choix = 0
					v.lock = 0
					AffTank()
					Balle = v.BalleExplosion
					image(Balle, v.xbasem, v.ybasem)
					v.Act -= 1
					v.ChangementSaison += 1


			if v.choix == 2: #Move
				#Initialisation du dès de déplacements
				if v.CP < 1:
					v.CP = int(random(0, 10))
					v.CP = 20

				#Déplacements lorsque CP est différent de 0 (Joueur a encore des déplacements)
				if v.CP > 0:
					if v.IA == True and v.Player == 2:
						v.Direction2 = IA("move") #Si nous jouons contre l'IA, elle décide dans quelle direction elle veut se déplacer

					if v.IA == False and v.keyCode == pygame.K_UP or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_UP or v.Player == 2 and v.Direction2 == 1):
						v.CP -= 1
						if v.Player == 1:
							v.ybase -= 50
							CDD()
							v.Direction = 1
						if v.Player == 2:
							v.ybase2 -= 50
							CDD2()
							v.Direction2 = 1
						# Move.play()
					if v.IA == False and v.keyCode == pygame.K_DOWN or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_DOWN or v.layer == 2 and v.Direction2 == 2):
						v.CP -= 1
						if v.Player == 1:
							v.ybase += 50
							CDD()
							v.Direction = 2
						if v.Player == 2:
							v.ybase2 += 50
							CDD2()
							v.Direction2 = 2
						# Move.play()
					if v.IA == False and v.keyCode == pygame.K_LEFT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_LEFT or v.Player == 2 and v.Direction2 == 3):
						v.CP -= 1
						if v.Player == 1:
							v.xbase -= 50
							CDD()
							v.Direction = 3
						if v.Player == 2:
							v.xbase2 -= 50
							CDD2()
							v.Direction2 = 3
						# Move.play()
					if v.IA == False and v.keyCode == pygame.K_RIGHT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_RIGHT or v.Player == 2 and v.Direction2 == 4):
						v.CP -= 1
						if v.Player == 1:
							v.xbase += 50
							CDD()
							v.Direction = 4
						if v.Player == 2:
							v.xbase2 += 50
							CDD2()
							v.Direction2 = 4
						# Move.play()

					if v.TestCadriD == 0 and (v.IA == False and v.keyCode == pygame.K_UP or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_UP or v.Player == 2 and v.Direction2 == 1)):
						if v.Player == 1:
							v.ybase += 50
						if v.Player == 2:
							v.ybase2 += 50
						v.CP += 1
						v.TestCadriD = 1
					if v.TestCadriD == 0 and (v.IA == False and v.keyCode == pygame.K_DOWN or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_DOWN or v.Player == 2 and v.Direction2 == 2)):
						if v.Player == 1:
							v.ybase -= 50
						if v.Player == 2:
							v.ybase2 -= 50
						v.CP += 1
						v.TestCadriD = 1
					if v.TestCadriD == 0 and (v.IA == False and v.keyCode == pygame.K_LEFT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_LEFT or v.Player == 2 and v.Direction2 == 3)):
						if v.Player == 1:
							v.xbase += 50
						if v.Player == 2:
							v.xbase2 += 50
						v.CP += 1
						v.TestCadriD = 1
					if v.TestCadriD == 0 and (v.IA == False and v.keyCode == pygame.K_RIGHT or v.IA == True and (v.Player == 1 and v.keyCode == pygame.K_RIGHT or v.Player == 2 and v.Direction2 == 4)):
						if v.Player == 1:
							v.xbase -= 50
						if v.Player == 2:
							v.xbase2 -= 50
						v.CP += 1
						v.TestCadriD = 1

					AffTank()
					fill(200)

					textSize(50)
					text(v.CP, 450, 490)
# 
				#Déplacements lorsque CP est inférieur à 1 (Joueur n'a plus de déplacements)
				if v.CP < 1:
					v.choix = 0
					v.Act -= 1
					v.ChangementSaison += 1

	if v.IsMulti == True and ((v.WhoIAm == 1 and v.Player == 2) or (v.WhoIAm == 2 and v.Player == 1)):
		AffTank()

	if v.TimerMin <= -1 and v.vietank1 < v.vietank2 or v.vietank1 < 1: #Détéction de victoire (fin de timer / plus de vie)
		background(0)
		fill(255, 0, 0)
		textSize(40)
		textAlign("CENTER")
		text("Player 2 WIN", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		v.Winner = 2
	if v.TimerMin <= -1 and v.vietank2 < v.vietank1 or v.vietank2 < 1:
		background(0)
		fill(0, 0, 255)
		textSize(40)
		textAlign("CENTER")
		text("Player 1 WIN", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		v.Winner = 1
	if v.TimerMin <= -1 and v.vietank1 == v.vietank2: #Egalité
		background(0)
		fill(255, 0, 255)
		textSize(40)
		textAlign("CENTER")
		text("EQUALITY", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		v.Winner = -1

	if v.Design == 1 and v.Changementok == True and v.ChangementSaison == v.SummerDay:
		v.Design = 2
		v.ChangementSaison = 0
	if v.Design == 2 and v.Changementok == True and v.ChangementSaison == v.WinterDay:
		v.Design = 1
		v.ChangementSaison = 0
	if v.Design > 2:
		v.Design=1
	if v.Winner == 0:
		textAlign("RIGHT")
		textSize(15)
		fill(255)
		text(str(v.TimerMin)+":"+str(v.TimerSec), v.width-10, 20)

	if v.IsMulti == True:
		v.toshow = 'Multiplayer'


while MainGameMaster == True:

	# MusicBackground() # On charge la musique du jeu

	# Ici, on appelle le void qu'il faut en fonction de ce qu'on veut afficher
	
	MenuMain() if v.toshow == "Menu" else ''
	MenuPlay() if v.toshow == "MenuPlay" else ''
	MenuEditor() if v.toshow == "MenuEditor" else ''
	Game() if v.toshow == "Game" else ''
	Reset() if v.toshow == "Reset" else ''
	ServerJoin() if v.toshow == "ServerJoin" else ''
	Multiplayer() if v.toshow == "Multiplayer" else ''
	MenuMaps() if v.toshow == "MenuMaps" else ''
	Options() if v.toshow == "Options" else ''
	Credits() if v.toshow == "Credits" else ''


	pygame.display.flip() # Acualisation de la page

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			MainGameMaster = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				MainGameMaster = False
			else:
				keyPressed(event.key, event.unicode) # On verifie si une touche a été appuyée
		if event.type == pygame.KEYUP:
			v.keyCode = 0
pygame.quit()