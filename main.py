import pygame

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,1))
    if pygame.image. get_extended ( ) == True:
        image = pygame.image.load ("assets\IMG_20230310_210204_275.jpg").convert_alpha()
        screen.blit(image, (200,200))
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
