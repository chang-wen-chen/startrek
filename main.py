# Manipulate sprites
import pygame
import random

# Constant variables
FPS = 60

WIDTH = 500
HEIGHT = 600

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0 ,0)
DARKGRAY = (47, 79, 79)

# Initialize game and window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Trek")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(DARKGRAY)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 8
    
    def update(self):
        # Return boolean list of keys on keyboard
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        
        self.speedy = random.randrange(2,10)
        self.speedx = random.randrange(-3,3) 
    
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
        
            self.speedy = random.randrange(2,10)
            self.speedx = random.randrange(-3,3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y
        
 
    
    def update(self):
        self.speedy = -10

        if self.rect.bottom < 0:
            self.kill()
        self.rect.y += self.speedy    

all_sprites = pygame.sprite.Group()

rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()

all_sprites.add(player)
for i in range(18):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)

# Game loop
running = True

while running:

    # FPS runs at most in 1 sec, constrain for different CPU clocks
    clock.tick(FPS)

    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update game
    all_sprites.update()
    # Judge if group elements collide, return crash number
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    # Judge trek is hit by rock, game finished
    hits = pygame.sprite.spritecollide(player, rocks, False)
    if hits:
        running = False

    # Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()
            
pygame.quit()