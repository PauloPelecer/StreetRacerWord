import pygame
pygame.init()

# Inicialize a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

# Carregue a sprite
sprite_image = pygame.image.load('sprite.png')
sprite_rect = sprite_image.get_rect()
sprite_rect.center = (screen_width // 2, screen_height // 2)

click_time = None
clicked = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if sprite_rect.collidepoint(event.pos):
                click_time = pygame.time.get_ticks()
                clicked = True

    screen.fill((255, 255, 255))

    # Desenhe a sprite
    screen.blit(sprite_image, sprite_rect)

    if clicked:
        current_time_ms = pygame.time.get_ticks()
        elapsed_seconds = (current_time_ms - click_time) // 1000
        font = pygame.font.Font(None, 36)
        text = font.render(f"Segundos após o clique: {elapsed_seconds}", True, (0, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 50))

    pygame.display.flip()
    clock.tick(60)  # Limite de 60 FPS

pygame.quit()
