import pygame

pygame.init()
# создаем окно программы
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Programme')
img = pygame.image.load('icon.jpg')
pygame.display.set_icon(img)

# работа со шрифтами
font = pygame.font.SysFont('malgungothic', 32)

# создание текста
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
follow = font.render('alive!', 1, RED, GREEN)
width, height = follow.get_size()
x, y = 0, 300
direct_x = 1
direct_y = 1
FPS = 60
### игровой цикл (цикл обработки событий)

clock = pygame.time.Clock()
# перехватываем все события, связанные с нашим окном
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(follow, (x, y))

    x += direct_x
    if x + width >= 600 or x < 0:
        direct_x = -direct_x

    y += direct_y
    if y + height >= 400 or y < 0:
        direct_y = -direct_y
    pygame.display.update()
