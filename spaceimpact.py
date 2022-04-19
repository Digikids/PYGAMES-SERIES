import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pygame')

black = (0, 0, 0)
white = (255, 255, 255)
gold = (255,215,0)
car_width = 73

clock = pygame.time.Clock()

carImg = pygame.image.load('resources/racecar.png')
enemyImg = pygame.image.load('resources/ship.png')

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def enemy(enemyX, enemyY):
    gameDisplay.blit(enemyImg, (enemyX, enemyY))

def text_objects(text, font):
    textSurface = font.render(text, True, gold)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width/2)
    y = (display_height-90)
    enemyX = display_width/2
    enemyY = -5
    crashed = False
    moving_right, moving_left = True, False

    x_change = 0

    while crashed == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()

        #Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)
        enemy(enemyX, enemyY)

        #moving_enemy
        if moving_right == True:
            enemyX += 1
            if enemyX > (display_width-100):
                enemyY += 100
                moving_right = False
                moving_left = True
        elif moving_left == True:
            enemyX -= 1
            if enemyX < 0:
                enemyY += 100
                moving_right = True 
                moving_left = False 

        if x > (display_width-car_width) or x < 0:
            crash()

        pygame.display.update()
        clock.tick(100)

game_loop()