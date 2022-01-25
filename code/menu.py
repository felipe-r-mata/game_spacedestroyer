import pygame
from obj import Obj, Text


class Menu:

    def __init__(self, image):

        self.bg = Obj(image, 0, 0)
        self.logo = Obj("../sprites/logo1.png", 100, 10)
        self.message = Obj("../sprites/menu_message1.png", 590, 600)
        self.gameover = Obj("../sprites/gameover1.png", 500, 200)

        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window)
        self.message.group.draw(window)
        self.logo.group.draw(window)
        self.update()

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True

    def update(self):
        self.message.anim("menu_message", 10, 3)
        self.logo.anim("logo", 20, 3)


class GameOver(Menu):

    def __init__(self, image):
        super().__init__(image)

        self.gameover = Obj("../sprites/gameover1.png", 500, 200)

    def draw(self, window):
        self.bg.group.draw(window)
        self.logo.group.draw(window)
        self.gameover.group.draw(window)
        self.update()

    def update(self):
        self.gameover.anim("gameover", 10, 3)







