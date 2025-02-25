import pygame
pygame.init()

window =pygame.display.set_mode((600,600))

pygame.display.set_caption("My_first pygame")

x = 550
y = 50
vel = 7
width = 40
length = 60

is_jump = False
jump_count = 10

clock = pygame.time.Clock()
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT]and x < 600 - width - vel:
        x += vel

    if not (is_jump):

        if keys[pygame.K_DOWN] and y < 600 - length - vel:
            y += vel
        
        if keys[pygame.K_UP]and y > vel:
            y -= vel

        if keys[pygame.K_SPACE]:
            is_jump = True

    else:
        if jump_count >= -10:
          y -= (jump_count * abs(jump_count)) * 0.5
          jump_count -= 1
        else:
            jump_count = 10
            is_jump = False


    window.fill((0,254,254))
    pygame.draw.rect(window,(255,255,0),(x,y,width,length))
    pygame.display.update()
    # clock.tick(100)

pygame.quit()   

