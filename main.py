import pygame as pg

from vector import fVector2 as fVec2
from vector import iVector2 as iVec2

import camera
from player import Player
from world import World


pg.init()

clock = pg.time.Clock()

screen = camera.CameraInstance(iVec2(800, 600), fVec2(0, 0))
world = World(iVec2(1800, 700), 50)

player = Player(fVec2(0, 0), fVec2(25, 25))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player.move(fVec2(0, 5))
    if keys[pg.K_s]:
        player.move(fVec2(0, -5))
    if keys[pg.K_a]:
        player.move(fVec2(5, 0))
    if keys[pg.K_d]:
        player.move(fVec2(-5, 0))
    
    pg.draw.rect(world.surface, (255,255,255), player.rect)
    print(player.pos.y)
    screen.render(world.surface, player.pos, clock)

    pg.display.flip()
    clock.tick(60)

pg.quit()