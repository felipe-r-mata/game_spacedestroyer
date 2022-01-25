import pygame


class Obj:

    def __init__(self, image, x, y):

        pygame.init()

        pygame.mixer.init()
        self.sound_fire = pygame.mixer.Sound("../sounds/laser.mp3")
        self.sound_block = pygame.mixer.Sound("../sounds/explosion.mp3")
        self.sound_crash = pygame.mixer.Sound("../sounds/crash.mp3")
        self.sound_bonus = pygame.mixer.Sound("../sounds/bonus.mp3")

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.life = 4
        self.bonus = 0

        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0
            self.frame += 1

        if self.frame == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("../sprites/" + image + str(self.frame) + ".png")

    def colision(self, group, name):
        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "asteroid" and colision:
            self.sound_crash.play()
            self.life -= 1
        elif name == "bonus" and colision:
            self.sound_bonus.play()
            self.bonus += 1
        elif self.bonus == 4:
            self.life += 1
            self.bonus = 0

    def move_ship(self, event):
        pygame.mouse.set_visible(False)
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 50
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 49

    def move_prop(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 32
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] + 30


class Fire(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.pts = 0

        pygame.time.set_timer(pygame.USEREVENT, 10)

    def shot(self, image):
        self.sprite.image = pygame.image.load(image)

    def move_fire(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.sound_fire.play()
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 22
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 140

        if event.type != pygame.USEREVENT:
            return
        self.sprite.rect[1] -= 10

    def colision_fire(self, group, name):
        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "asteroid" and colision:
            self.sound_block.play()
            self.pts += 10


class Text:

    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Arial Bold", size)
        self.render = self.font.render(text, False, (255, 255, 255))

    def drawing(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, text):
        self.render = self.font.render(text, False, (255, 255, 255))
