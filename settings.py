import pygame as pg 
# Game Options and Settings

# Set the DEBUG_MODE flag
# This is used to enable some additional help such as displaying events within the console as the game is being played.
DEBUG_MODE = True

# Set the title/name of the game
TITLE = "Stacker"

# Define the dimensions of the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Define the number of frames per second.
FPS = 60

# Define Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255,165,0)

# Define the gird size
# The grid is made up of quares so this will be used for both width and height of each individual square within the grid.
GRID_SIZE = 40

# The last level is when the player manages to get to the very top row of the grid.
# this is calualted from dividing the screen height by the grid size and geting the integer value (i.e. no remainder) 
MAX_LEVEL = SCREEN_HEIGHT // GRID_SIZE

# Define input trigger that will be used to identify that the player wants to start a new game.
START_GAME_USER_TRIGGER = pg.K_SPACE

# Define in-game input trigger.
# This is the main game action.
INPUT_USER_TRIGGER = pg.K_SPACE

# Define the number of lives to start with.
# The specifies the number of boxes to start with
LIVES_START = 5

# Define the level to start on
LEVEL_START = 1

# Define the colors for the active boxes
# These are the boxes that are currently moving left-to-right and in-active boxes.
BOX_ACTIVE_COLOR = (0,60,136)

# Define the colors for the in-active boxes
# These are the boxes that are left behind on the previous levels.
BOX_INACTIVE_COLOR = (0,132,203)