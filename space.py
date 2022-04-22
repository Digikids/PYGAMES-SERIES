import pygame
import random
import math

#initialise the pygame
pygame.init()

#create the screen
mode = [800, 600]
screen = pygame.display.set_mode((mode[0], mode[1]))

#title and icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("resources/images.png")
pygame.display.set_icon(icon)

#Other variables
white = (255, 255, 255)
black = (0, 0, 0)
score_value = 0
font = pygame.font.Font("resources/PatrickHand-Regular.ttf", 20)
game_over = pygame.font.Font("resources/PatrickHand-Regular.ttf", 60)
textXY = [10, 10]

#player
playerimg = pygame.image.load("resources/racecar.png")
playerXY = [320, 500]
playerX_change = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
	enemyimg.append(pygame.image.load("resources/enemy.png"))
	enemyX.append(random.randint(0, mode[0]-64))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(0.3)
	enemyY_change.append(40)

#bullet
bulletimg = pygame.image.load("resources/bullet.png")
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 0.9
bullet_state = "ready"
#Drawing the player on the screen
def player(x, y):
	screen.blit(playerimg, (x, y))
#Drawing the enemy
def enemy(x, y, i):
	screen.blit(enemyimg[i], (x, y))
def show_score(x, y):
	score = font.render("Score: " + str(score_value), True, black)
	screen.blit(score, (x, y))

def game_over_text():
	over_text = game_over.render("GAME OVER!!", True, black) 
	screen.blit(over_text, (250, 250))

def fire_bullet(x, y):
	global bullet_state
	bullet_state = "Fire"
	screen.blit(bulletimg, (x+36, y))

def is_collision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY- bulletY, 2)))
	if distance < 40:
		return True
	else:
		return False

running = True
while running == True:
	screen.fill(white)
	#exiting the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#moving the player
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.7
			if event.key == pygame.K_RIGHT:
				playerX_change = + 0.7
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bulletX = playerXY[0]
					fire_bullet(bulletX, bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerXY[0] += playerX_change
	#checking boudaries
	if playerXY[0] <= 0:
		playerXY[0] = 0
	elif playerXY[0] > mode[0]-73:
		playerXY[0] = mode[0]-73

	#drawing the enemies
	for i in range(num_of_enemies):
		#game over
		if enemyY[i] > 300:
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break
		enemyX[i] += enemyX_change[i]	
		if enemyX[i] <= 0:
			enemyY_change[i] = 0.3
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= mode[0]-64:
			enemyX_change[i] = -0.3
			enemyY[i] += enemyY_change[i]

		#collision
		collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision == True:
			bulletY = 480
			bullet_state = "ready"
			score_value += 1
			enemyX[i] = random.randint(0, mode[0]-64)
			enemyY[i] = random.randint(30, 150)

		enemy(enemyX[i], enemyY[i], i)

	#bullet movement
	if bulletY <= 0:
		bulletY = 480
		bullet_state = "ready"
	if bullet_state == "Fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change

	player(playerXY[0], playerXY[1])
	show_score(textXY[0], textXY[1])
	pygame.display.update()

pygame.quit()