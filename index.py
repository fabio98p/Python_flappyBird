import pygame
import random

pygame.init()
background = pygame.image.load("./img/background.jpg")
bird = pygame.image.load("./img/bird.jpg")
base = pygame.image.load("./img/base.svg")
gameOver = pygame.image.load("./img/gameOver.png")
pipeDown = pygame.image.load("./img/pipe.png")
pipeUp = pygame.transform.flip(pipeDown, False, True)

windows = pygame.display.set_mode((1920, 1080))
FPS = 10000
vel_wolrd = 3
repeateBase = 573.75
font = pygame.font.SysFont('Comic Sans MS', 50)


class pipe_class:
    def __init__(self):
        self.x = 1920
        self.y = random.randint(100, 400)

    def avanzamento(self):
        self.x -= vel_wolrd
        windows.blit(pipeDown, (self.x, self.y+500))
        windows.blit(pipeUp, (self.x, self.y-500))

    def triggher(self, bird, birdx, birdy):
        tolleranza = 0

        bird_dx = birdx+bird.get_width()-tolleranza
        bird_sx = birdx+tolleranza
        bird_up = birdy+tolleranza
        bird_down = birdy+bird.get_height()-tolleranza

        pipe_dx = self.x + pipeDown.get_width()
        pipe_sx = self.x
        pipe_up = self.y
        pipe_down = self.y+500

        if  bird_sx < pipe_dx and bird_dx > pipe_sx:
            if bird_down > pipe_down or bird_up < pipe_up:
                looser()
    def between_pipe(self, bird, birdx):
        tolleranza = 0
        bird_dx = birdx+bird.get_width()-tolleranza
        bird_sx = birdx+tolleranza
        pipe_dx = self.x + pipeDown.get_width()
        pipe_sx = self.x

        if  bird_sx < pipe_dx and bird_dx > pipe_sx:
            return True
# dichiarazione funzione riguardante lo status iniziale del ucceollo


def inizializza():
    global birdx, birdy, bird_vely
    global basex
    global pipe
    global score
    global between_pipe
    birdx, birdy = 200, 200
    bird_vely = 0
    basex = 0
    score = 0
    pipe = []
    pipe.append(pipe_class())
    between_pipe = False

# dichiarazione funzione riguardante l'inserimento delle immagini all'interno del gioco


def draw_object():
    windows.blit(background, (0, 0))
    for t in pipe:
        t.avanzamento()
    windows.blit(bird, (birdx, birdy))
    # rendere il il pavimento in movimento ma essendo corto ho dovuto ripeterlo in loop
    basexLoop = basex - repeateBase
    for pippo in range(5):
        basexLoop += repeateBase
        windows.blit(base, (basexLoop, 700))
    basexLoop = 0
    score_render = font.render(str(score), 1, (255,255,255))
    windows.blit(score_render, (100,100))

# dichiarazione funzione per il refresch di ogni fotogrammo


def refresh():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

# funzione che viene chiamata quando perdi


def looser():
    # stampa game over
    windows.blit(gameOver, (500, 100))
    refresh()
    reset = False
    # while che blocca l'intero gioco finche non si usa uno dei comandi assegnati
    while not reset:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                reset = True
                inizializza()
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()


inizializza()

while True:
    # avvenimenti indipendenti dal giocatore
    bird_vely += 1
    if basex < -repeateBase:
        basex = 0
    birdy += bird_vely
    basex -= vel_wolrd
    # comandi per comandare roba
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            bird_vely = -10
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

    if pipe[-1].x < 1300:
        pipe.append(pipe_class())
    for t in pipe:
        t.triggher(bird, birdx, birdy)
    if not between_pipe:
        for t in pipe:
            if t.between_pipe(bird, birdx):
                between_pipe = True
                break
    if between_pipe:
        between_pipe = False
        for t in pipe:
            if t.between_pipe(bird, birdx):
                between_pipe = True
                break
        if not between_pipe:
            score += 1
    # quando perdi
    if birdy > 900:
        looser()
    # modifica la posizione degli elementi a sachermo
    draw_object()
    # passa al frame successivo
    refresh()
