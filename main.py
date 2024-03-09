# sprite
import pygame

# Constant variables
FPS = 60
WHITE = (255,255,255)
GREEN = (0, 255, 0)
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
        self.rect.center = (WIDTH/2,HEIGHT/2)
    
    def update(self):
        self.rect.x += 2
        if self.rect.left > WIDTH:
            self.rect.right = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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