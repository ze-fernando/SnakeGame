import pygame
from pygame.locals import *
import const as c

pygame.init()

screen = pygame.display.set_mode(c.size)
title = pygame.display.set_caption("Snake's code by ze-fernando")

while c.reset:
    c.skin.fill((0,255,0))
    c.apple.fill((255,0,0))

    while not c.game_over:

        c.clock.tick(c.tick)
        for e in pygame.event.get():
            if e.type == QUIT:
                    pygame.quit()
                    exit()

            if e.type == KEYDOWN:
                if e.key == K_UP and c.direction != c.down:
                    c.direction = c.up

                if e.key == K_DOWN and c.direction != c.up:
                    c.direction = c.down

                if e.key == K_LEFT and c.direction != c.right:
                    c.direction = c.left

                if e.key == K_RIGHT and c.direction != c.left:
                    c.direction = c.right

        
        for p in range(len(c.snake) -1, 0, -1):
            c.snake[p] = (c.snake[p-1][0], c.snake[p-1][1])

        if c.direction == c.up:
            c.snake[0] = (c.snake[0][0], c.snake[0][1] - 10)
            
        if c.direction == c.down:
            c.snake[0] = (c.snake[0][0], c.snake[0][1] + 10)
            
        if c.direction == c.left:
            c.snake[0] = (c.snake[0][0] - 10, c.snake[0][1])
            
        if c.direction == c.right:
            c.snake[0] = (c.snake[0][0] + 10, c.snake[0][1])


        if c.colid(c.snake[0], c.pos_apple):
            c.pos_apple = c.position()
            c.snake.append((810,810))
            c.points += 1
            c.tick += 1

        if c.snake[0][0] == 800 or c.snake[0][1] == 800 or c.snake[0][0] < 0 or c.snake[0][1] < 0:
            c.game_over = True


        screen.fill((0,0,0));
        screen.blit(c.apple, c.pos_apple)

        fonte = c.font_r.render('Points: %s' % (c.points), True, (255, 255, 255))
        f_rect = fonte.get_rect()
        f_rect.topleft = (800 - 120, 20)
        screen.blit(fonte, f_rect)        

        for pos in c.snake:
            screen.blit(c.skin, pos)


        pygame.display.update()


    while c.game_over:
        screen.fill((0,0,0))

        texto = c.font_l.render('You lose!', True, (255, 255, 255))
        te_rect = texto.get_rect()
        te_rect.midtop = (800 / 2, 10)

        text = c.font_r.render('You scored  %s points!' % (c.points), True, (255, 255, 255))
        t_rect = text.get_rect()
        t_rect.midtop = (800 / 2, 60)        

        res = c.font_r.render('Press space for reset!', True, (255, 255, 255))
        res_rect = res.get_rect()
        res_rect.midtop = (800 / 2, 700)

        screen.blit(res, res_rect) 
        screen.blit(texto, te_rect)    
        screen.blit(text, t_rect)
        
        pygame.display.update()

        pygame.time.wait(500)

        while c.game_over:
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()
                    exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_SPACE:
                        c.snake = [(310,300), (320,300), (330,300)]
                        c.pos_apple = c.position()
                        c.tick = 15
                        c.points = 0
                        c.game_over = False



