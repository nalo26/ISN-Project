#Nous voila parti pour quelque chose de plutôt complexe -.-'
import pygame
import settings as v
from ProcToPy import *
v.init()

def IA(state): # Ici sont effectuées toutes les décisions de l'IA
	if state == "choix": #Si c'est au tour de l'IA de jouer, elle choisit ce qu'elle veut faire
		#println("x1 : "+xbase/50+", x2 : "+xbase2/50+", diff y : "+abs(ybase - ybase2)/50+", y1 : "+ybase/50+", y2 : "+ybase2/50+", diff x : "+abs(xbase - xbase2)/50)
		if v.Act > 1 and (v.xbase == v.xbase2 and abs(v.ybase - v.ybase2) < 7*50 or v.ybase == v.ybase2 and abs(v.xbase - v.xbase2) < 7*50): #Si le tank ennemi est aligné à nous et qu'il nous reste au moins une action
			v.choix = 1 #Choisir de tirer
		else:
			v.choix = 2 #Choisir de bouger (s'approcher si elle est trop loin, fuir s'il ne lui reste qu'une action)
		delay(200)
		return choix #Renvoyer son choix

	if state == "shoot": #Si elle veut tirer
		if v.xbase == v.xbase2 and abs(v.ybase - v.ybase2) < 7*50: #Si elle est aligné au joueur en x
			if v.ybase < v.ybase2:
				v.Direction2 = 1 #Tirer en haut
			if v.ybase > v.ybase2:
				v.Direction2 = 2 #Tirer en bas
		if v.ybase == v.ybase2 and abs(v.xbase - v.xbase2) < 7*50: #Si elle est aligné au joueur en y
			if v.xbase < v.xbase2:
				v.Direction2 = 3 #Tirer à gauche
			if v.xbase > v.xbase2:
				v.Direction2 = 4 #Tirer à droite
		delay(200)
		v.IsFire2 = True #Indiquer qu'elle tire
		return v.Direction2 #Renvoyer la direction de son tir

	if state == "move": #Si elle veut se déplacer
		if v.inDev == False:
			if v.Act == 3 and v.CP > v.MaxDepl:
				CalculTraj() #Calculer la nouvelle trajectoire optle
			else:
				for y in range(10): #Chercher la case suivante à laquelle elle doit aller
					for x in range(10):
						if v.Traj[x+y*10] == v.needed: #Une fois qu'elle est trouvé, savoir dans quelle direction elle est par rapport à l'IA
							if y < v.ybase2/50:
								v.Direction2 = 1 #S'orienter vers le haut
							if y > v.ybase2/50:
								v.Direction2 = 2 #S'orienter vers le bas
							if x < v.xbase2/50:
								v.Direction2 = 3 #S'orienter vers la gauche
							if x > v.xbase2/50:
								v.Direction2 = 4 #S'orienter vers la droite
				if v.needed + 1 == max:
					v.needed -= 1
				else:
					v.needed += 1
				#v.Traj[xbase2/50+ybase2/50*10] = 0
		else:
			v.Direction2 = random(1, 5) #TEMPORAIRE, juste le temps que j'implante les décisions de déplacement. Pour le moment il se contente d'avancer aléatoirement

		delay(1000)
		return v.Direction2 #Renvoyer la direction vers laquelle elle avance
	return -1 #En cas d'erreur, renvoyer -1


'''
Si nous ne sommes pas alligné
S'il nous reste de la vie
S'il reste des choix
S'il reste des déplacments

Prendre en compte :
Ete:
Peut pas aller sur la lave / montagne
Vitesse/2 sur l'eau

Hiver:
Eviter la lave (perte de vie)
Peut pas aller sur les montagnes
Glisse sur la glace (toute une longueur = 1 déplacement)
'''

def CalculTraj():	
	v.MaxDepl = v.CP
	for l in range(10):
		for j in range(10):
			v.Traj[j+l*10] = 0 #reset de la map de déplacement
	i = 0
	toPrint = ""
	v.Traj[xbase/50+ybase/50*10] = -1
	tempX = v.xbase2/50
	tempY = v.ybase2/50
	if v.xbase > v.xbase2:
		while tempX != v.xbase/50:
			v.Traj[tempX+tempY*10] = i
			tempX += 1
			i += 1
	if v.xbase < v.xbase2:
		while tempX != v.xbase/50:
			v.Traj[tempX+tempY*10] = i
			tempX -= 1
			i += 1
	if v.ybase > v.ybase2:
		while tempY != v.ybase/50:
			v.Traj[tempX+tempY*10] = i
			tempY += 1
			i += 1
	if v.ybase < v.ybase2:
		while tempY != v.ybase/50:
			v.Traj[tempX+tempY*10] = i
			tempY -= 1
			i += 1
	max = i
	for l in range(10):
		for j in range(10):
			toPrint += v.Traj[j+l*10]+" "
		toPrint += "\n"
	print(toPrint)
	#delay(10000000)