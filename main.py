import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Снайпер")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)


def draw_target(x, y, time_left):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)
    text = font.render(str(time_left), True, (255, 255, 255))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def get_new_target():
    return random.randint(100, 700), random.randint(100, 500), time.time()


targets = [get_new_target() for _ in range(3)]
score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, (x, y, start_time) in enumerate(targets):
                if (x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= 30 ** 2:
                    score += 1
                    targets[i] = get_new_target()

    current_time = time.time()
    for i, (x, y, start_time) in enumerate(targets):
        time_left = 4 - int(current_time - start_time)
        if time_left < 1:
            score -= 1
            targets[i] = get_new_target()
        else:
            draw_target(x, y, time_left)

    score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# 2