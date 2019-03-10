import os, pygame
import ProcToPy, Credits, Getkey, IA, Menu, MenuEditeur, MenuMaps, Options # Charger les autres fenêtres 


MainGameMaster = True

Player = 0 #Joueur 1 et 2 changement
Act = 0
xbase = 0 #Emplacement tank 1 (0, 0)
ybase = 0
xbase2 = 450 #Emplacement tank 2 (450, 450)
ybase2 = 450
DefaultVie = 5 #Vie des tanks par défaut
vietank1 = DefaultVie #Vie des tanks
vietank2 = DefaultVie
Direction = 2 #Direction des sprites des tanks
Direction2 = 2
CP = 0 #Compteur Placement
turn = 0 #Un décompte de random éffectué
arrows = 0 #Empèche le joueur de maintenir les flèches pour se déplacer ( un appui = un déplacement )
choix = 0 #Validation Choix
choix2 = 0 #Choix entre Attaque ou Déplacement
choix3 = 0 #Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
xbasem = 0 # Emplacement balle
ybasem = 0
CB = 0 #Compteur Balle
MLock = 0
lock = 0 #touche de tire vérouillée
lock2 = 0 #direction du tir
lock3 = 0 #Anti Enter*2 ( effet d'un key pressed pour enter car non ascii)
TestCadriD = 0 #Test cadrillage renvoie 0 ou 1 => Si on peux passer ou pas
TD2 = 0 
Bas = False #Variable détectant si plusieurs bord existes pour un angle (texture)
Haut = False
Droite = False
Gauche = False
end = False
toshow = "Menu"
Menu = 1
bord = False
DegatsLaveTank = False
ChangementSaison = 0
Changementok = False 

# Parties valeurs MenuEditeur
Selectile = 0
Selectedtile = 0
LockTile = 0
XCursorEdit = 0
YCursorEdit = 0

#MenuMaps
# JSONObject Map1
# JSONObject Map2
# JSONObject Map3

InteracMap = 0 #Interac(tion)Map permet de définir s'il s'agit d'une lecture (0) ou d'une écriture de map
SelectMap = 1 #Annonce quelle map est sélectione

#Menu option
MenuOpt = 0
SMenuOpt = 1
MusicVOL = 1 #  <---------------------------------------------------------------------
SoundVOL = 50
TSel = 1
TypeDeSon = 1
Design = 1
SummerDay = 1 
WinterDay = 1 
DefaultMin = 5
DefaultSec = 0
Link = 0 #Permet d'accéder au parametres de son en jeu

TimerSec = DefaultSec
TimerMin = DefaultMin
ComptTimer = 0

#MusicBackground
FrameRate = 60
DecompteMusique = 19 * 60 + 1

#Maps de base lorsqu'on édite une map dans le menu editeur
#Collision = {
#  0, 2, 2, 4, 4, 0, 0, 1, 1, 3, 
#  0, 2, 2, 2, 4, 4, 0, 0, 0, 3, 
#  0, 1, 2, 2, 0, 0, 0, 3, 0, 0, 
#  0, 1, 2, 2, 2, 0, 0, 0, 1, 1, 
#  0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 
#  1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 
#  1, 1, 0, 0, 0, 2, 2, 2, 1, 0, 
#  0, 0, 3, 0, 0, 0, 2, 2, 1, 0, 
#  3, 0, 0, 0, 4, 4, 2, 2, 2, 0, 
#  3, 1, 1, 0, 0, 4, 4, 2, 2, 0
#}
Collision = {
  0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0
}


# import processing.sound.*
# SoundFile Fire
# SoundFile Move
# SoundFile MusicBackground

pygame.init()
screen = pygame.display.set_mode((500, 550)) # Définir la taille de l'écran

#Chargement des images du jeu
BackgMenu = pygame.image.load("data/BackMenu.png").convert_alpha()
BackOpt = pygame.image.load("data/Options.png").convert_alpha()
Credits = pygame.image.load("data/Crédits.png").convert_alpha()

arbre = pygame.image.load("data/arbre.png").convert_alpha()
Montagne = pygame.image.load("data/Montagne.png").convert_alpha()
Eau = pygame.image.load("data/Eau.png").convert_alpha()
Lave = pygame.image.load("data/Lave.png").convert_alpha()
ContH = pygame.image.load("data/Lavehaut.png").convert_alpha()
ContB = pygame.image.load("data/Lavebas.png").convert_alpha()
ContG = pygame.image.load("data/Lavegauche.png").convert_alpha()
ContD = pygame.image.load("data/Lavedroite.png").convert_alpha()
ContHD = pygame.image.load("data/Lavehaut+droite.png").convert_alpha()
ContHG = pygame.image.load("data/Lavehaut+gauche.png").convert_alpha()
ContBD = pygame.image.load("data/Lavebas+droite.png").convert_alpha()
ContBG = pygame.image.load("data/Lavebas+gauche.png").convert_alpha()

