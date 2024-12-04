import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.draw.rect(screen, (255,255,255), pg.Rect(20, 30, 40, 50))
    
    pg.display.flip()
    clock.tick(60)

pg.quit()