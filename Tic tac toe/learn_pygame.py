import pygame

# создаем окно программы
size = (600, 400)
pygame.display.set_mode(size)
pygame.display.set_caption('My Programme')
img = pygame.image.load('icon.jpg')
pygame.display.set_icon(img)


### игровой цикл (цикл обработки событий)

# перехватываем все события, связанные с нашим окном
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()