arbreW = pygame.image.load("data/arbreW.png").convert_alpha()
MontagneW = pygame.image.load("data/MontagneW.png").convert_alpha()
EauW = pygame.image.load("data/EauW.png").convert_alpha()
LaveW = pygame.image.load("data/LaveW.png").convert_alpha()
ContHW = pygame.image.load("data/LavehautW.png").convert_alpha()
ContBW = pygame.image.load("data/LavebasW.png").convert_alpha()
ContGW = pygame.image.load("data/LavegaucheW.png").convert_alpha()
ContDW = pygame.image.load("data/LavedroiteW.png").convert_alpha()
ContHDW = pygame.image.load("data/Lavehaut+droiteW.png").convert_alpha()
ContHGW = pygame.image.load("data/Lavehaut+gaucheW.png").convert_alpha()
ContBDW = pygame.image.load("data/Lavebas+droiteW.png").convert_alpha()
ContBGW = pygame.image.load("data/Lavebas+gaucheW.png").convert_alpha()

STank1 = pygame.image.load("data/Selection Tank1.png").convert_alpha()
STank2 = pygame.image.load("data/Selection Tank2.png").convert_alpha()
Tank1 = pygame.image.load("data/Tank1u.png").convert_alpha()
Tank1u = pygame.image.load("data/Tank1u.png").convert_alpha()
Tank1d = pygame.image.load("data/Tank1d.png").convert_alpha()
Tank1r = pygame.image.load("data/Tank1r.png").convert_alpha()
Tank1l = pygame.image.load("data/Tank1l.png").convert_alpha()
Tank2 = pygame.image.load("data/Tank2d.png").convert_alpha()
Tank2u = pygame.image.load("data/Tank2u.png").convert_alpha()
Tank2d = pygame.image.load("data/Tank2d.png").convert_alpha()
Tank2r = pygame.image.load("data/Tank2r.png").convert_alpha()
Tank2l = pygame.image.load("data/Tank2l.png").convert_alpha()
Vies = pygame.image.load("data/Vies.png").convert_alpha()
BalleU = pygame.image.load("data/BalleU.png").convert_alpha()
BalleD = pygame.image.load("data/BalleD.png").convert_alpha()
BalleR = pygame.image.load("data/BalleR.png").convert_alpha()
BalleL = pygame.image.load("data/BalleL.png").convert_alpha()
BalleExplosion = pygame.image.load("data/Explosion.png").convert_alpha()

while MainGameMaster == True:
	ProcToPy.image(BackgMenu, screen, 0, 0)

	# Getkey.keyPressed() # On verifie si une touche a été appuyée
	# MusicBackground() # On charge la musique du jeu

	# Ici, on appelle le void qu'il faut en fonction de ce qu'on veut afficher
	'''
	if toshow == "Menu":
		Menu.Menu()
	if toshow == "MenuPlay":
		Menu.MenuPlay()
	if toshow == "MenuEditor":
		MenuEditeur.MenuEditor()
	if toshow == "Game":
		Game()
	# if toshow == "ServerJoin":
	# 	ServerJoin()
	# if toshow == "ServerCreate":
	# 	ServerCreate()
	if toshow == "MenuMaps":
		MenuMaps.MenuMaps()
	if toshow == "Options":
		Options.Options()
	if toshow == "Credits":
		Credits.Credits()
'''
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			MainGameMaster = False
	pygame.display.flip() # Acualisation de la page
pygame.quit()

