import sys
import py_compile
from py_compile import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP

py_compile.init()
#resolution is ignored on laptop
surface = py_compile.display.set_mode((640, 480))
clock = py_compile.time.Clock()
surfrect = surface.get_rect()
rect = py_compile.Rect((0,0), (128 , 128))
rect.center = (surfrect . w // 2, surfrect.h // 2)
touched = False
while True:
    for event in py_compile.event.get():
        if event.type == QUIT:
            py_compile.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                touched = True
        elif event.type == MOUSEBUTTONUP:
            touched = False

    surface.fill((0, 0, 0))
    if touched:
        rect.center = py_compile.mouse.get_pos()
    py_compile.draw.rect(surface, (255, 0, 0), rect)
    py_compile.display.flip()
    clock.tick(60)
    surface.fill((0, 0, 0))
    if touched:
        rect.move_ip(py_compile.mouse.get_rel())
        rect.clamp_ip(surfrect)
        surface.fill((255,255, 255), rect)
        py_compile.display.flip()
        

    