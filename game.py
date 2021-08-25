import pygame
from pygame.constants import FULLSCREEN
from ennemie import ennemie
pygame.init()
pygame.display.set_caption("comet_game")
fenetre = pygame.display.set_mode((1800,780),FULLSCREEN)

running = True
fond = pygame.image.load("assets/bg.jpg").convert()
perso =  pygame.image.load("assets/player.png").convert_alpha()
momie = ennemie()
pose_perso = perso.get_rect()
pose_perso = pose_perso.move(50,700)
pygame.key.set_repeat(30,30)
while running:
    fenetre.blit(fond,(0,0))
    fenetre.blit(perso,pose_perso)
    momie.mise_a_jour()
    momie.dessiner(fenetre)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pose_perso = pose_perso.move(20,0)
            elif event.key == pygame.K_q:
                pose_perso = pose_perso.move(-20,0)
         