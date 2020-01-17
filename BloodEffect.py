from GameObject import GameObject
from pygame import Vector2
import pyganim
import random

class BloodEffect(GameObject) :

    PATH_IMAGES_01 = 'Assets\\blood\\'
    PATH_IMAGES_02 = 'Assets\\blood2\\'
    PATH_IMAGES_03 = 'Assets\\blood3\\'
    

    def __init__(self, pos):
        super().__init__(pos)

        randomInt = random.randint(0, 2)
        anim = self.__create_random_blood(0)
        self._setAnimation_(anim)
        self._curr_animation.play()


    def play(self):
        if(self.is_active == False) :
            self.is_active=True
            self._curr_animation.play()


    def __create_random_blood(self, randomInt) :
        if(randomInt == 0) :
            anim = pyganim.PygAnimation(
                [
                    (BloodEffect.PATH_IMAGES_01 + 'blood_01.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01+ 'blood_02.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_03.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_04.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_05.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_06.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_07.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_08.png', 0.1),
                    (BloodEffect.PATH_IMAGES_01 + 'blood_09.png', 0.1),
                ], False)
        elif randomInt == 2 :
            anim = pyganim.PygAnimation(
                [
                    (BloodEffect.PATH_IMAGES_02 + 'blood_01.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02+ 'blood_02.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02 + 'blood_03.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02 + 'blood_04.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02 + 'blood_05.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02 + 'blood_06.png', 0.1),
                    (BloodEffect.PATH_IMAGES_02 + 'blood_07.png', 0.1)
                ], False)
        else :
            anim = pyganim.PygAnimation(
                [
                    (BloodEffect.PATH_IMAGES_03 + 'blood_01.png', 0.2),
                    (BloodEffect.PATH_IMAGES_03 + 'blood_02.png', 0.2),
                    (BloodEffect.PATH_IMAGES_03 + 'blood_03.png', 0.2),
                    (BloodEffect.PATH_IMAGES_03 + 'blood_04.png', 0.2)
                ], False)

        return anim

    