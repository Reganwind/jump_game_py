#Sprite classes for platform game
import pygame
import pygame as pg
import os
from setting import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        # self.image = pg.Surface((30, 40))
        # self.image.fill(YELLOW)
        self.image = pygame.image.load('img/little.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class PlatForm(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# pygame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption("Jumper")
# clock = pygame.time.Clock()
#
# game_folder = os.path.dirname(__file__)
# image_folder = os.path.join(game_folder, "./img/")

#define player
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((20,20))
        self.image = pg.image.load(os.path.join(image_folder, "little.png"))
        # self.image.fill(RED)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x +=5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# all_sprites = pygame.sprite.Group()
# player = Player1()
# all_sprites.add(player)
#
# running = True
# while running:
#     clock.tick(FPS)
#
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False
#
#     all_sprites.update()
#
#     screen.fill(BLACK)
#     all_sprites.draw(screen)
#
#     pygame.display.update()
#
# pygame.quit()
