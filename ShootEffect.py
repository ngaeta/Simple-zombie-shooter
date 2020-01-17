from GameObject import GameObject
from pygame import Vector2, transform
import Game

class ShootEffect(GameObject):
    
    PATH_IMAGES = 'Assets\\shootEffect.png'

    def __init__(self):
        super().__init__(Vector2(0))
        self._setImage_(self.PATH_IMAGES)
        self.__time_to_disappear = float(0.7)
        self.is_active = False
        self._img = transform.scale(self._img, (30, 30))


    def update(self):
        super().update()

        if self.is_active :
            if self.__time_to_disappear <= 0 :
                self.is_active =False
            else:
                self.__time_to_disappear-= AIV.Game.deltaTime


    def play(self, shootPos):
        self.__time_to_disappear= float(0.7)
        self.is_active = True
        self._position = shootPos

