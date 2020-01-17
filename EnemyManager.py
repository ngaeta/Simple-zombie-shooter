from pygame import Vector2
from AIV.Zombie import Zombie
import random
import Game

class EnemyManager() :

    enemies = list()
    POSITION = (
        (1280, 100), (1280, 300), (1280, 500),
        (1480, 100), (1480, 300), (1480, 500), 
        (1680, 100), (1680, 300), (1680, 500), 
        (1880, 100), (1880, 300), (1880, 500),
        (2080, 100), (2080, 300), (2080, 500)
    )

    @staticmethod
    def init() :
        EnemyManager.__createZombies__()


    @staticmethod
    def update():
        for enemy in EnemyManager.enemies :
            enemy.update()


    @staticmethod
    def draw() :
        for enemy in EnemyManager.enemies :
            enemy.draw()


    def enque(self, zombie) :
        if(Game.player.is_active) :
            zombie.reset()
            # half_width = Game.WIDTH / 2
            # zombie.position.x += random.randint(Game.WIDTH + half_width, Game.WIDTH * 2)


    @staticmethod
    def __createZombies__() :
        for pos in EnemyManager.POSITION :
            x = pos[0]
            y = pos[1]
            EnemyManager.enemies.append(Zombie(Vector2(x, y)))