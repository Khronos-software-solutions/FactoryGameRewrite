import pygame as pg

from vector import fVector2 as fVec2, iVector2 as iVec2

class CameraInstance:
    def __init__(self, size: iVec2, pos: fVec2, show_fps: bool = False):
        self.size: iVec2 = size
        self.pos: fVec2 = pos
        self.show_fps: bool = show_fps
        self.screen = pg.display.set_mode((size.x, size.y))
        self.FONT = pg.font.SysFont('Sans Serif', 30)


    def render(self, world: pg.Surface, focus: fVec2, clock: pg.time.Clock | None):
        """Renders world to screen while making sure to not show out of bounds.

        Args:
            world (pygame.Surface): The world to render. Must have a set size (height and width).
            focus (tuple[float, float]): The focus point of the camera, for example a player's location.
            clock (pygame.time.Clock): clock to show frames per second. If `show_fps` is false or clock is not given, the FPS counter will not be shown
        """

        # 'Clear' screen
        self.screen.fill((0,0,0))

        self.pos = fVec2(focus.x - self.size.x // 2, focus.y - self.size.y // 2)

        
        
        # check world bounds
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > world.get_width() - self.size.x:
            self.pos.x = world.get_width() - self.size.x
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.y > world.get_height() - self.size.y:
            self.pos.y = world.get_height() - self.size.y

        self.screen.blit(world, (0, 0), (self.pos.x, self.pos.y, self.size.x, self.size.y))

        if self.show_fps and clock is not None:
            self.screen.blit(self.FONT.render(str(round(clock.get_fps(), 2)), False, pg.Color(0,0,0)), (0,0))