import pygame
import random

pygame.init()
background = pygame.image.load("./img/background.jpg")
bird = pygame.image.load("./img/bird.png")
base = pygame.image.load("./img/base.svg")
gameOver = pygame.image.load("./img/gameOver.png")
pipeUp = pygame.image.load("./img/pipe.png")
pipeDown = pygame.transform.flip(pipeUp, False, True)

SCHERMO = pygame.display.set_mode((1920, 1080))
FPS = 50
# dichiarazione funzione riguardante lo status iniziale del ucceollo
def inizializza() :
	global birdx,birdy, bird_vely
	birdx, birdy = 200, 200
	bird_vely = 0

# dichiarazione funzione riguardante l'inserimento delle immagini all'interno del gioco
def draw_object() : 
	SCHERMO.blit(background, (0,0))
	SCHERMO.blit(bird, (birdx,birdy))

def refresh() : 
	pygame.display.update()
	pygame.time.Clock().tick(FPS)

inizializza()

while True:
	bird_vely += 1
	birdy += bird_vely
	draw_object()
	refresh()