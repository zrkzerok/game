import pygame
from pygame.constants import FULLSCREEN, MOUSEBUTTONDOWN
from ennemie import ennemie
from sort import sort
def charge_imgs(dossier,fichier,extension,nombre):
    images = []
    for i in range(1,nombre + 1):
        print(dossier + fichier + str(i) + extension)
        image = pygame.image.load(dossier + fichier + str(i) + extension).convert_alpha()
        images.append(image)
    return images 
pygame.init()
pygame.display.set_caption("comet_game")
fenetre = pygame.display.set_mode((1800,780),FULLSCREEN)

running = True
fond = pygame.image.load("assets/bg.jpg").convert()
persos = charge_imgs("assets/player/","man",".png",5)
fireball_img = charge_imgs("assets/","projectile",".png",1)
for i in range(len(fireball_img)):
    fireball_img[i] = pygame.transform.scale(fireball_img[i],(100,100))
kamea_img = charge_imgs("assets/kamea/","EnergyBall",".png",7)
for i in range(len(persos)):
    persos[i] = pygame.transform.flip(persos[i],True,False)
    persos[i] = pygame.transform.scale(persos[i],(120,120))
persoindex = 0
sorts = []
momies = [ennemie()]
pose_perso = persos[persoindex].get_rect()
animationcount = 0
pose_perso = pose_perso.move(50,760)
pygame.key.set_repeat(30,30)
horloge = pygame.time.Clock()
temp_respawn = 0

while running:
    animationcount = animationcount + 1
    dt = horloge.tick()
    temp_respawn = temp_respawn - dt
    if temp_respawn <= 0:
        momies.append(ennemie())
        temp_respawn = 1200
    if animationcount >= 50:
        animationcount = 0
        persoindex = persoindex + 1
        if persoindex == 5:
            persoindex = 0
    fenetre.blit(fond,(0,0))
    fenetre.blit(persos[persoindex],pose_perso)
    invalidesort = []
    for s in sorts:
        s.mise_a_jour()
        s.dessiner(fenetre)
        momies_invalide = []
    
        for momie in momies:
            if s.x + s.largeur() > momie.x and s.x + s.largeur() < momie.x + momie.largeur:
                momie.point_de_vie = momie.point_de_vie - s.degat
                if momie.point_de_vie <= 0:
                    momies_invalide.append(momie)
                invalidesort.append(s)
                break
            
        for momie_invalide in momies_invalide:
            momies.remove(momie_invalide)
    for sort_invalide in invalidesort:
        sorts.remove(sort_invalide)
    for momie in momies:   
        momie.mise_a_jour()
        momie.dessiner(fenetre)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                fireball = sort(pose_perso.x,pose_perso.y)
                fireball.images(fireball_img)
                fireball.vitesse = 2
                fireball.degat = 35
                sorts.append(fireball)
            elif event.button == pygame.BUTTON_RIGHT:
                kamea = sort(pose_perso.x,pose_perso.y)
                kamea.vitesse = 1
                kamea.degat = 100
                kamea.images(kamea_img)
                sorts.append(kamea)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pose_perso = pose_perso.move(20,0)
            elif event.key == pygame.K_q:
                pose_perso = pose_perso.move(-20,0)
    if pose_perso.x < -40:
        pose_perso.x = -40
    elif pose_perso.x + pose_perso.w - 40 > fenetre.get_width():
        pose_perso.x = fenetre.get_width() - pose_perso.w + 40
     