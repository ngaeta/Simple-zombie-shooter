
from pygame import Vector2, transform
import pygame
import Game
from GameObject import GameObject
from Zombie import Zombie

class Bullet(GameObject):

    PATH_IMAGES = 'Assets\\bullet.png'

    def __init__(self, pos):
        super().__init__(pos)

        self._setImage_(self.PATH_IMAGES)
        self._velocity = Vector2(1280, 0)
        self._img = transform.scale(self._img, (10, 10))
        self._setColliderRect_(pygame.rect.Rect(self._position.x, self._position.y, 15, 10), self.on_collision)

    
    def update(self):
        super().update()

        if(self.is_active) :
            if(self._position.x > Game.WIDTH) :
                self.is_active= False
                self.__out_of_screen = True

    
    def is_out_of_screen(self) :
        if(hasattr(self, "_Bullet__out_of_screen")) :
            return self.__out_of_screen
        else :
            return False


    def on_collision(self, objCollision) :

        if type(objCollision) is Zombie and hasattr(objCollision, "on_hit") :
            objCollision.on_hit(objCollision)
            self.is_active=False
            self.__out_of_screen =True #for delete



    