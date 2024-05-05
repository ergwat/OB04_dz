# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import main as m

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_sword_up = pygame.image.load("images/pixel_warrior_sword_up.png")
        self.image_sword_down = pygame.image.load("images/pixel_warrior_sword_down.png")
        self.image = self.image_sword_up
        self.rect = self.image.get_rect()
        self.attacking = False
        self.attack_timer = None

    def attack(self):
        self.sword_hit()
        if self.rect.right >= monster_sprite.rect.left:
            monster1.hp = warrior1.attack()

    def sword_hit(self):
        if not self.attacking: # Начать анимацию только если не атакуем
            self.image = self.image_sword_down
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks() # Запускаем таймер

    def update(self):
        # Обновление состояния атаки
        if self.attacking and pygame.time.get_ticks() - self.attack_timer > 200:
            self.image = self.image_sword_up # Возращаем исходное изображение
            self.attacking = False # Закончили анимацию атаки
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


class TextBox(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.font = pygame.font.Font("PressStart2P-Regular.ttf", 18)
        self.image = self.font.render(self.text, False, RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.text = f"{monster1.name}: {monster1.hp} hp"
        self.image = self.font.render(self.text, False, RED)
#Константы экрана
WIDTH = 800
HEIGHT = 600
FPS = 30

# Создание группы спрайтов
all_sprites = pygame.sprite.Group()
create_grass(WIDTH)

# Создаем игру и окно
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Создаем шрифт
font = pygame.font.Font("PressStart2P-Regular.ttf", 18)

# Создание спрайта воина
player_sprite = Player()
player_sprite.rect.x = 20
player_sprite.rect.y = HEIGHT - player_sprite.rect.height - 30
all_sprites.add(player_sprite)

# Создание спрайта монстра
monster_sprite = Monster()
monster_sprite.rect.x = WIDTH - monster_sprite.rect.width - 200
monster_sprite.rect.y = HEIGHT - monster_sprite.rect.height - 30
all_sprites.add(monster_sprite)


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY =(200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Создаём персонажей на классах из main.py
monster1 = m.Monster("Пятачок",random.randint(10,30), random.randint(1,20))
warrior1 = m.Fighter(m.Sword(random.randint(3,51)))
warrior1.choose_monster(monster1)


# Создаем поверхность с текстом
monster_healthbar = TextBox(f"{monster1.name}: {monster1.hp} hp", (monster_sprite.rect.x + monster_sprite.rect.width//2), (monster_sprite.rect.y - 20))
all_sprites.add(monster_healthbar)

#all_sprites.add(text)









# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    player_sprite.attack()

                case pygame.K_LEFT:
                    if player_sprite.rect.x > 0:
                        player_sprite.rect.x -= 10

                case pygame.K_RIGHT:
                    if player_sprite.rect.right < monster_sprite.rect.left + 50:
                        player_sprite.rect.x += 10


# Обновление
# Обновление спрайтов
    all_sprites.update()  # Важно вызвать метод update у всех спрайтов

    # Рендеринг
    screen.fill(GREY)
    all_sprites.draw(screen)

# После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

'''# Обработка нажатий клавиш. Здесь именно факт зажатия и удерживания, если нужно непрерывное движен
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.rect.x > 0: player.rect.x -= 10
    if keys[pygame.K_RIGHT]:
        if player.rect.right < monster.rect.left + 25: player.rect.x += 10
'''