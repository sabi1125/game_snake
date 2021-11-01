import pygame
from pygame.constants import WINDOWHITTEST
import random
import math




#initinize pygame
pygame.init()
#set screen size 
screen = pygame.display.set_mode((800,600))
skin = (255,255,255)
#snake 
snakeImg = pygame.image.load("head.png")
snakeRe = pygame.transform.scale(snakeImg,(32,32))
snakeX = 400
snakeY = 300
snake_changeX = 0
snake_changeY = 0

def snake(x,y):
    screen.blit(snakeRe,(x,y))



#food
foodImg = pygame.image.load("food.png")
foodX = random.randint(0,800)
foodY = random.randint(0,600)
def food():
    screen.blit(foodImg,(foodX,foodY))




#eating food mechanic(collison)
def eat(foodX,foodY,snakeX,snakeY):
    distance = math.sqrt((math.pow(foodX-snakeX,2)) + (math.pow(foodY-snakeY,2)))
    if distance < 27:
        return True
    else:
        return False
    

score_val = 0


font = pygame.font.Font('freesansbold.ttf',24)
textX = 10
textY = 10

def score(x,y):
    score = font.render("Score : " + str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))


running = True


while running:
    screen.fill((0,0,0))
    score(textX,textY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_changeX = 0
                snake_changeY = -4
            if event.key == pygame.K_DOWN:
                snake_changeX = 0
                snake_changeY = 4
            if event.key == pygame.K_RIGHT:
                snake_changeY = 0
                snake_changeX = 4
            if event.key == pygame.K_LEFT:
                snake_changeY = 0
                snake_changeX = -4




#eatfood mechanic
    eaten = eat(foodX,foodY,snakeX,snakeY)
    if eaten:
        foodX = random.randint(600,800)
        foodY = random.randint(0,600)
        score_val+= 1
        
    

#food border
    if foodX > 762:
        foodX = 762
    elif foodX < 0:
        foodX = 0

    if foodY > 562:
        foodY = 562
    elif foodY < 0:
        foodY = 0



#snake border blocks
    if snakeX > 762:
        snakeX = 762    
        print("GAMEOVER\n Score: " + str(score_val))
        break

    if snakeY > 562:
        snakeY = 562
        print("GAMEOVER\n Score: " + str(score_val))
        break

    if snakeX < 0:
        snakeX =0
        print("GAMEOVER\n Score: " + str(score_val))
        break
    
    if snakeY < 0:
        snakeY = 0
        print("GAMEOVER\n Score: " + str(score_val))
        break

    snakeY += snake_changeY
    snakeX += snake_changeX

    food()
    snake(snakeX,snakeY)
    pygame.display.update()
