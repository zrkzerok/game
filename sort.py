import pygame
class sort():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vitesse = 0
        self.degat = 0
    def mise_a_jour(self):
         self.x = self.x + self.vitesse
    def dessiner(self,surface):
        surface.blit(self.sprites[self.img_index],(self.x,self.y))
        self.img_index = (self.img_index + 1) % len(self.sprites)
    def images(self,img):
        self.sprites = img
        self.largeurs = []
        self.img_index = 0
        for i in img:
            self.largeurs.append(i.get_width())
    def largeur(self):
        return self.largeurs[self.img_index]
    
    