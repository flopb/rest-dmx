#import pygame
#screen = pygame.display.set_mode( ( 1024, 768 ) )
#screen = pygame.display.set_mode( ( 1024, 768 ), pygame.FULLSCREEN )

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

crashed = False

WHITE=(255,255,255)
BLUE=(0,0,255)

gameDisplay.fill(WHITE)

pygame.draw.rect(gameDisplay,BLUE,(200,150,100,50))

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYUP and event.key == 27:
            pygame.quit()
        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()