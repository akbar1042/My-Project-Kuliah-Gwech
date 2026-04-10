import pygame
import random
from settings import WIDTH

class EnemyCar:
    def __init__(self, speed):
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        x = random.randint(50, WIDTH - 100)
        self.rect = self.image.get_rect(topleft=(x, -100))
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class PowerUp:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(50, WIDTH-50), -50, 30, 30)
        self.speed = 5

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
    