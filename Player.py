import pyganim
import pygame
from Game import Game
from ShootEffect import ShootEffect
from BloodEffect import BloodEffect
from Bullet import Bullet
from GameObject import GameObject
from Zombie import Zombie

class Player(GameObject):
    
    PATH_SHOOT = 'Assets\\handgun\\shoot\\'   
    PATH_IDLE = 'Assets\\handgun\\idle\\'
    PATH_WALK = 'Assets\\handgun\\move\\'

    def __init__(self, pos):
        super().__init__(pos)
        
        self.__speed = float(150)
        self.__scale = (100, 100)
        self.__is_shooting=False
        self.__gunOffset = pygame.Vector2(94, 57)
        self.__bulletOffset = pygame.Vector2(13, 13)
        self.__shootEffect = ShootEffect.ShootEffect()
        self.__bulletList = list()

        self.__create_animations__()
        self._setAnimation_(self.__idle_anim)
        self.__idle()

        r = pygame.rect.Rect(self._position.x, self._position.y, 70, 115)
        self._setColliderRect_(r, self.on_collision)


    def input(self, event):

        if hasattr(self, "_Player__block_input") == False :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self._velocity.x = self.__speed
                    self.__walk()
                elif event.key == pygame.K_a:
                    self._velocity.x = -self.__speed
                    self.__walk()

                if event.key == pygame.K_w:
                    self._velocity.y = -self.__speed
                    self.__walk()
                elif event.key == pygame.K_s:
                    self._velocity.y = self.__speed
                    self.__walk()
            else : 
                self._velocity=pygame.Vector2(0)

                if(self.__is_shooting == False 
                    and self._curr_animation != self.__idle_anim)  :
                    self.__idle()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 1 and self.__is_shooting==False):
                    self.__shoot()
    

    def update(self):
        super().update()

        if(self._curr_animation == self.__shoot_anim):
            if(self.__shoot_anim.currentFrameNum == 2):
                self.__is_shooting=False
                self.__idle()

        if self.__shootEffect.is_active : 
            self.__shootEffect.update()

        if hasattr(self, "_Player__blood_effect") :
            self.__blood_effect.update()   

        for bullet in self.__bulletList :
            if bullet.is_out_of_screen() == False :
                bullet.update()
            else:
                self.__bulletList.remove(bullet)  


    def draw(self):
        super().draw()

        if self.__shootEffect.is_active :
            self.__shootEffect.draw()

        if hasattr(self, "_Player__blood_effect") :
            self.__blood_effect.draw()

        for bullet in self.__bulletList :
            bullet.draw()


    def __idle(self):
        self._velocity = pygame.Vector2(0)
        self.__changeAnimation(self.__idle_anim)


    def __shoot(self) :
        self.__is_shooting = True
        self.__shootEffect.play(self.__gunOffset + self._position)
        self.__bulletList.append(Bullet.Bullet(self.__shootEffect._position + self.__bulletOffset))
        self.__changeAnimation(self.__shoot_anim)
        

    def __walk(self):
        if hasattr(self, "_Player__is_shooting") and self.__is_shooting == False:
            self.__changeAnimation(self.__walk_anim)


    def on_hit(self) :
        self.is_active= False
        self.__blood_effect = BloodEffect.BloodEffect(self._position)


    def __changeAnimation(self, animation):
        self._curr_animation.stop()
        self._curr_animation = animation
        self._curr_animation.play()


    def __create_animations__(self):
        shoot_anim_speed = 0.06
        self.__shoot_anim = pyganim.PygAnimation(
            [
                (self.PATH_SHOOT + 'survivor-shoot_handgun_0.png', shoot_anim_speed),
                (self.PATH_SHOOT + 'survivor-shoot_handgun_1.png', shoot_anim_speed),
                (self.PATH_SHOOT + 'survivor-shoot_handgun_2.png', shoot_anim_speed)
            ], False)
        self.__shoot_anim.scale(self.__scale)

        self.__idle_anim = pyganim.PygAnimation(
            [
                (self.PATH_IDLE + 'survivor-idle_handgun_0.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_1.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_2.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_3.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_4.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_5.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_6.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_7.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_8.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_9.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_10.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_11.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_12.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_13.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_14.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_15.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_16.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_17.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_18.png', 0.1),
                (self.PATH_IDLE + 'survivor-idle_handgun_19.png', 0.1)
            ])
        self.__idle_anim.scale(self.__scale)

        walk_anim_speed = 0.05
        self.__walk_anim = pyganim.PygAnimation(
            [
            (self.PATH_WALK + 'survivor-move_handgun_0.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_1.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_2.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_3.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_4.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_5.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_6.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_7.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_8.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_9.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_10.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_11.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_12.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_13.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_14.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_15.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_16.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_17.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_18.png', walk_anim_speed),
            (self.PATH_WALK + 'survivor-move_handgun_19.png', walk_anim_speed)
            ])
        self.__walk_anim.scale(self.__scale)


    def on_collision(self, objCollision) :
    
        if type(objCollision) is Zombie.Zombie :
            self.__block_input = True
            self._velocity=pygame.Vector2(0)
            objCollision.attack(self)