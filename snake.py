#!/usr/bin/env python3

# snake.py is a simple snake game with pygame

import pygame
import time
import random

# constants
snake_speed = 10

window_x = 720
window_y = 480
cell_size = 20

font_name = 'times new roman'
font_small = 20
font_large = 50
antialias = True

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)


# initialize pygame
pygame.init()

# set window
bounds = (window_x, window_y)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")

# FPS (frames per second) controller
fps = pygame.time.Clock()

# pause variable
pause = False

# starting score
score = 0
score_per_apple = 10

# snake class
class Snake:
    length = 4
    position = [10 * cell_size, 5 * cell_size]
    body = [ [10 * cell_size, 5 * cell_size],
                   [9 * cell_size, 5 * cell_size],
                   [8* cell_size, 5 * cell_size],
                   [7 * cell_size, 5 * cell_size]
                 ]
    direction = 'RIGHT'
    
    #snake methods
    def ChangeDirection(self, change_to):
        # snake can't reverse it's movement
        if change_to == 'UP' and self.direction != 'DOWN':
             self.direction = 'UP'
        if change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    
    def Move(self):
        # Moving the snake
        if self.direction == 'UP':
            self.position[1] -= cell_size
        if self.direction == 'DOWN':
            self.position[1] += cell_size
        if self.direction == 'LEFT':
            self.position[0] -= cell_size
        if self.direction == 'RIGHT':
            self.position[0] += cell_size
            
        # check for collisions - screen edges
        if self.position[0] < 0 or self.position[0] > window_x - cell_size:
            GameOver()
        if self.position[1] < 0 or self.position[1] > window_y - cell_size:
            GameOver()
        # check for collision with self
        for block in self.body:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                GameOver()

        # check for fruit (will need to rework when fruit is an object)
        if self.position[0] == fruit_position[0] and self.position[1] == fruit_position[1]:
            self.length += 1
            global score
            score += score_per_apple
            global fruit_spawn
            fruit_spawn = False

            
        # update the snake array to include the new position
        self.body.insert(0, list(self.position))
        # drop the oldest postion if snake is longer than length
        if len(self.body) > self.length:
            self.body.pop();
        
    def Draw(self):
        for pos in self.body:
            pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))


#fruit as global variables until I  think of how to make this a class
fruit_position = [random.randrange(1, window_x//cell_size) * cell_size, 
                  random.randrange(1, window_y//cell_size) * cell_size]

fruit_spawn = True

def fruit_draw(fruit_pos):
    pygame.draw.rect(window, red, pygame.Rect(fruit_pos[0], fruit_pos[1], cell_size, cell_size))

# # Fruit class
# class Fruit:
    
#     def __init__(self):
#         self.position = [random.randrange(1, window_x//cell_size) * cell_size,
#                     random.randrange(1, window_y//cell_size) * cell_size]
                
# score board class
class ScoreBoard:

    # def __init__(self):
    #     self.score = 0

    # def increase(self):
    #     self.score += score_per_fruit

    def Draw(self):
        score_font = pygame.font.SysFont(font_name, font_small)
        score_surface = score_font.render("Score: " + str(score), antialias, white)
        score_rect = score_surface.get_rect()
        window.blit(score_surface, score_rect)




# Game over function
def GameOver():
    message_font = pygame.font.SysFont(font_name, font_large)
    game_over_surface = message_font.render("Game Over", antialias, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit draws the text on the screen
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # quit after 2 seconds
    time.sleep(2)
    pygame.quit()
    quit()

snake = Snake()

board = ScoreBoard()

change_to = snake.direction;

# Main game loop
while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                if pause == False:
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    # sending commands to snake
    snake.ChangeDirection(change_to)
        
    if not pause:
        snake.Move()

    # make new apple if it was eaten
    if not fruit_spawn:
        fruit_position = [random.randrange(1, window_x//cell_size) * cell_size,
                          random.randrange(1, window_y//cell_size) * cell_size]
        fruit_spawn = True
    
    # clear the screen for the new frame
    window.fill(black)
    
    # drawing the snake
    snake.Draw()

    # draw the fruit
    fruit_draw(fruit_position)

    # draw the scoreboard
    board.Draw()
    
    # refresh the screen
    pygame.display.update()
    
    # FPS refresh rate
    fps.tick(snake_speed)
