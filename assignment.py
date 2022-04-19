import pygame
from random import randint

pygame.init()

width = 600
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Rectangle Game")

clock = pygame.time.Clock()
violet = (238, 130, 238)
my_rect_width = 50
my_rect_height = 50
rectx = width/2
recty = height/2
speedx = randint(-10, 10)
speedy = randint(-10, 10)
random_color = ()
default_color = violet


run = True

while run == True:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Moving the rectangle
    rectx += speedx
    recty += speedy
    if (rectx + my_rect_width) > 600 or rectx < 0:
        speedx *= -1
        default_color = (randint(1,255),randint(0,255),randint(0,255))
    if (recty + my_rect_height) > 600 or recty < 0:
        speedy *= -1
        default_color = (randint(1,255),randint(0,255),randint(0,255))
    
    window.fill((56, 67, 3))
    pygame.draw.rect(window, default_color, (rectx, recty, my_rect_width, my_rect_height))
    pygame.display.update()

pygame.quit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         circle_dimesions[0] -= 25
        #     if event.key == pygame.K_RIGHT:
        #         circle_dimesions[0] += 25
        #     if event.key == pygame.K_UP:
        #         circle_dimesions[1] -= 25
        #     if event.key == pygame.K_DOWN:
        #         circle_dimesions[1] += 25

        