import pygame
from pygame.constants import FULLSCREEN
from ennemie import ennemie
pygame.init()
pygame.display.set_caption("comet_game")
fenetre = pygame.display.set_mode((1800,780),FULLSCREEN)

running = True
fond = pygame.image.load("assets/bg.jpg").convert()
perso =  pygame.image.load("assets/player.png").convert_alpha()
persos = [pygame.image.load("assets/player/player1.png").convert_alpha(),
pygame.image.load("assets/player/player2.png").convert_alpha(),
pygame.image.load("assets/player/player3.png").convert_alpha(),
pygame.image.load("assets/player/player4.png").convert_alpha(),
pygame.image.load("assets/player/player5.png").convert_alpha(),
pygame.image.load("assets/player/player6.png").convert_alpha(),
pygame.image.load("assets/player/player7.png").convert_alpha(),
pygame.image.load("assets/player/player8.png").convert_alpha(),
pygame.image.load("assets/player/player9.png").convert_alpha(),
pygame.image.load("assets/player/player10.png").convert_alpha(),
pygame.image.load("assets/player/player11.png").convert_alpha(),
pygame.image.load("assets/player/player12.png").convert_alpha(),
pygame.image.load("assets/player/player13.png").convert_alpha(),
pygame.image.load("assets/player/player14.png").convert_alpha(),
pygame.image.load("assets/player/player15.png").convert_alpha(),
pygame.image.load("assets/player/player16.png").convert_alpha(),
pygame.image.load("assets/player/player17.png").convert_alpha(),
pygame.image.load("assets/player/player18.png").convert_alpha(),
pygame.image.load("assets/player/player19.png").convert_alpha(),
pygame.image.load("assets/player/player20.png").convert_alpha(),
pygame.image.load("assets/player/player21.png").convert_alpha(),
pygame.image.load("assets/player/player22.png").convert_alpha(),
pygame.image.load("assets/player/player23.png").convert_alpha(),
pygame.image.load("assets/player/player24.png").convert_alpha()]
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
    if pose_perso.x < -40:
        pose_perso.x = -40
    elif pose_perso.x + pose_perso.w - 40 > fenetre.get_width():
        pose_perso.x = fenetre.get_width() - pose_perso.w + 40
     