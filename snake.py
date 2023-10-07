import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
    def draw_snake(self):
        for block in self.body:
            # create rect from the position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw the rectange
            pygame.draw.rect(screen, (183,111,122), block_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
class FRUIT:
    def __init__(self):
        # create an x and y position
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rectangle
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
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
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
# this event is trigger every 150 ms
pygame.time.set_timer(SCREEN_UPDATE, 150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # ends any code that's been run
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            
    # second param in blit is axis
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    # draw all our elements (background, snake, fruits) and displays on main display surface
    pygame.display.update()
   
    # our game will never run faster than 60 frames per second
    # while loop will never execute more than 60 times per second
    clock.tick(60)