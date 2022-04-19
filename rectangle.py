import pygame
from random import randint

pygame.init()
my_dimensions = [600, 600]

window = pygame.display.set_mode((my_dimensions[0],my_dimensions[1]))
pygame.display.set_caption("Rectangle Game")

clock = pygame.time.Clock()
B_color = (0, 0, 0)
RectDims = [50, 50]
RectCood = [my_dimensions[0]/2, my_dimensions[1]/2]
default_color = (238, 130, 238)
speeds = [randint(-10, 10), randint(-10, 10)]

run = True
while run == True:
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Rectangle movements
    RectCood[0] += speeds[0]
    RectCood[1] += speeds[1]
    if (RectCood[0] + RectDims[0] > 600) or (RectCood[0] < 0):
        speeds[0] *= -1
        default_color = (randint(1, 255), randint(1, 255), randint(1, 255))
    if (RectCood[1] + RectDims[1]) > 600 or RectCood[1] < 0:
        speeds[1] *= -1
        default_color = (randint(1, 255), randint(1, 255), randint(1, 255))
    window.fill(B_color)
    pygame.draw.rect(window, default_color, (RectCood[0], RectCood[1], RectDims[0], RectDims[1]))
    pygame.display.update()

pygame.quit()