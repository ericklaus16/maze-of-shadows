import pygame

class Player:
    def __init__(self, x, y, speed):
        self.pos = pygame.Vector2(x, y)
        self.speed = speed
        self.radius = 40

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.pos.x += self.speed * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, self.radius)
