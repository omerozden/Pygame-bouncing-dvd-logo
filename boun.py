import pygame

FPS             = 60
SCREENHEIGHT    = 480
SCREENWIDTH     = 640
DVD             = pygame.image.load("assets/dvd.png")
DVDHEIGHT       = int(DVD.get_rect()[2] * 0.125)
DVDWIDTH        = int(DVD.get_rect()[3] * 0.125)
COLORS          = [[255, 0, 0], [0, 255, 0], [255, 255, 0], [128, 0, 128], [255, 255, 255]]
colorIndex      = 0
exit            = False
x, y            = 0, 250
speed           = [-3, 3]


pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()
DVD = pygame.transform.scale(DVD, (DVDHEIGHT, DVDWIDTH)).convert_alpha()

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    flag = False
    if x >= SCREENWIDTH - 140 or x <= 0:
        speed[0] = -speed[0]
        flag = True
    if y >= SCREENHEIGHT - 75 or y <= 0:
        speed[1] = -speed[1]
        flag = True
    if flag:
        if colorIndex == len(COLORS) - 1:
            colorIndex = 0
        else:
            colorIndex += 1
        flag = False
    fill(DVD, pygame.Color(COLORS[colorIndex][0], COLORS[colorIndex][1], COLORS[colorIndex][2]))
    screen.fill(pygame.Color(0, 0, 0))
    screen.blit(DVD, (x, y))
    x += speed[0]
    y += speed[1]
    pygame.display.update()
    clock.tick(FPS)