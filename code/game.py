from obj import Obj, Fire, Text
import random


class Game:

    def __init__(self):
        # background
        self.bg = Obj("../sprites/background.png", 0, 0)
        self.bg2 = Obj("../sprites/background.png", 0, -720)

        # spaceship
        self.ship = Obj("../sprites/spaceship.png", 571, 560)
        self.fire = Fire("../sprites/shot1.png", -100, -100)
        self.prop = Obj("../sprites/exhaust1.png", 590, 640)

        # asteroids & bonus
        self.bonus = Obj("../sprites/bonus1.png", random.randrange(0, 1240), random.randrange(-500, -50))
        self.asteroid = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)
        self.asteroid2 = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)
        self.asteroid3 = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)

        self.change_scene = False

        self.score = Text(60, "0")
        self.life = Text(40, "4")

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.ship.drawing(window)
        self.asteroid.drawing(window)
        self.asteroid2.drawing(window)
        self.asteroid3.drawing(window)
        self.bonus.drawing(window)
        self.fire.drawing(window)
        self.prop.drawing(window)
        self.score.drawing(window, 50, 50)
        self.life.drawing(window, 200, 50)

    def update(self):
        self.move_bg()
        self.move_bonus()
        self.move_asteroid()
        self.game_over()
        self.asteroid.anim("asteroid", 3, 17)
        self.asteroid2.anim("asteroid", 2, 17)
        self.asteroid3.anim("asteroid", 1, 17)
        self.ship.colision(self.asteroid.group, "asteroid")
        self.ship.colision(self.asteroid2.group, "asteroid")
        self.ship.colision(self.asteroid3.group, "asteroid")
        self.ship.colision(self.bonus.group, "bonus")
        self.fire.colision_fire(self.asteroid.group, "asteroid")
        self.fire.colision_fire(self.asteroid2.group, "asteroid")
        self.fire.colision_fire(self.asteroid3.group, "asteroid")
        self.bonus.anim("bonus", 2, 2)
        self.prop.anim("exhaust", 3, 4)
        self.score.update_text(str(self.fire.pts))
        self.life.update_text(str(self.ship.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 6
        self.bg2.sprite.rect[1] += 6

        if self.bg.sprite.rect[1] >= 720:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -720

    def move_asteroid(self):
        self.asteroid.sprite.rect[1] += 10

        if self.asteroid.sprite.rect[1] >= 730:
            self.asteroid.sprite.kill()
            self.asteroid = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)

        self.asteroid2.sprite.rect[1] += 5

        if self.asteroid2.sprite.rect[1] >= 730:
            self.asteroid2.sprite.kill()
            self.asteroid2 = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)

        self.asteroid3.sprite.rect[1] += 15

        if self.asteroid3.sprite.rect[1] >= 730:
            self.asteroid3.sprite.kill()
            self.asteroid3 = Obj("../sprites/asteroid1.png", random.randrange(0, 1240), -50)

    def move_bonus(self):
        self.bonus.sprite.rect[1] += 10

        if self.bonus.sprite.rect[1] >= 10000:
            self.bonus.sprite.kill()
            self.bonus = Obj("../sprites/bonus1.png", random.randrange(0, 1240), random.randrange(-500, -50))

    def game_over(self):
        if self.ship.life <= 0:
            self.change_scene = True









