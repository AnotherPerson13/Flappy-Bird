# Игра сделанная на [pygame] со сбором монет и препятствиями

### В этом README файле я расскажу как все устроено в моей программе как можно четко и ясно

### Цель игры - Собрать 3 монеты и закончить уровень 
Сами монеты раскиданы в случайном положении по карте

- ###  [Раздел 1] - Базовая часть кода
- ###  [Раздел 2] - Функции, функции и ещё раз функции

## Раздел 1 - Основая часть игры. ~~или проще база~~


Эта часть кода которую мы будем смотреть 


``` python
import random
import pygame
from pygame.locals import *

pygame.init()

Height = 800
Width = 750

Coins_sum = 0
Hits_sum: int = 0

Fps = 60
FramePerSec = pygame.time.Clock()

is_jump = False

displaysurface = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Game")
```
Начиная со строки 1 - 4, я импортировал библиотеки 
- **random**
- **pygame**

И инициализировал сам [pygame] для его работы.

Со строки 5 - 9, я присваиваю переменным данные для их работы по типу Coins_sum.

- **Coins_sum** - Это переменная хранит в себе данные о том сколько монет собрал игрок и сколько сейчас он имеет их
- **Hits_sum** - Переменная которая подсчитавает количество столкновений игрока с блоком который наносит урон игроку (При его касании считайте это гарантированная смерть и перезапуск игры)
- **Fps** - Думаю это логично, количество кадров в секунду которое разрешено обрабатывать игре 
- - FramePerSecond - Это часть от Fps которая дает команду python-у
- **is_jump** - Переменная необходимая для гравитации, передает значение если игрок в воздухе или нет

Последние 2 строки отвечают за присваивание игре название вместо стандартного на "Game"
и придает игре размер окна от переменных **Width** и **Height**

---

## Раздел 2 - Классы, классы и ещё раз классы

Эта часть кода достаточно важная и без нее игра банально не сможет запустится без данных по типу 
- **Игрока**
- **Платформы**
- **Монеты**
- и **_Платформы смерти_**

---

### Красная платформа ~~не смерти~~
``` python
class Baseplate(pygame.sprite.Sprite):
    def __init__(self):

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((Width, 20))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(Width / 2, Height - 10))
```
Он создан в классе и имеет параметры
- **image** - Придает прямоугольнику изображение 
- - **fill** - Закрашивает прямоугольник
- **rect** - Сам прямоугольник

Это платформа на которой игрок может спокойно стоять и прыгать ~~и бла бла бла~~

---

### Обычная платформа
``` python
class Platform1(pygame.sprite.Sprite):
    def __init__(self, x, y,size_x,size_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size_y, size_x))
        self.image.fill((200, 110, 30))
        self.rect = self.image.get_rect(center=(x, y))
```
Он также ~~как и все следующие~~ создан в классе и имеет параметры
- **image** - Придает прямоугольнику изображение 
- - **fill** - Закрашивает прямоугольник
- **rect** - Сам прямоугольник

! И при этом имеет параметры которые указываются при создании класса !
- **x**
- **y**
- **size_x**
- **size_y**

X и переменная Y нужны для того что бы поставить платформу в определенную точку на карте тогда как 
Size_x и Size_y необходимы для установления размеров платформы

---

### Платформа убийца или же платформа смерти
``` python
class KillPlatform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((height, width))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
```
Эта платформа которую вы неособо полюбите т.к она может снести ваш прогресс в 0 при помощи только 1 прикосновения как я говорил ранее
> (При его касании считайте это гарантированная смерть и перезапуск игры)

Эта платформа имеет такие же значения как с обычной платформой и различается только красным цветом и небольшим размером

---

### Монеты ~~или же золото без текстур~~
``` python 
class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill((248, 218, 41))
        self.rect = self.image.get_rect(center=(x, y)
```        

Все те же данные - но уже размер и её цвет различается от обычных платформ

---

