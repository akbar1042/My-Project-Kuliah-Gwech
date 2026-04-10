import pygame
import random
from settings import *
from player import PlayerCar
from enemy import EnemyCar
from enemy import PowerUp
from utils import draw_text
from utils import draw_center_text
pygame.init()
jalan = pygame.image.load("assets/jalan.png")
jalan = pygame.transform.scale(jalan, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("DARJO RACING")
clock = pygame.time.Clock()

player = PlayerCar()
enemies = []
powerups = []

jalan_y = 0
spawn_timer = 0
score = 0
speed = 5
flash = 0

game_state = "menu"

running = True

while running:
    clock.tick(FPS)
    jalan_y += 5
    if jalan_y >= HEIGHT:
        jalan_y = 0

    screen.blit(jalan, (0, jalan_y))
    screen.blit(jalan, (0, jalan_y - HEIGHT))
    
    pygame.image.load("assets/jalan.png")
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "menu":
                game_state = "play"
                draw_center_text(screen, "TRAFFIC RACER", 50, 200)
                draw_center_text(screen, "Press any key to start", 30, 300)
            elif game_state == "gameover":
                # reset game
                enemies.clear()
                score = 0
                speed = 5
                player.rect.center = (WIDTH//2, 500)
                game_state = "play"
                draw_center_text(screen, "GAME OVER", 50, 250)
                draw_center_text(screen, f"Score: {score}", 30, 300)
                draw_center_text(screen, "Press any key to restart", 25, 350)

    if game_state == "menu":
        draw_text(screen, "TRAFFIC RACER", 50, WIDTH//2, 200)
        draw_text(screen, "Press any key to start", 30, WIDTH//2, 300)

    elif game_state == "play":
        keys = pygame.key.get_pressed()
        player.move(keys)

        spawn_timer += 1
        if spawn_timer > 30:
            enemies.append(EnemyCar(speed))
            spawn_timer = 0
            
            
        if random.randint(1, 200) == 1:
            powerups.append(PowerUp())

        for enemy in enemies:
            enemy.move()

            if player.rect.colliderect(enemy.rect):
                game_state = "gameover"
                flash = 10
                
        for p in powerups:
            p.move()
            p.draw(screen)

            if player.rect.colliderect(p.rect):
                player.speed += 2
                powerups.remove(p)

        enemies = [e for e in enemies if e.rect.y < HEIGHT]

        score += 1

        # difficulty scaling 🔥
        if score % 200 == 0:
            speed += 1

        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        draw_text(screen, f"Score: {score}", 30, 70, 30)

    elif game_state == "gameover":
        draw_text(screen, "GAME OVER", 50, WIDTH//2, 250)
        draw_text(screen, f"Score: {score}", 30, WIDTH//2, 300)
        draw_text(screen, "Press any key to restart", 25, WIDTH//2, 350)


    if flash > 0:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(100)
        overlay.fill((255, 0, 0))
        screen.blit(overlay, (0, 0))
        flash -= 1
    
    pygame.display.flip()

pygame.quit()