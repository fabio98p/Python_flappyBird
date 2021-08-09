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

# funzione che viene chiamata quando perdi
def looser() :
	# stampa game over
	windows.blit(gameOver, (500, 100))
	refresh()
	reset = False
	# while che blocca l'intero gioco finche non si usa uno dei comandi assegnati
	while not reset:
		for event in pygame.event.get() :
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) :
				reset = True
				inizializza()
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				pygame.quit()


inizializza()

while True:
	#avvenimenti indipendenti dal giocatore
	bird_vely += 1
	if basex < -repeateBase: basex = 0
	birdy += bird_vely
	basex -= vel_wolrd
	# comandi per comandare roba
	for event in pygame.event.get() :
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP) :
			bird_vely = -10
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			pygame.quit()
	#quando perdi
	if birdy > 500 : looser()
	# modifica la posizione degli elementi a sachermo
	draw_object()
	# passa al frame successivo
	refresh()