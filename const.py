#Libs
import pygame
import random

pygame.init()
#Tela
X = 800
Y = 800

size = (X,Y)

#Funções

def position():
    x = random.randint(0,790)
    y = random.randint(0,790)

    return (x // 10 * 10, y // 10 * 10)


def colid(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])



#Direções

up = 0

right = 1

down = 3

left = 2

#Componentes

snake = [(310,300), (320,300), (330,300)]

skin = pygame.Surface((10,10))

apple = pygame.Surface((10,10))

pos_apple = position()

direction = up

clock = pygame.time.Clock()

tick = 15

points = 0

game_over = False

reset = True

font_r = pygame.font.Font('freesansbold.ttf', 22)

font_l = pygame.font.Font('freesansbold.ttf', 40)

