import pygame
import settings
from player import Player

pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.GAME_TITLE)

clock = pygame.time.Clock() # Relógio para controlar o FPS

# Inicializando o jogador
player = Player(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2, settings.PLAYER_SPEED)

running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Preenche a tela com a cor preta

    player.move(dt)  # Movimenta o jogador
    player.draw(screen)  # Desenha o jogador

    pygame.display.flip()  # Atualiza a tela

    dt = clock.tick(settings.FPS) / 1000  # Calcula o tempo decorrido

pygame.quit()
