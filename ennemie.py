import pygame
class ennemie():
    def __init__(self):
        self.sprite = pygame.image.load("assets/mummy.png").convert_alpha()
        self.x = 1500
        self.y = 750
        self.point_de_vie = 85
        self.vitesse = 1 
        self.largeur = self.sprite.get_width()
    def mise_a_jour(self):
        self.x = self.x - self.vitesse
    def dessiner(self,surface):
        surface.blit(self.sprite,(self.x,self.y))