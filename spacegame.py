import pygame
import random
import math
from pygame import mixer

#To initialize the pyame
pygame.init()

screen=pygame.display.set_mode((800,600)) #Building the screen

speedadjust=1.5

#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)

#Background image and sound
background=pygame.image.load("images/background.jpg")
#mixer.music.load("images/epic-war-background-music-55-sec-361360.mp3")
#mixer.music.play()

#Player
player_img=pygame.image.load("images/player.png")
playerx=370
playery=290
change_playery=0*speedadjust
change_playerx=0*speedadjust
score=0

#Bullet
bullet_img=pygame.image.load("images/bullet.png")
bulletx=playerx+18
bullety=playery-24
change_bullety=4*speedadjust
change_bulletx=0*speedadjust
shootbullet=False

#Enemy1
enemy1_img=pygame.image.load("images/enemy.png")
enemy1x=random.randint(0,800)
enemy1y=random.randint(0,600)
change_enemy1y=1.5*speedadjust
change_enemy1x=0*speedadjust

#Enemy2
enemy2x=random.randint(0,800)
enemy2y=random.randint(0,600)
change_enemy2y=1.5*speedadjust
change_enemy2x=0*speedadjust

def player(x,y):
    screen.blit(player_img,(x,y)) #drawing an image of the pic into out screen

def enemy(x,y):
    screen.blit(enemy1_img,(x,y)) #drawing an image of the pic into out screen

def bullet(x,y):
    screen.blit(bullet_img,(x,y))

def fire_bullet():
    global bullety
    bullety-=change_bullety

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < 27

font=pygame.font.Font(None, 36)
def show_score(x,y,score):
    score_text=font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


running=True
while running:
    #TO CHANGE THE BACKGROUND
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    show_score(0,0,score)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:    #KEEP THE WINDOW OPEN UNTIL THE CLOSE BUTTON IS CLICKED ON
            running=False
        if event.type==pygame.KEYDOWN:   #CHECKING IF ANY KEY IS PRESSED OR NOT
            if event.key==pygame.K_LEFT:
                print("LEFT ARROW PRESSED")
                change_playerx=-1.9*speedadjust
            if event.key==pygame.K_RIGHT:
                print("RIGHT ARROW PRESSED")
                change_playerx=1.9*speedadjust
            if event.key==pygame.K_UP:
                print("UP ARROW PRESSED")
                change_playery=-1.9*speedadjust
            if event.key==pygame.K_DOWN:
                change_playery=1.9*speedadjust
                print("DOWN ARROW PRESSED")
            if event.key==pygame.K_SPACE or event.key==pygame.K_KP_ENTER:
                shootbullet=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                change_playerx=0
                change_playery=0
        
    #PLAYER
    playerx+=change_playerx
    playery+=change_playery
    if playerx<=0:
        playerx=0
    if playery<0:
        playery=0
    if playerx>=736: #considering the size of space ship which is 64 800-64 = 736
        playerx=736
    if playery>=536: #considering the size of space ship which is 64 600-64 = 536
        playery=536

    #enemy1 movement
    enemy1y+=change_enemy1y
    if enemy1y>=600: #considering the size of space ship which is 64 600-64 = 536
        enemy1y=0
        enemy1x=random.randint(0,600)
    #enemy2 movement
    enemy2y+=change_enemy2y
    if enemy2y>=600: #considering the size of space ship which is 64 600-64 = 536
        enemy2y=0
        enemy2x=random.randint(0,600)

    #GAMEOVER
    if is_collision(enemy1x, enemy1y, playerx, playery):
        break
    if is_collision(enemy2x, enemy2y, playerx, playery):
        break

    #BULLET
    if shootbullet:
        bullet(bulletx,bullety)
        fire_bullet()
        if bullety<=0:
            shootbullet=False
            bulletx=playerx+18
            bullety=playery-24
    else:
        bullety=playery-24
        bulletx=playerx+18

    if is_collision(enemy1x, enemy1y, bulletx, bullety):
        score+=1
        enemy1y=0
        enemy1x=random.randint(0,600)
    if is_collision(enemy2x, enemy2y, bulletx, bullety):
        score+=1
        enemy2y=0
        enemy2x=random.randint(0,600)

    player(playerx,playery)
    enemy(enemy1x,enemy1y)
    enemy(enemy2x,enemy2y)
    pygame.display.update()
    player(playerx,playery)
    enemy(enemy1x,enemy1y)
    enemy(enemy2x,enemy2y)
    pygame.display.update()

# GAME OVER screen
over_font = pygame.font.Font(None, 64)
score_text = font.render("Score: " + str(score), True, (255, 255, 255))
game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))

while True:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(game_over_text, (300, 250))
    screen.blit(score_text, (330, 320))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
