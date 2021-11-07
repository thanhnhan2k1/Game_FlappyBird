#file chứa hàm main chính của game
#flappybird.py

#khai báo thư viện dùng trong game
import pygame, sys, random,os, menu, Bird, Columns, Scores
from pygame.locals import *
from pygame import mixer

#chèn nhạc vào trong game
mixer.init()
pygame.mixer.music.load('img\FlyAway.mp3')
pygame.mixer.music.play(-1)

pygame.init()
#os.environ['SDL_VIDEO-CENTERED'] = '1'

#các thông số của cửa sổ pygame
WINDOWNWIDTH = 400
WINDOWNHEIGHT=600

#hàm để định dạng phông chữ
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont,textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

#một vài màu sắc cơ bản
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

#phông chữ Supermario256
font = "m/SuperMario256.ttf"

#những thông tin của lớp Bird
BIRDWIDTH = 60
BIRDHEIGHT = 43
G = 0.5
SPEEDLY = -8
BIRDUP = pygame.image.load('img/birdup.png')
BIRDDOWN = pygame.image.load("img/birddown.png")
BIRDEND = pygame.image.load('img/gothit1.png')

#nhũng thông tin của lớp Columns
COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 160
DISTANCE = 200
COLUMNSPEED = 2
COLUMNING = pygame.image.load('img/column2.png')

#load ảnh nền của game và menu
BACKGROUND = pygame.image.load('img/background.png')
Menu_bg = pygame.image.load('img/background.png')

FPS=60
fpsClock = pygame.time.Clock()

DISPLAYSURF =  pygame.display.set_mode((WINDOWNWIDTH, WINDOWNHEIGHT))
pygame.display.set_caption('Flappy Bird')

#Hàm main
def main():
    bird = Bird.Bird()
    columns = Columns.Columns()
    score = Scores.Scores()
    
    while True:
        menu.main_menu()      
if __name__ == '__main__':
    main()