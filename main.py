# Manipulate sprites
import pygame
import random

# Constant variables
FPS = 60
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)
WIDTH = 500
HEIGHT = 600

# Initialize game and window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Trek")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
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

        

all_sprites = pygame.sprite.Group()
player = Player()

all_sprites.add(player)
for i in range(18):
    rock = Rock()
    all_sprites.add(rock)

# Game loop
running = True

while running:

    # FPS runs at most in 1 sec, constrain for different CPU clocks
    clock.tick(FPS)

    # Get inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game
    all_sprites.update()

    # Render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
            
pygame.quit()