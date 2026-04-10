import pygame
from settings import WIDTH, HEIGHT, BLACK

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, BLACK)
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)
    
def draw_center_text(screen, text, size, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, (0,0,0))
    rect = text_surface.get_rect(center=(WIDTH//2, y))
    screen.blit(text_surface, rect)