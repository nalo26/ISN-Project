import pygame, ProcToPy

pygame.init()

ecran = pygame.display.set_mode((300, 200))
image = pygame.image.load("data/arbre.png").convert_alpha()

continuer = True

while continuer:
	ProcToPy.image(image, ecran, 0, 50)
	# ecran.blit(image, (0, 50))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			continuer = False
	pygame.display.flip()

pygame.quit()