# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pixel_warrior_184x200.png")
        self.rect = self.image.get_rect()

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/pixel_orc_245x250.png")
        self.rect = self.image.get_rect()

#Константы экрана
WIDTH = 800
HEIGHT = 600
FPS = 30

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()

# Создание спрайтов травы
grass = pygame.sprite.Sprite()
grass.image = pygame.image.load("images/grass2.png")

all_sprites.add(grass)

# Создание спрайта воина
player = Player()
player.rect.x = 20
player.rect.y = HEIGHT - player.rect.height
all_sprites.add(player)

# Создание спрайта монстра
monster = Monster()
monster.rect.x = WIDTH - monster.rect.width - 20
monster.rect.y = HEIGHT - monster.rect.height
all_sprites.add(monster)



# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY =(200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Обновление
    # Обновление спрайтов

# Рендеринг
    screen.fill(GREY)
    all_sprites.draw(screen)
# После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()