# -*- coding: cp1252 -*-
import os
import pygame 

pygame.init()#initialisation fenetre pygame


#Chargement et collage du fond
fond = pygame.image.load(os.path.join('FondPuissance4.png')) #Chargement
fenetre.blit(fond,(0,0)) #Positionne le fond dans la fenetre

#Mettre la fenêtre a la taille de l'image
tailleimg = fond.get_size ()
fenetre = pygame.display.set_mode((tailleimg))

#Couleur du fond de la fenêtre
white=(255,255,255)
fenetre.fill(white)

pygame.display.set_caption('Fruissance 4') #Titre de la fenetre




#Chargement de la pomme
pomme = pygame.image.load("Notre nom.png").convert_alpha()


#Rafraıchissement de l'ecran
pygame.display.flip()



#Tant qu'on clique pas sur la croix quit, le jeu reste ouvert
gameExit = False
while not gameExit:              
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

#La fonction qui, à partir des coordonées du point où a cliqué l'utilisateur, retourne le numéro de la colonne correspondante
espace=
case=
def colonneChoisie(x) :
	col=(x-(espace))/case
	if col in range (0,7) :
		return col
	

		
#Cliquer là où on veut que ça aille
		if event.type == pygame.MOUSEBUTTONUP :
			x,y = pygame.mouse.get_pos()
			colonne=colonneChoisie(x)

	
	pygame.display.update()




#pygame.quit()
#quit()
