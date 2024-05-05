# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import main as m

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

# Создание спрайтов травы
def create_grass(width):
    x = 0  # Начальная координата X для первой текстуры травы
    while x < width:
        grass = pygame.sprite.Sprite()
        grass.image = pygame.image.load("images/grass2.png")
        grass.rect = grass.image.get_rect()
        grass.rect.y = HEIGHT - grass.rect.height  # Позиционируем у нижнего края окна
        grass.rect.x = x
        all_sprites.add(grass)
        x += grass.rect.width  # Перемещаем X на ширину спрайта для следующего

#Константы экрана
WIDTH = 800
HEIGHT = 600
FPS = 30

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()
create_grass(WIDTH)





# Создание спрайта воина
player = Player()
player.rect.x = 20
player.rect.y = HEIGHT - player.rect.height - 30
all_sprites.add(player)

# Создание спрайта монстра
monster = Monster()
monster.rect.x = WIDTH - monster.rect.width - 20
monster.rect.y = HEIGHT - monster.rect.height - 30
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


# Создаём персонажей на классах из main.py
monster1 = m.Monster("Пятачок",random.randint(10,30), random.randint(1,20))
warrior1 = m.Fighter(m.Sword(random.randint(3,51)))
warrior1.choose_monster(monster1)



# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: running = False

# Обработка нажатий клавиш. Здесь именно факт зажатия и удерживания
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 10
    if keys[pygame.K_RIGHT]:
        player.rect.x += 10

# Обновление
    # Обновление спрайтов

# Рендеринг
    screen.fill(GREY)

    all_sprites.draw(screen)
# После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()