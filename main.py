import pygame 
from random import randrange
from sys import exit

pygame.init()
pygame.font.init()

# Window

count = 0
SIZE = 50

WIDTH, HEIGHT = 600, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snaces")
# pygame.display.set_icon(pygame.image.load('Snace_icon.png'))

FPS = 30
clock = pygame.time.Clock()

score = 0 
scoreFont = pygame.font.SysFont(None, 30)

gameOverFont = pygame.font.SysFont(None, 50)

# Player

plX, plY = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
dx, dy  = 0, 0
snake_list = [(plX, plY)]
snake_lenght = 0

snake_dirs = {"Left":True, "Right":True, "Up":True, "Down":True}

# Apple
appleX, appleY = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)


# Game Control

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    key = pygame.key.get_pressed()

    if (key[pygame.K_w] or key[pygame.K_UP]) and snake_dirs["Up"]:
        dx,dy = 0,-1
        snake_dirs = {"Left":True, "Right":True, "Up":True, "Down":False}
    elif (key[pygame.K_s] or key[pygame.K_DOWN]) and snake_dirs["Down"]:
        dx,dy = 0,1
        snake_dirs = {"Left":True, "Right":True, "Up":False, "Down":True}
    elif (key[pygame.K_a] or key[pygame.K_LEFT]) and snake_dirs["Left"]:
        dx,dy = -1,0
        snake_dirs = {"Left":True, "Right":False, "Up":True, "Down":True} 
    elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and  snake_dirs["Right"]:
        dx,dy = 1, 0
        snake_dirs = {"Left":False, "Right":True, "Up":True, "Down":True} 

    if plX == appleX and plY == appleY:
        appleX, appleY = randrange(SIZE, WIDTH - SIZE, SIZE), randrange(SIZE, HEIGHT - SIZE, SIZE)
        score += 100
        snake_lenght += 1


    # Rendering

    win.fill((245, 244, 219))

    count += 1
    if count == 5:
        count = 0

        plX += dx * SIZE 
        plY += dy * SIZE 
        snake_list.append((plX, plY))

    pygame.draw.circle(win, (255, 0, 0), (appleX + SIZE // 2, appleY + SIZE // 2), SIZE // 2)

    for x, y in snake_list:
        plX, plY = x, y
        if plX > 550:
            plX = 0 - SIZE
        elif plX < 0:
            plX = 500 + SIZE
        elif plY > 550:
            plY = 0 - SIZE
        elif plY < 0:
            plY = 500 + SIZE
        pygame.draw.rect(win, (255, 200, 0), (plX, plY, SIZE - 3, SIZE - 3))

    if len(snake_list) != len(set(snake_list)) and snake_lenght > 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            gameOverFontRender = gameOverFont.render("GAME OVER", False, (0,0,0))
            gameOverFontSurf = gameOverFontRender.get_rect()
            gameOverFontSurf.center = (300, 100)
            win.blit(gameOverFontRender, gameOverFontSurf)

            gameOverFontRender = gameOverFont.render(f"SCORE: {str(score)}", False, (0,0,0))
            gameOverFontSurf = gameOverFontRender.get_rect()
            gameOverFontSurf.center = (300, 200)
            win.blit(gameOverFontRender, gameOverFontSurf)
            pygame.display.flip()

    snake_list = snake_list[-snake_lenght -1:]

    scoreFontRender = scoreFont.render(str(score), False, (0,0,0))
    win.blit(scoreFontRender, (500, 20))

    pygame.display.flip()
    clock.tick(FPS)