import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            # create rect from the position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw the rectange
            pygame.draw.rect(screen, (183,111,122), block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else: 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True 

class FRUIT:
    def __init__(self):
        # create an x and y position
        self.randomize()

    def draw_fruit(self):
        # create a rectangle
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        # draw a square at this position
        pygame.draw.rect(screen, (126,166,114),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()

# starts all the modules (sounds, graphics,etc)
pygame.init()
cell_number = 40
cell_size = 20
# need to create the display surface (main game window)
# creates window 400 pixels wide by 500 pixels high
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# clock object that helps influence time in game
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
# this event is trigger every 150 ms
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # ends any code that's been run
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            
    # second param in blit is axis
    screen.fill((175,215,70))
    main_game.draw_elements()
    # draw all our elements (background, snake, fruits) and displays on main display surface
    pygame.display.update()
   
    # our game will never run faster than 60 frames per second
    # while loop will never execute more than 60 times per second
    clock.tick(60)