import pygame
pygame.init()

window =pygame.display.set_mode((600,600))

pygame.display.set_caption("My_first pygame")

x = 50
y = 50
vel = 6
width = 40
length = 60

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get ():
        if event.type == pygame.quit:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
       x += vel
    
    if keys[pygame.K_DOWN]:
       y += vel
    
    if keys[pygame.K_UP]:
       y -= vel

    window.fill((0,254,254))
    pygame.draw.rect(window,(255,255,0),(x,y,width,length))
    pygame.display.update()

pygame.quit()   

