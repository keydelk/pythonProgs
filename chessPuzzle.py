#!/usr/bin/env python3

import pygame

# the main pygame function
def main():
    #initialize the module
    pygame.init()
    
    #load and set the icon
    icon = pygame.image.load("icon_32x32.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Chess Puzzle")
    
    #define screen dimenstions
    screen_width = 1200
    screen_height = 900
    
    #load another image
    image = pygame.image.load("pygame135x135.png")
    
    #define the posiion
    xpos = (screen_width - 135)/2
    ypos = 10
    
    #how many pixels to move each frame
    step_x = 2
    step_y = 0
    gravity = .3
    
    #create a surface on the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    
    #define a variable to control the main loop
    running = True
    
    #main loop
    while running:
        step_y += gravity
        if step_y > 20:
            step_y = 20
        if xpos > screen_width - 135 or xpos < 0:
            step_x = -step_x
        if ypos > screen_height - 135 or ypos < 0:
            step_y = -step_y
        
        #update the position
        xpos += step_x
        ypos += step_y
        
        screen.fill((255, 255, 255))
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()
        # event handling, gets all events fomr the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False to exit the main loop
                running = False


# run the main function only if the module is executed as the main script
if __name__ == "__main__":
    main()

