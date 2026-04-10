import pygame
from settings import WIDTH

class PlayerCar:
    def __init__(self):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect(center=(WIDTH//2, 500))
        self.speed = 6

    def move(self, keys):
        angle = 0

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            angle = 10
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            angle = -10

        self.rotated_image = pygame.transform.rotate(self.image, angle)

    def draw(self, screen):
        img = getattr(self, "rotated_image", self.image)
        screen.blit(img, self.rect)