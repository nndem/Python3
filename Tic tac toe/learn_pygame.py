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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
follow = font.render('alive!', 1, RED, GREEN)


### игровой цикл (цикл обработки событий)

# перехватываем все события, связанные с нашим окном
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(follow, (0, 0))
    pygame.display.update()