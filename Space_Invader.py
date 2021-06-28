import pygame as pg
import random
import time
#initailize the game
pg.init()

# create the screen.
screen=pg.display.set_mode((800,600))

# Title and icon
pg.display.set_caption("Space_mayank")
icon=pg.image.load('game.png')
pg.display.set_icon(icon)
background=pg.image.load('game_background.png')
score=0
gameover=pg.image.load('gamer.png')
# Player
player_img=pg.image.load('shooter.png')
playerX=370
playerY=480
playerX_change=0
playerY_change=0
def player(x,y):
	screen.blit(player_img,(x,y))

# Enemy
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
for i in range(10):
	enemy_img.append(pg.image.load('enemy.png'))
	enemyX.append(random.randint(50,730))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(1)
	enemyY_change.append(25)

def enemy(x,y,i):
	screen.blit(enemy_img[i],(x,y))

# Bullet
bullet_img=pg.image.load('bullet1.png')
bulletX=0
bulletY=480
bulletY_change=10
bullet_state='ready'# bullet is ready to get fired.
def fire(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bullet_img,(x+16,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
	distance=(((enemyX-bulletX)**(2)) +((enemyY-bulletY)**(2)))**(1/2)
	if distance < 27:
		return True
	else:
		return False

# note that display comes only for a while and as soon as program gets executed it quits. 
# we are gonna use events in pygame to handle this.
#lets set a varible running

# Game Loop

running = True
while running:# note every functionality or event  will be written inside this while loop.   
	# filling colours to window.
	screen.fill((0,128,128))
	screen.blit(background,(0,0))


	for event in pg.event.get():# it will check each and every event of key press.
		if event.type==pg.QUIT: # this adds quit functionality to game window that I have created.
			running =False

		# if keystroke is pressed check whether its right or left.
		if  event.type ==pg.KEYDOWN:#this checks if a key is pressed or not.
			if event.key==pg.K_LEFT:
				playerX_change-=15
			if event.key==pg.K_RIGHT:
				playerX_change+=15
			if event.key==pg.K_UP:
				playerY_change-=4.5
			if event.key==pg.K_DOWN:
				playerY_change+=4.5

			if event.key==pg.K_SPACE:
				if bullet_state is "ready":

				    bulletX=playerX
				    fire(bulletX,bulletY)
		if  event.type ==pg.KEYUP:#this checks whether a pressed key is released or not.
			if event.key==pg.K_LEFT:
				playerX_change=0
			if event.key==pg.K_RIGHT:
				playerX_change=0
			if event.key==pg.K_UP:
				playerY_change=0
			if event.key==pg.K_DOWN:
				playerY_change=0


    
	
	

    # note that we have to call player function after screen.fill as screen is to be loaded first and then on top of that player is to br loaded.


# Enemy Movement	
	for i in range(10):
		enemyX[i]+=enemyX_change[i]
		if enemyX[i]<=0:
			enemyX_change[i]=1
			enemyY[i]+=enemyY_change[i]
		elif enemyX[i]>=720:
			enemyX_change[i]=-1
			enemyY[i]+=enemyY_change[i]

		collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
		if collision:
			bulletY=480
			bullet_state="ready"
			score+=1
			enemyX[i]=random.randint(50,730)
			enemyY[i]=random.randint(50,150)

		enemy(enemyX[i],enemyY[i],i)
		if enemyY[i]>=playerY-80:
			running=False
			print('GAME OVER')
			screen.blit(gameover,(144,44))
			time.sleep(3)
			print("Your score is: ",score)

		
		
	
# Bullet Movement

	if bulletY<=0:
		bulletY=480
		bullet_state="ready"
	if bullet_state is "fire":
		fire(bulletX,bulletY)
		bulletY-=bulletY_change
	
# Player Movement 
	playerX+=playerX_change
	if playerX<=0:
		playerX=0
	if playerX>=736:
	    playerX=736
	player(playerX,playerY)
	pg.display.update()#we need to update the display after every frame.
	