def CDD():
	# Cadrillage Des Déplacements (Tanks)
	CDDx = xbase/50
	CDDy = ybase/50*10
	CDD = CDDx + CDDy
	# Permet de fixer des limites pour la glisse sur la glace
	bord = False

	# Colisions cotés de terrain (Déplacements), si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
	if CDDx < 0:
		CDD += 1
		xbase += 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDy < 0:
		CDD += 10
		ybase += 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDx > 9:
		CDD -= 1
		xbase -= 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDy > 90:
		CDD -= 10
		ybase += 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	# Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if Collision[CDD] == 1:
		TestCadriD = 0
		TD2 = 1
	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
	if Collision[CDD] == 3 and Design == 1:
		TestCadriD=0
		TD2=1
	if Collision[CDD] == 3 and Design == 2:
		TestCadriD = 1
		TD2 = 1
		vietank1 -= 1
		DegatsLaveTank = True
	else:
		DegatsLaveTank = False
	#Si le tank va dans l'eau (Il est alors ralenti)
	if Collision[CDD] == 2 and Design == 1:
		CP=CP-1
	#Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
	if Collision[CDD] == 2 and Design == 2:

		while Collision[CDD] == 2 and keyCode==RIGHT and bord == False:
			xbase += 50
			if xbase <= 450:
				CDDx = xbase/50
			else:
				bord = True 
				xbase -= 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				xbase -= 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==LEFT and bord == False:
			xbase -= 50
			if xbase >= 0:
				CDDx = xbase/50
			else:
				bord = True 
				xbase += 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				xbase += 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==UP and bord == False:
			ybase -= 50
			if ybase >= 0:
				CDDy = ybase/50*10
			else:
				bord = True 
				ybase += 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				ybase += 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==DOWN and bord == False:
			ybase += 50
			if ybase <= 450:
				CDDy = ybase/50*10
			else:
				bord = True 
				ybase -= 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				ybase -= 50
			AffTank()

def CDD2():
	#Cadrillage Des Déplacements (Tanks)
	CDDx = xbase2/50
	CDDy = ybase2/50*10
	CDD = CDDx + CDDy
	#Permet de fixer les bug sur les déplacements avec la glace
	bord = False

	#Colisions cotés de terrain (Déplacements), si le tank rencontre la limite et qu'il se trouve sur de l'eau CP a besoin de +2 pour revenir a son etat initial
	if CDDx < 0:
		CDD += 1
		xbase2 += 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDy < 0:
		CDD += 10
		ybase2 += 50
		CP+= 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDx > 9: 
		CDD -= 1
		xbase2 -= 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1
	if CDDy > 90:
		CDD -= 10
		ybase2 -= 50
		CP += 1
		if Collision[CDD] == 2:
			CP += 1

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if Collision[CDD] == 1:
		TestCadriD = 0
		TD2 = 1

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Lave)
	if Collision[CDD] == 3 and Design == 1:
		TestCadriD = 0
		TD2 = 1

	if Collision[CDD] == 3 and Design == 2:
		TestCadriD = 1
		TD2 = 1
		vietank2 -= 1
		DegatsLaveTank = True
	else:
		DegatsLaveTank = False
	#Si le tank va dans l'eau (Il est alors ralenti)
	if Collision[CDD] == 2 and Design == 1:
		CP -= 1
	#Si le Tank va sur la glace (Il glisse jusqu'à un rebord ou un terrain différent de la glace)
	if Collision[CDD] == 2 and Design == 2:

		while Collision[CDD] == 2 and keyCode==RIGHT and bord == False:
			xbase2 += 50
			if xbase2 <= 450:
				CDDx = xbase2/50
			else:
				bord = True 
				xbase2 -= 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				xbase2 -= 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==LEFT and bord == False:
			xbase2 -= 50
			if xbase2 >= 0:
				CDDx = xbase2/50
			else:
				bord = True 
				xbase2 += 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				xbase2 += 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==UP and bord == False:
			ybase2 -= 50
			if ybase2 >= 0:
				CDDy = ybase2/50*10
			else:
				bord = True 
				ybase2 += 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				ybase2 += 50
			AffTank()

		while Collision[CDD] == 2 and keyCode==DOWN and bord == False:
			ybase2 += 50
			if ybase2 <= 450:
				CDDy = ybase2/50*10
			else:
				bord = True 
				ybase2 -= 50
			CDD = CDDx + CDDy
			if Collision[CDD] == 1:
				bord = True
				ybase2 -= 50
			AffTank()

def CDA():
	#Cadrillage Des Attaques (Bullets)
	CDAx = xbasem / 50
	CDAy = ybasem / 50 * 10
	CDA = CDAx + CDAy

	#Colisions cotés de terrain (Attaque)
	if CDAx < 0:
		CDA += 1
		CB = 0
	if CDAy < 0:
		CDA += 10
		CB = 0
	if CDAx > 9:
		CDA -= 1
		CB = 0
	if CDAy > 90:
		CDA -= 10
		CB = 0

	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Montagne)
	if Collision[CDA] == 1:
		CB=0
	if Collision[CDA] == 1 and Design==2:
		Collision[CDA] = 0
	#Si le tank veux aller dans un endroit qu'il ne peux traverser (Foret)
	if Collision[CDA] == 4:
		CB=0


