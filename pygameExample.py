import pygame
pygame.init() # initalise

screen = pygame.display.set_mode((1280,720)) #creates a surface
clock = pygame.time.Clock()

while True: # game loop
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill((255,255,255))  # Fill the display with a solid color
    myRect = pygame.Rect(20,20,400,300)
    pygame.draw.rect(screen,(255,0,0),myRect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
