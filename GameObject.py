import pyganim
import Game
from pygame import Vector2, image, draw

class GameObject:
    
    def __init__(self, pos):
        self._position = pos
        self._velocity = Vector2(0)
        self.is_active = True


    def update(self):
        if self.is_active :
            self._position += self._velocity * Game.second

            if(hasattr(self, "_GameObject__rect")) :
                self.__rect.x = self._position.x
                self.__rect.y = self._position.y

            if(hasattr(self, "_GameObject__on_collision_func")) :
                self.__check_collision()


    def draw(self):

        if self.is_active :
            if hasattr(self, "_GameObject__hasimage"):
                Game.windowSurface.blit(self._img, self._position)
            elif hasattr(self, "_GameObject__hasanimation"):
                self._curr_animation.blit(Game.windowSurface, self._position)

        # if(hasattr(self, "_GameObject__rect")) :
        #     draw.__rect(Game.windowSurface, Game.BGCOLOR, self.__rect)


    def _setColliderRect_(self, __rect, __on_collision_func):
        self.__rect = __rect

        if(__on_collision_func != None) :
            self.__on_collision_func = __on_collision_func

        Game.listCollider.append(self)


    def _setImage_(self, name):
        self._img = image.load(name)
        self.__hasimage = True


    def _setAnimation_(self, animation) :
        self.__hasanimation=True
        self._curr_animation = animation


    def __check_collision(self) :
        if self.is_active :
            for gameObj in Game.listCollider :
                __rect = gameObj.__rect
                if self.__rect.colliderect(__rect) :
                    self.__on_collision_func(gameObj)