### Наш игрок 
``` python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill((128, 255, 40))
        self.rect = self.image.get_rect(center=(100, 400))
        self.speed = 5
        self.is_jump = False
        self.gravity = 3
        self.jump_power = 200
        self.fall_speed = 1
        self.ground = 0
```
---
Этот раздел с игроком самый важный и хранит кучу информации о игроке и т.д по типу 
- **image** - Внешний вид игрока
- **rect** - Его хитбокс или же прямоугольник
- **speed** - Скорость передвижения игрока
- **is_jump** - Находится ли игрок в прыжке ~~или воздухе~~
- **gravity** - Гравитация которая тянет игрока вниз
- **jump_power** - Сила прыжка игрока
- **fall_speed** - Скорость падения игрока
- **ground** - Находится ли игрок на любой платформе (Baseplate,Platform1)
---
#### Также он имеет свою функцию
``` python
    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -8
        if keys[pygame.K_d]:
            self.speedx = 8
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= Height - 15:
            self.rect.bottom = Height - 15
            self.is_jump = False

        if self.is_jump == False:
            if keys[pygame.K_SPACE]:
                self.ground = self.rect.y
                self.is_jump = True
                self.gravity = -4.5
        if self.is_jump == True:
            if self.rect.y <= self.ground - 195:  # Высота прыжка (Менять последний параметр)
                self.gravity = 5

        self.rect.x += self.speedx
        self.rect.y += self.gravity
```
Как по мне тут стоит рассказать по подробнее о том что и для чего нужно

---
## Переменные функции
- keys - Сама переменная keys отслеживает нажатия игрока на определенные кнопки по типу 
- - K_a - Кнопка A ~~или же Ф~~
- - K_d - Кнопка D ~~или же в~~
- - K_SPACE - Кнопка пробела
- speedx - Собственная скорость игрока по координатам X 
- - При отсутствии движения она равна 0
- - При движении в левую сторону -8 
- - При движении в правую сторону 8
---
## Сами функции
Передвижение персонажа 
- A - Это налево
- D - Это направо
---
``` python
    if keys[pygame.K_a]:
            self.speedx = -8
        if keys[pygame.K_d]:
            self.speedx = 8
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= Height - 15:
            self.rect.bottom = Height - 15
            self.is_jump = False
```
---
Прыжок игрока
- Проверяет если игрок сейчас в прыжке
- - Если нет то при нажатии K_SPACE
> (K_SPACE - Кнопка пробела)
>
- - Значение ground приравнивается последнему месту (по оси Y) где был игрок
- - Приравнивают значение is_jump в True
- - И ставит значение гравитации -4.5
``` python
    if self.is_jump == False:
    if keys[pygame.K_SPACE]:
        self.ground = self.rect.y
        self.is_jump = True
        self.gravity = -4.5
```

---

## Раздел 3 - Нудное присваивание данных

Тут мы присваиваем данные всем группам, классам и т.д
``` python
x_place = random.randint(1, 750)
x2_place = random.randint(1, 750)
x3_place = random.randint(1, 750)
y_place = random.randint(200,600)
y2_place = random.randint(200,600)
y3_place = random.randint(200,600)

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
players = pygame.sprite.Group()
coins = pygame.sprite.Group()
kill_platforms = pygame.sprite.Group()

BP = Baseplate()

P1 = Player()

PT1 = Platform1(100, 250, 100, 20)
PT2 = Platform1(300, 450, 30, 120)
PT3 = Platform1(600, 200, 74, 20)
PT4 = Platform1(400, 600, 15, 50)

KT1 = KillPlatform(20, 20, 600, 500)

C1 = Coins(x_place, y_place)
C2 = Coins(x2_place, y2_place)
C3 = Coins(x3_place, y3_place)

players.add(P1)
platforms.add(BP)
platforms.add(PT1)
platforms.add(PT2)
platforms.add(PT3)
platforms.add(PT4)

kill_platforms.add(KT1)

coins.add(C1)
coins.add(C2)
coins.add(C3)

all_sprites.add(P1)

all_sprites.add(BP)
all_sprites.add(PT1)
all_sprites.add(PT2)
all_sprites.add(PT3)
all_sprites.add(PT4)

all_sprites.add(KT1)

all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)
```






















[pygame]: <https://pygame.ru/?ysclid=lhlsj9u86q715249548>