def AffTank(): #Affiche le tank
	delay(50)
	if Design == 1:
		background(45, 139, 97)
	if Design == 2:
		background(196, 247, 255)
	#Affichage barre d'info
	fill(0)
	rect(0, 500, 500, 50)
	fill(200)
	rect(0, 500, 500, 3)
	noStroke()

	for x in range(10):
		for y in range(10):
			Ax = x
			Ay = y * 10
			A = Ax + Ay
			if Collision[A] == 1 and Design==1:
				ProcToPy.image(Montagne, screen, x*50, y*50)
			if Collision[A] == 1 and Design==2:
				ProcToPy.image(MontagneW, screen, x*50, y*50)
			#Couleur Roche
			if Collision[A] == 2:
				#Eau
				if Design == 1:
					ProcToPy.image(Eau, screen, x*50, y*50)
				if Design == 2:
					ProcToPy.image(EauW, screen, x*50, y*50)
				#rebors eau
				if A>10 and Collision[A-10] !=2:
					if Design == 1:
						ProcToPy.image(ContH, screen, x*50, y*50)
					if Design == 2:
						ProcToPy.image(ContHW, screen, x*50, y*50)
					Haut = True
				if A<90 and Collision[A+10] !=2:
					if Design == 1:
						ProcToPy.image(ContB, screen, x*50, y*50)
					if Design == 2:
						ProcToPy.image(ContBW, screen, x*50, y*50)
					Bas = True
				if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and Collision[A-1] !=2:
					if Design == 1:
						ProcToPy.image(ContG, screen, x*50, y*50)
					if Design == 2:
						ProcToPy.image(ContGW, screen, x*50, y*50)
					Gauche = True
				if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and Collision[A+1] !=2:
					if Design == 1:
						ProcToPy.image(ContD, screen, x*50, y*50)
					if Design == 2:
						ProcToPy.image(ContDW, screen, x*50, y*50)
					Droite = True
		#Coins/angles lave
		#Eté
		if Haut == True and Droite == True and Design == 1:
			ProcToPy.image(ContHD, screen, x*50, y*50)
		if Haut == True and Gauche == True and Design == 1:
			ProcToPy.image(ContHG, screen, x*50, y*50)
		if Bas == True and Droite == True and Design == 1:
			ProcToPy.image(ContBD, screen, x*50, y*50)
		if Bas == True and Gauche == True and Design == 1:
			ProcToPy.image(ContBG, screen, x*50, y*50)

		if Haut == True and Droite==True and Design == 2:
			ProcToPy.image(ContHDW, screen, x*50, y*50)
		if Haut == True and Gauche==True and Design == 2:
			ProcToPy.image(ContHGW, screen, x*50, y*50)
		if Bas == True and Droite==True and Design == 2:
			ProcToPy.image(ContBDW, screen, x*50, y*50)
		if Bas == True and Gauche==True and Design == 2:
			ProcToPy.image(ContBGW, screen, x*50, y*50)

		#Remise a 0 de la détection des tiles autours du blocs de lave
		Bas = False
		Haut = False
		Droite = False
		Gauche = False

		if Collision[A] == 3:
			#Lave
			if Design == 1:
				ProcToPy.image(Lave, screen, x*50, y*50)
			if Design == 2:
				ProcToPy.image(LaveW, screen, x*50, y*50)
			#rebors lave
			if A>10 and Collision[A-10] != 3:
				if Design == 1:
					ProcToPy.image(ContH, screen, x*50, y*50)
				if Design == 2:
					ProcToPy.image(ContHW, screen, x*50, y*50)
				Haut=True
			if A<90 and Collision[A+10] !=3:
				if Design == 1:
					ProcToPy.image(ContB, screen, x*50, y*50)
				if Design == 2:
					ProcToPy.image(ContBW, screen, x*50, y*50)
				Bas = True
			if A!=0 and A!=10 and A!=20 and A!=30 and A!=40 and A!=50 and A!=60 and A!=70 and A!=80 and A!=90 and Collision[A-1] != 3:
				if Design == 1:
					ProcToPy.image(ContG, screen, x*50, y*50)
				if Design == 2:
					ProcToPy.image(ContGW, screen, x*50, y*50)
				Gauche = True
			if A!=9 and A!=19 and A!=29 and A!=39 and A!=49 and A!=59 and A!=69 and A!=79 and A!=89 and A!=99 and Collision[A+1] != 3:
				if Design == 1:
					ProcToPy.image(ContD, screen, x*50, y*50)
				if Design == 2:
					ProcToPy.image(ContDW, screen, x*50, y*50)
				Droite = True

        #Coins/angles lave
			if Haut == True and Droite == True and Design == 1:
				ProcToPy.image(ContHD, screen, x*50, y*50)
			if Haut == True and Gauche == True and Design == 1:
				ProcToPy.image(ContHG, screen, x*50, y*50)
			if Bas == True and Droite == True and Design == 1:
				ProcToPy.image(ContBD, screen, x*50, y*50)
			if Bas == True and Gauche == True and Design == 1:
				ProcToPy.image(ContBG, screen, x*50, y*50)

			if Haut == True and Droite == True and Design == 2:
				ProcToPy.image(ContHDW, screen, x*50, y*50)
			if Haut == True and Gauche == True and Design == 2:
				ProcToPy.image(ContHGW, screen, x*50, y*50)
			if Bas == True and Droite == True and Design == 2:
				ProcToPy.image(ContBDW, screen, x*50, y*50)
			if Bas == True and Gauche == True and Design == 2:
				ProcToPy.image(ContBGW, screen, x*50, y*50)

			#Remise a 0 de la détection des tiles autours du blocs de lave
			Bas= False
			Haut= False
			Droite= False
			Gauche= False
			#Couleur Lave

			#Foret/arbre en bas pour recouvrir les tank
			if Collision[A] == 4 and Design == 1:
				ProcToPy.image(arbre, screen, x*50, y*50)
			if Collision[A] == 4 and Design == 2:
				ProcToPy.image(arbreW, screen, x*50, y*50)
			#Couleur Foret

	#Affichage dégats lave
	if DegatsLaveTank == True:
		fill(255, 0, 0, 100)
		rect(0, 0, 500, 500)

	#Selection entourage tank
	if Player == 1:
		ProcToPy.image(STank1, screen, xbase, ybase)
	if Player == 2:
		ProcToPy.image(STank2, screen, xbase2, ybase2)

	#Affichage Tank
	if Collision[xbase/50+ybase/50*10] != 4 and Design != 2:
		if Direction == 1:
			Tank1 = Tank1u 
			ProcToPy.image(Tank1, screen, xbase, ybase)
		if Direction == 2:
			Tank1 = Tank1d 
			ProcToPy.image(Tank1, screen, xbase, ybase)
		if Direction == 3:
			Tank1 = Tank1l 
			ProcToPy.image(Tank1, screen, xbase, ybase)
		if Direction == 4:
			Tank1 = Tank1r 
			ProcToPy.image(Tank1, screen, xbase, ybase)

	if Collision[xbase2/50+ybase2/50*10] != 4 and Design != 2:
		if Direction2 == 1:
			Tank2 = Tank2u 
			ProcToPy.image(Tank2, screen, xbase2, ybase2)
		if Direction2 == 2:
			Tank2 = Tank2d 
			ProcToPy.image(Tank2, screen, xbase2, ybase2)
		if Direction2 == 3: 
			Tank2 = Tank2l 
			ProcToPy.image(Tank2, screen, xbase2, ybase2)
		if Direction2 == 4:
			Tank2 = Tank2r 
			ProcToPy.image(Tank2, screen, xbase2, ybase2)

	#Affichage des vies
	fill(255)
	textSize(14)
	text("V1:", 20, 530)
	text(":V2", 460, 530)
	for viebarre1 in range(vietank1, DefaultVie):
		fill(150, 32, 32)
		ProcToPy.image(Vies, screen, 12*viebarre1+40, 523, 8, 8)
	for viebarre2 in range(vietank2, DefaultVie):
		fill(150, 32, 32)
		ProcToPy.image(Vies, screen, -12*viebarre2+460, 523, 8, 8)

	#Affichage de la Commande pour accéder aux options en jeu
	textAlign(CENTER)
	fill(255)
	text("Press Shift", 250, 520)
	text("For Options", 250, 540)
	textAlign(LEFT)

