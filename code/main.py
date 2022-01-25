import pygame
from obj import Obj, Fire, Text
from menu import Menu, GameOver
from game import Game


class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("../sounds/meshuggah.mp3")
        pygame.mixer.music.play(-1)
        self.sound_gameover = pygame.mixer.Sound("../sounds/gameover.mp3")

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.loop = True
        self.fps = pygame.time.Clock()

        self.menu = Menu("../sprites/start.png")
        self.game = Game()
        self.gameover = GameOver("../sprites/start.png")

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
            pygame.mixer.music.stop()
            self.sound_gameover.play()
        else:
            self.sound_gameover.stop()
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.ship.life = 4
            self.game.fire.pts = 0
            pygame.mixer.music.play()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            elif not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.ship.move_ship(events)
                self.game.fire.move_fire(events)
                self.game.prop.move_prop(events)
            else:
                self.gameover.events(events)

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


game = Main(1280, 720, "Space Destroyer")
game.update()

