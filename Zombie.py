from GameObject import GameObject
from pygame import Vector2, rect
import Game
import pyganim
import pygame 
import BloodEffect
import random
import EnemyManager

class Zombie(GameObject) :

    PATH_WALK = 'Assets\\Zombie\\Walk\\'
    PATH_ATTACK = 'Assets\\Zombie\\Attack\\'
    PATH_IDLE = 'Assets\\Zombie\\Idle\\'

    def __init__(self, pos):
        super().__init__(pos)
        
        self._start_pos = Vector2(pos.x, pos.y)
        self._health= random.randint(3, 8)
        self._velocity = Vector2(-70, 0)
        self.__scale = (130, 130)
        r = rect.Rect(self._position.x, self._position.y, 130, 115)
        self._setColliderRect_(r, None)
        self.__blood_list = list()
        self.__outScreenPos__ = -self.__scale[0] * 2

        walk_anim_speed = 0.1
        self.__walk_anim = pyganim.PygAnimation(
            [
                (self.PATH_WALK + 'skeleton-move_0.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_1.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_2.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_3.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_4.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_5.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_6.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_7.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_8.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_9.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_10.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_11.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_12.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_13.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_14.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_15.png', walk_anim_speed),
                (self.PATH_WALK + 'skeleton-move_16.png', walk_anim_speed)
            ])
        self.__walk_anim.rotate(180)
        self.__walk_anim.scale(self.__scale)

        anim_attack_speed = 0.1
        self.__attack_anim = pyganim.PygAnimation(
            [
                (self.PATH_ATTACK + 'attack_0.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_1.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_2.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_3.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_4.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_5.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_6.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_7.png', anim_attack_speed),
                (self.PATH_ATTACK + 'attack_8.png', anim_attack_speed),
            ], False)
        self.__attack_anim.rotate(180)
        self.__attack_anim.scale(self.__scale)

        idle_anim_speed = 0.1
        self.idle_anim = pyganim.PygAnimation(
            [
                (self.PATH_IDLE + 'idle_0.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_1.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_2.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_3.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_4.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_5.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_6.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_7.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_8.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_9.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_10.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_11.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_12.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_13.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_14.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_15.png', idle_anim_speed),
                (self.PATH_IDLE + 'idle_16.png', idle_anim_speed)
            ])
        self.idle_anim.rotate(180)
        self.idle_anim.scale((100, 100))

        self._setAnimation_(self.__walk_anim)
        self._curr_animation.play()


    def update(self):
        super().update()

        if self.is_active :

            if self._position.x <= self.__outScreenPos__ :
                EnemyManager.EnemyManager.enque(self)

            if(hasattr(self, "_Zombie__target") and self._curr_animation == self.__attack_anim) :
                if(self.__attack_anim.currentFrameNum == 8) :
                    self._curr_animation = self.idle_anim
                    self._curr_animation.play()
                    self._position += Vector2(15, 15)   #problem with idle images 
                elif(self.__attack_anim.currentFrameNum == 4) :
                    self.__target.on_hit()


    def draw(self) :
        super().draw()

        for blood in self.__blood_list :
            blood.draw()


    def reset(self) :
        self._health = 5
        self._velocity = Vector2(-70, 0)
        self._position = Vector2(self._start_pos.x, self._start_pos.y)


    def attack(self, __target) :
        if(hasattr(self, "_Zombie__target") == False) :
            self.__target = __target
            self._velocity= Vector2(0)
            self._curr_animation = self.__attack_anim
            self._curr_animation.play()


    def on_hit(self, objectHit) :
        #it is invincible while attack
        if(hasattr(self, "_Zombie__target") == False) :
            self.__blood_list.append(BloodEffect.BloodEffect(objectHit._position))
            self._health -= 1

            if self._health <= 0 :
                EnemyManager.EnemyManager.enque(self)
      