def Compteur():
	if ComptTimer >= 60 / 20: #S'il s'est écoulé une minute
		ComptTimer = 0
		TimerSec -= 1         #Réduire le timer d'une seconde
		if TimerSec == -1:    #Si une minute s'est écoulée
			TimerSec = 59     #Remettre les secondes par défaut
			TimerMin -= 1     #Réduire les minutes

def MusicBackground():
	# MusicBackground.amp((float)MusicVOL/1000) #Volume du son
	DecompteMusique -= 1
	if DecompteMusique < 0 or DecompteMusique == 19 * 60: #Boucle musique de fond
		# MusicBackground.play()
		DecompteMusique = 19*60

def Reset():
	vietank1 = DefaultVie
	vietank2 = DefaultVie
	xbase = 0
	ybase = 0
	xbase2 = 450
	ybase2 = 450
	Menu = 1
	Player = 0
	TimerSec = DefaultSec
	TimerMin = DefaultMin
	Winner = 0
	toshow = "Menu"

def Game():
	ComptTimer += 1
	Compteur() #Ajouter du temps au compteur dès que nous somme en jeu
	# Move.amp((float)SoundVOL/1000)
	# Fire.amp((float)SoundVOL/1000)
	textAlign(LEFT)
	if IsMulti == False or IsMulti == True and AmIServer == True:
		if Player == 0 and Act == 0 and vietank1 > 0 and vietank2 > 0 or Player == 2 and Act == 0 and vietank1 > 0 and vietank2 > 0:
			background(0)
			stroke(0)
			fill(0, 0, 255)
			textSize(40)
			text("Player 1", 160, 220)
			text("Press Down", 130, 270)
			if keyPressed == True and keyCode == DOWN:
				Player = 1
				Act = 3
				MaxDepl = 0
				needed = 1

	if IsMulti == False or IsMulti == True and AmIClient == True:
		if Player == 1 and Act == 0 and vietank1 > 0 and vietank2 > 0:
			background(0)  
			fill(255, 0, 0)
			textSize(40)
			text("Player 2", 160, 220)
			text("Press Down", 130, 270)
			if IA == False and keyPressed == True and keyCode == DOWN or IA == True:
				Player = 2 
				Act = 3

  #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	if Winner == 0 and (IsMulti == False or IsMulti == True and (AmIServer == True and Player == 1 or AmIClient == True and Player == 2)):
		if Act > 0:

			AffTank()

			if choix == 0: #Choix des actions (Left=Shoot/Right=Move)
				if IA == False or IA == True and Player == 1: #Si nous sommes en 1v1 contre l'IA et que c'est à nous de jouer

					if keyCode == LEFT:#Lorsque le curseur est sur Shoot
						choix2 = 1
						choix3 = 1
						fill(255, 255, 255, 100) #Souligne en rouge le choix Left
						rect(55, 227, 180, 30)

					if keyCode == RIGHT: #Lorsque le curseur est sur Move
						choix2 = 2
						choix3 = 1
						fill(255, 255, 255, 100)#Souligne en rouge le choix Right
						rect(263, 227, 180, 30)

					if choix3 == 1 and keyCode == ENTER: #Lorsque l'action est choisie par Enter
						choix = choix2
						choix3 = 0


					#Affichage du choix des Actions (shoot ou move)
					fill(0, 0, 0, 125)
					rect(0, 175, 500, 140)

					fill(0, 0, 0, 65)
					rect(0, 175+140, 500, 500-(175+140))
					rect(0, 0, 500, 175)

					fill(255, 255, 255, 30)
					rect(0, 175+140, 500, 3)
					rect(0, 172, 500, 3)

					textAlign(CENTER)
					textSize(45)
					fill(255, 255, 255, 200)
					ellipse(480, 190, 15, 15)
					if Player == 1:
						fill(0, 0, 255)
					if Player == 2:
						fill(255, 0, 0)
					ellipse(480, 190, 10, 10)

					textSize(23)
					fill(250, 250, 250, 255)
					text("Left(for Attack)     Right(for move)", 250, 250)
					fill(255)
					textSize(20)
					text("Press arrow", 250, 200)
					text("And then press Enter", 250, 300)
					textAlign(LEFT)
				elif IA == True and Player == 2:
					choix = IA("choix") #Si nous jouons contre l'IA et que c'est à elle de jouer, nous lui demandons son choix

			if choix == 1: #Shoot

				if CB < 1 or lock == 0:
					CB = int(random(0, 10))
					# println(CB)
					if Player == 1:
						DistFeu1 = CB
						xbasem = xbase
						ybasem = ybase
					if Player == 2:
						DistFeu2 = CB
						xbasem = xbase2
						ybasem = ybase2

					AffTank()

					if IsMulti == False or IsMulti == True and (AmIServer == True and Player == 1 or AmIClient == True and Player == 2) or IA == True and Player == 1:
						fill(200)
						textSize(20)
						text("Press arrows to shoot your bullet in a direction", 30, 430)
						text("Then press Enter", 180, 480)

					if IA == True and Player == 2:
						Direction2 = IA("shoot") #Si nous jouons contre l'IA, elle décide dans quelle direction elle veut tirer

					if IA == False and keyCode == UP or IA == True and (Player == 1 and keyCode ==  UP or Player == 2 and Direction2 == 1):
						lock2 = 1
						lock3 = 1
						if Player == 1:
							triangle(xbase+10, ybase-10, xbase+40, ybase-10, xbase+25, ybase-30)
							Direction = 1
						if Player == 2:
							triangle(xbase2+10, ybase2-10, xbase2+40, ybase2-10, xbase2+25, ybase2-30)
							Direction2 = 1
					if IA == False and keyCode == DOWN or IA == True and (Player == 1 and keyCode == DOWN or Player == 2 and Direction2 == 2):
						lock2 = 2
						lock3 = 1
						if Player == 1:
							triangle(xbase+10, ybase+60, xbase+40, ybase+60, xbase+25, ybase+80)
							Direction = 2
						if Player == 2:
							triangle(xbase2+10, ybase2+60, xbase2+40, ybase2+60, xbase2+25, ybase2+80)
							Direction2 = 2
					if IA == False and keyCode == LEFT or IA == True and (Player == 1 and keyCode == LEFT or Player == 2 and Direction2 == 3):
						lock2 = 3
						lock3 = 1
						if Player == 1:
							triangle(xbase-10, ybase+10, xbase-10, ybase+40, xbase-30, ybase+25)
							Direction = 3
						if Player == 2:
							triangle(xbase2-10, ybase2+10, xbase2-10, ybase2+40, xbase2-30, ybase2+25)
							Direction2 = 3
					if IA == False and keyCode == RIGHT or IA == True and (Player == 1 and keyCode == RIGHT or Player == 2 and Direction2 == 4):
						lock2 = 4
						lock3 = 1
						if Player == 1:
							triangle(xbase+60, ybase+10, xbase+60, ybase+40, xbase+80, ybase+25)
							Direction = 4
						if Player == 2:
							triangle(xbase2+60, ybase2+10, xbase2+60, ybase2+40, xbase2+80, ybase2+25)
							Direction2 = 4
					if lock3 == 1 and (IA == False and keyCode == ENTER or IA == True and (Player == 1 and keyCode == ENTER or Player == 2 and IsFire2 == 1)):
						# Fire.play(3)
						lock = lock2
						lock3 = 0
						if Player == 1:
							IsFire1 = 1
						if Player == 2:
							IsFire2 = 1

				if CB > 0 and lock != 0:

					CB -= 1
					AffTank()
					if lock == 1:
						ybasem -= 50
						CDA()
						Balle = BalleU
						ProcToPy.image(Balle, screen, xbasem, ybasem)
					if lock == 2:
						ybasem += 50
						CDA()
						Balle = BalleD
						ProcToPy.image(Balle, screen, xbasem, ybasem)
					if lock == 3:
						xbasem -= 50
						CDA()
						Balle = BalleL
						ProcToPy.image(Balle, screen, xbasem, ybasem)
					if lock == 4:
						xbasem += 50
						CDA()
						Balle = BalleR
						ProcToPy.image(Balle, screen, xbasem, ybasem)
					if Player == 1 and xbasem == xbase2 and ybasem == ybase2:
						CB = 0
						vietank2 -= 1
					if Player == 2 and xbasem == xbase and ybasem == ybase:
						CB = 0
						vietank1 -= 1

					fill(200)
					textSize(50)
					text(CB, 450, 490, 500)

				if CB < 1 and lock != 0:
					choix = 0
					lock = 0
					AffTank()
					Balle = BalleExplosion
					ProcToPy.image(Balle, screen, xbasem, ybasem)
					Act -= 1
					ChangementSaison += 1


			if choix == 2: #Move
				#Initialisation du dès de déplacements
				if CP < 1:
					CP = int(random(0, 10))
					CP = 20

				#Déplacements lorsque CP est différent de 0 (Joueur a encore des déplacements)
				if CP > 0:
					if IA == True and Player == 2:
						Direction2 = IA("move") #Si nous jouons contre l'IA, elle décide dans quelle direction elle veut se déplacer

					if IA == False and keyPressed == True and keyCode == UP or IA == True and (Player == 1 and keyPressed == True and keyCode == UP or Player == 2 and Direction2 == 1):
						CP = CP-1
						if Player == 1:
							ybase -= 50
							CDD()
							Direction = 1
						if Player == 2:
							ybase2 -= 50
							CDD2()
							Direction2 = 1
						# Move.play()
					if IA == False and keyPressed == True and keyCode == DOWN or IA == True and (Player == 1 and keyPressed == True and keyCode == DOWN or Player == 2 and Direction2 == 2):
						CP = CP-1
						if Player == 1:
							ybase += 50
							CDD()
							Direction = 2
						if Player == 2:
							ybase2 += 50
							CDD2()
							Direction2 = 2
						# Move.play()
					if IA == False and keyPressed == True and keyCode == LEFT or IA == True and (Player == 1 and keyPressed == True and keyCode == LEFT or Player == 2 and Direction2 == 3):
						CP = CP-1
						if Player == 1:
							xbase -= 50
							CDD()
							Direction = 3
						if Player == 2:
							xbase2 -= 50
							CDD2()
							Direction2 = 3
						# Move.play()
					if IA == False and keyPressed == True and keyCode == RIGHT or IA == True and (Player == 1 and keyPressed == True and keyCode == RIGHT or Player == 2 and Direction2 == 4):
						CP = CP-1
						if Player == 1:
							xbase += 50
							CDD()
							Direction = 4
						if Player == 2:
							xbase2 += 50
							CDD2()
							Direction2 = 4
						# Move.play()

					if TestCadriD == 0 and (IA == False and keyCode == UP or IA == True and (Player == 1 and keyCode == UP or Player == 2 and Direction2 == 1)):
						if Player == 1:
							ybase += 50
						if Player == 2:
							ybase2 += 50
						CP += 1
						TestCadriD = 1
					if TestCadriD == 0 and (IA == False and keyCode == DOWN or IA == True and (Player == 1 and keyCode == DOWN or Player == 2 and Direction2 == 2)):
						if Player == 1:
							ybase -= 50
						if Player == 2:
							ybase2 -= 50
						CP += 1
						TestCadriD = 1
					if TestCadriD == 0 and (IA == False and keyCode == LEFT or IA == True and (Player == 1 and keyCode == LEFT or Player == 2 and Direction2 == 3)):
						if Player == 1:
							xbase += 50
						if Player == 2:
							xbase2 += 50
						CP += 1
						TestCadriD = 1
					if TestCadriD == 0 and (IA == False and keyCode == RIGHT or IA == True and (Player == 1 and keyCode == RIGHT or Player == 2 and Direction2 == 4)):
						if Player == 1:
							xbase -= 50
						if Player == 2:
							xbase2 -= 50
						CP += 1
						TestCadriD = 1

					AffTank()
					fill(200)

					textSize(50)
					text(CP, 450, 490, 500)

				#Déplacements lorsque CP est inférieur à 1 (Joueur n'a plus de déplacements)
				if CP < 1:
					choix = 0
					Act -= 1
					ChangementSaison += 1
	else:
		AffTank()

	if TimerMin <= -1 and vietank1 < vietank2 or vietank1 < 1: #Détéction de victoire (fin de timer / plus de vie)
		background(0)
		fill(255, 0, 0)
		textSize(40)
		textAlign(CENTER)
		text("Player 2 WIN", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		Winner = 2
	if TimerMin <= -1 and vietank2 < vietank1 or vietank2 < 1:
		background(0)
		fill(0, 0, 255)
		textSize(40)
		textAlign(CENTER)
		text("Player 1 WIN", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		Winner = 1
	if TimerMin <= -1 and vietank1 == vietank2: #Egalité
		background(0)
		fill(255, 0, 255)
		textSize(40)
		textAlign(CENTER)
		text("EQUALITY", 250, 220)
		textSize(20)
		text("Click SPACE to return to menu", 250, 300)
		Winner = -1

	if Design == 1 and Changementok == True and ChangementSaison == SummerDay:
		Design = 2
		ChangementSaison = 0
	if Design == 2 and Changementok == True and ChangementSaison == WinterDay:
		Design = 1
		ChangementSaison = 0
	if Design > 2:
		Design=1
	if Winner == 0:
		textAlign(RIGHT)
		textSize(15)
		fill(255)
		text(TimerMin+":"+TimerSec, width-10, 20)








# def load_ProcToPy.image(name):
# 	path = os.path.join(main_dir, 'data', name)
# 	return pygame.image.load(path).convert()
# if __name__ == '__main__':
# 	main()