import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        # create an x and y position
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # draw a square at this position
        pygame.draw.rect(screen, (126,166,114),fruit_rect)


# starts all the modules (sounds, graphics,etc)
pygame.init()

cell_number = 40
cell_size = 20
# need to create the display surface (main game window)
# creates window 400 pixels wide by 500 pixels high
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# clock object that helps influence time in game
clock = pygame.time.Clock()

fruit = FRUIT()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # ends any code that's been run
            sys.exit()
    # second param in blit is axis
    screen.fill((175,215,70))
    fruit.draw_fruit()
    # draw all our elements (background, snake, fruits) and displays on main display surface
    pygame.display.update()
   
    # our game will never run faster than 60 frames per second
    # while loop will never execute more than 60 times per second
    clock.tick(60)