import pygame
import random

pygame.init()
background = pygame.image.load("./img/background.jpg")
bird = pygame.image.load("./img/bird.png")
base = pygame.image.load("./img/base.svg")
gameOver = pygame.image.load("./img/gameOver.png")
pipeUp = pygame.image.load("./img/pipe.png")
pipeDown = pygame.transform.flip(pipeUp, False, True)

windows = pygame.display.set_mode((1920, 1080))
FPS = 50
vel_wolrd = 3
repeateBase = 573.75


# dichiarazione funzione riguardante lo status iniziale del ucceollo
def inizializza() :
	global birdx,birdy, bird_vely, basex
	birdx, birdy = 200, 200
	bird_vely = 0
	basex = 0

# dichiarazione funzione riguardante l'inserimento delle immagini all'interno del gioco
def draw_object() : 
	windows.blit(background, (0,0))
	windows.blit(bird, (birdx,birdy))
	# rendere il il pavimento in movimento ma essendo corto ho dovuto ripeterlo in loop
	basexLoop = basex -repeateBase
	for pippo in range(5) :
		basexLoop += repeateBase
		windows.blit(base, (basexLoop,700))
	basexLoop = 0



# dichiarazione funzione per il refresch di ogni fotogrammo
def refresh() : 
	pygame.display.update()
	pygame.time.Clock().tick(FPS)	

inizializza()


while True:
	#avvenimenti indipendenti dal giocatore
	bird_vely += 1
	if basex < -repeateBase: basex = 0
	birdy += bird_vely
	# comandi per comandare roba
	for event in pygame.event.get() :
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) :
			bird_vely = -10
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit()
	# modifica la posizione degli elementi a sachermo
	draw_object()
	basex -= vel_wolrd
	# passa al frame successivo
	refresh()