import pygame

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

music = pygame.mixer.music.load("assets\Fortnite Teamate Down Sound Effect.mp3")
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,1))
    if pygame.image. get_extended ( ) == True:
        image = pygame.image.load ("assets\IMG_20230310_210204_275.jpg").convert_alpha()
        screen.blit(image, (200,200))
        image = pygame.image.load ("assets\Rn_image_picker_lib_temp_98d895ad-4d84-401e-a8dd-de28c48f54a4.jpg").convert_alpha()
        image = pygame.transform.scale_by(image, (0.1, 0.07))
        screen.blit(image, (250,250))
        
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
