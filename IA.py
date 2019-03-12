#Nous voila parti pour quelque chose de plutôt complexe -.-'
#JSONObject Traj

from ProcToPy import *

IA = False
inDev = True
MaxDepl = 0
max = 0
needed = 1
diffX = 0
diffY = 0
DeplNeed = 0
Traj = {
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

def IA(state): # Ici sont effectuées toutes les décisions de l'IA
	from Game import state, xbase, ybase, xbase2, ybase2, Direction2, IsFire2, Act, CP
	if state == "choix": #Si c'est au tour de l'IA de jouer, elle choisit ce qu'elle veut faire
		#println("x1 : "+xbase/50+", x2 : "+xbase2/50+", diff y : "+abs(ybase - ybase2)/50+", y1 : "+ybase/50+", y2 : "+ybase2/50+", diff x : "+abs(xbase - xbase2)/50)
		if Act > 1 and (xbase == xbase2 and abs(ybase - ybase2) < 7*50 or ybase == ybase2 and abs(xbase - xbase2) < 7*50): #Si le tank ennemi est aligné à nous et qu'il nous reste au moins une action
			choix = 1 #Choisir de tirer
		else:
			choix = 2 #Choisir de bouger (s'approcher si elle est trop loin, fuir s'il ne lui reste qu'une action)
		delay(200)
		return choix #Renvoyer son choix

	if state == "shoot": #Si elle veut tirer
		if xbase == xbase2 and abs(ybase - ybase2) < 7*50: #Si elle est aligné au joueur en x
			if ybase < ybase2:
				Direction2 = 1 #Tirer en haut
			if ybase > ybase2:
				Direction2 = 2 #Tirer en bas
		if ybase == ybase2 and abs(xbase - xbase2) < 7*50: #Si elle est aligné au joueur en y
			if xbase < xbase2:
				Direction2 = 3 #Tirer à gauche
			if xbase > xbase2:
				Direction2 = 4 #Tirer à droite
		delay(200)
		IsFire2 = 1 #Indiquer qu'elle tire
		return Direction2 #Renvoyer la direction de son tir

	if state == "move": #Si elle veut se déplacer
		if inDev == False:
			if Act == 3 and CP > MaxDepl:
				CalculTraj() #Calculer la nouvelle trajectoire optle
			else:
				for y in range(10): #Chercher la case suivante à laquelle elle doit aller
					for x in range(10):
						if Traj[x+y*10] == needed: #Une fois qu'elle est trouvé, savoir dans quelle direction elle est par rapport à l'IA
							if y < ybase2/50:
								Direction2 = 1 #S'orienter vers le haut
							if y > ybase2/50:
								Direction2 = 2 #S'orienter vers le bas
							if x < xbase2/50:
								Direction2 = 3 #S'orienter vers la gauche
							if x > xbase2/50:
								Direction2 = 4 #S'orienter vers la droite
				if needed + 1 == max:
					needed -= 1
				else:
					needed += 1
				#Traj[xbase2/50+ybase2/50*10] = 0
		else:
			Direction2 = int(random(1, 5)) #TEMPORAIRE, juste le temps que j'implante les décisions de déplacement. Pour le moment il se contente d'avancer aléatoirement

		delay(1000)
		return Direction2 #Renvoyer la direction vers laquelle elle avance
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
	from Game import CP, xbase2, ybase2
	
	MaxDepl = CP
	for l in range(10):
		for j in range(10):
			Traj[j+l*10] = 0 #reset de la map de déplacement
	i = 0
	toPrint = ""
	Traj[xbase/50+ybase/50*10] = -1
	tempX = xbase2/50
	tempY = ybase2/50
	if xbase > xbase2:
		while tempX != xbase/50:
			Traj[tempX+tempY*10] = i
			tempX += 1
			i += 1
	if xbase < xbase2:
		while tempX != xbase/50:
			Traj[tempX+tempY*10] = i
			tempX -= 1
			i += 1
	if ybase > ybase2:
		while tempY != ybase/50:
			Traj[tempX+tempY*10] = i
			tempY += 1
			i += 1
	if ybase < ybase2:
		while tempY != ybase/50:
			Traj[tempX+tempY*10] = i
			tempY -= 1
			i += 1
	max = i
	for l in range(10):
		for j in range(10):
			toPrint += Traj[j+l*10]+" "
		toPrint += "\n"
	print(toPrint)
	#delay(10000000)