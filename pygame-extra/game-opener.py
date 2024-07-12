import pygame # pip install pygame (download)

pygame.init() # initiating pygame module
width_height=(750, 600) # Window tuple
window = pygame.display.set_mode(width_height) # Display on the screen. We need to create a infinite loop.

white = (255, 255, 255)  # RGB code of white
blue = (0, 0, 255) # Blue

pygame.draw.line(window, white, (0,0), (150,250), 20) # On window, white line, start at 0-0, finish at 150-250,
# have 20 px width.

flag = True

while flag:
    # We need to create an activity in the window with for loop.
    for activity in pygame.event.get():
        print(activity)
        if activity.type == pygame.QUIT:
            flag = False
    pygame.display.update()
pygame.QUIT