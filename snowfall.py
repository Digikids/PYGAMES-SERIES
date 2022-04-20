import pygame
import random

pygame.init()

color = [(0, 0, 0), (255, 255, 255)]
size = [700, 600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow Animation")

snow_list = []
for i in range(50):
    x = random.randrange(0, size[0])
    y = random.randrange(0, size[1])
    snow_list.append([x, y])

radius = 2
done = False
clock = pygame.time.Clock()

while done == False:
    screen.fill(color[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, color[1], snow_list[i], radius)
        snow_list[i][1] += 1

        #Cheking if the snow flake has moved off bottom of the screen
        if snow_list[i][1] > size[1]:
            #Reset it to just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, size[0])
            snow_list[i][0] = x


    pygame.display.update()
    clock.tick(20)

pygame.quit()
