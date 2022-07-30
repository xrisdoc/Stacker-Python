import pygame

DEBUG_MODE = True

# Colour Constants
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (255,165,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

BOX_ACTIVE_COLOR = (0,60,136)
BOX_INACTIVE_COLOR = (0,132,203)

SCREEN_WIDH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 40
MAX_LEVEL = SCREEN_HEIGHT // GRID_SIZE

START_GAME_USER_TRIGGER = pygame.K_SPACE
INPUT_USER_TRIGGER = pygame.K_SPACE

LIVES_START = 5
LEVEL_START = 1

SCREEN_NAME = "Stacker"

def main():
    # This is the game entry point

    # Define the varaibles that we need to be in a global scope.
    global SCREEN, CLOCK

    # Initialise the PyGame engine and setup the all of the resources we need (i.e Screen and Clock etc.)
    pygame.init() 
    pygame.display.set_caption(SCREEN_NAME)

    SCREEN = pygame.display.set_mode((SCREEN_WIDH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()

    # Display the startup screen
    # On this screen we will wait for the user to confirm when they want to start playing the game
    displayScreen("startup", START_GAME_USER_TRIGGER)

    # Draw all of the elements on the screen that need to be there when the game starts
    setupGameScreen()

    # Run the game!
    # This will loop indefinitely until the game is WON or LOST (or the user Quits)
    runGameLoop()
    
    # Terminate PyGame
    pygame.display.quit()
    pygame.quit()

def displayScreen(screenType, inputTrigger):

    if screenType == "startup":
        SCREEN.fill(YELLOW)

    elif screenType == "winner":
        SCREEN.fill(GREEN)

    elif screenType == "game-over":
        SCREEN.fill(RED)

    pygame.display.update()

    running = True
    while running:
        pygame.time.delay(50)

        for event in pygame.event.get():
            # NOTE:
            # For debuging purposes we will display the event information within the console.
            # This will only be output if the game is currently in debug mode (i.e. DEBUG_MODE = True)
            if DEBUG_MODE == True:
                print (event)
            
            # Check for the QUIT event
            # We need to stop the loop when this event is triggered.
            if event.type == pygame.QUIT:
                running = False

        # Check for the user input trigger that indicates we no longer need the current screen to be displayed
        # When the user triggers this input we will stop the loop and the proceed to the next step.
        keys = pygame.key.get_pressed()
        if keys[inputTrigger]:
            running = False

def setupGameScreen():
    # Set up the screen contents
    drawGrid(GRID_SIZE, BLACK)

def runGameLoop():
    # Initialise some variables
    level = LEVEL_START
    lives = LIVES_START    
    running = True

    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            # NOTE:
            # For debuging purposes we will display the event information within the console.
            # This will only be output if the game is currently in debug mode (i.e. DEBUG_MODE = True)
            if DEBUG_MODE == True:
                print (event)
            
            # Check for the QUIT event
            # We need to stop the game loop when this event is triggered.
            if event.type == pygame.QUIT:
                running = False

        # NOTE: 
        # This is only for testing at the moment. 
        # We will add more complexity to this to make progressing to the next level a bit mor challenging.
        # For now, when the user triggers the input action, move to the next level
        keys = pygame.key.get_pressed()
        if keys[INPUT_USER_TRIGGER]:
            level += 1

        # As long as the level is less than or equal to the MAX_LEVEL, the game will be in progress.
        # If the level has went beyond the MAX_LEVEL value then the user has successfully completed the game.

        if(level <= MAX_LEVEL):
            # Game is still in progress
            drawCharacterBoxes(level, lives)
            pygame.display.update()
        else:
            # The game was WON!
            # Stop the game loop and display the winner screen.
            running = False
            displayScreen("winner", START_GAME_USER_TRIGGER)
            

def drawCharacterBoxes(level, lives):
    # Reduce the lives of the user as they progress through the levels
    # This will make it more challenging to complete as they will have less chances to get it right on the later levels
    if (level == 3 or level == 4) and lives > 4:
        lives = 4

    elif (level == 5 or level == 6) and lives > 3:
        lives = 3

    elif (level == 7 or level == 8) and lives > 2:
        lives = 2

    elif (level == 9 or level == 10) and lives > 1:
        lives = 1

    # The border variable will pad the boxes abit to fit nicely within the grid squares
    border = 1

    # The number of lives determine how many active boxes are to be displayed
    # So, we want to create a box for each life the user currently has.
    for i in range(lives):
        # Determine where the current box should be placed
        posX = border + (i * GRID_SIZE)
        posY = SCREEN_HEIGHT - GRID_SIZE + border - ((level - 1) * GRID_SIZE)

        # Draw the current box on the screen
        rect = pygame.Rect((posX, posY), (GRID_SIZE - (2 * border), GRID_SIZE - (2 * border)))
        pygame.draw.rect(SCREEN, BOX_ACTIVE_COLOR, rect)

def drawGrid(blockSize, backgrondColor):
    # Set the background to the specified color
    SCREEN.fill(backgrondColor)

    # Generate a grid and display it on screen
    for x in range(SCREEN_WIDH):
        for y in range(SCREEN_HEIGHT):
            if y <= 1:
                color = RED
            elif y <= 3:
                color = ORANGE
            elif y <= 5:
                color = YELLOW
            elif y <= 7:
                color = GREEN
            else:
                color = WHITE

            posX = x * blockSize
            posY = y * blockSize

            rect = pygame.Rect(posX, posY, blockSize, blockSize)
            pygame.draw.rect(SCREEN, color, rect, 1)
            

# Call the main function to execute the game.
main()