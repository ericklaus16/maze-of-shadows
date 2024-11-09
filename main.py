import pygame

pygame.init() # Inicializa o Pygame
screen = pygame.display.set_mode((1280, 720)) # Cria uma janela de resolução 1280x720
pygame.display.set_caption("Maze of Shadows") # Define o nome da janela
clock = pygame.time.Clock() # Cria um objeto para ajudar a controlar o tempo
running = True

while(running):
    for event in pygame.event.get(): # Pegar eventos do pygame até que o evento QUIT seja encontrado
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) # Preenche a tela com a cor preta 
    pygame.display.flip() # Atualiza a tela

    clock.tick(120) # Limita a taxa de atualização para 120 FPS

pygame.quit() # Finaliza o Pygame