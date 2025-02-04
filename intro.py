import pygame

pygame.init()

measurements = (500, 500)

window = pygame.display.set_mode(measurements)
pygame.display.set_caption('Doreens Game')

playing = True

while playing:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.draw.rect(window, (255,0,0), (50,50,60,70))
    pygame.display.update()

pygame.quit()
