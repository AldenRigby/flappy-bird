import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2000)

game = Game('img/bird.png', 'img/pipe.png', 'img/background.png', 'img/ground.png')
game.resize_images()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()
            elif event.key == pygame.K_SPACE and not game.active:
                game.restart()

        if event.type == SPAWNPIPE:
            game.add_pipe()
            game.difficulty += 1 

    game.show_background(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.show_pipes(screen)
        game.move_pipes()
        game.check_collision()
        game.update_score()
        game.show_score("playing", screen, "black")
    else:
        game.game_over(screen, "red")

    game.show_ground(screen)
    game.move_ground()

    pygame.display.update()
    clock.tick(120)
