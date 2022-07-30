import pygame as pg 
import settings

class Game:
    level = settings.LEVEL_START
    lives = settings.LIVES_START 

    def __init__(self):
        # Initialise PyGame
        pg.init()
        pg.mixer.init()

        # Setup the game screen
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption(settings.TITLE)

        # Setup the clock
        self.clock = pg.time.Clock()

        # Set the isRunning flag to indicate that the game is running
        self.isRunning = True

    def start(self):
        # Starts a new game.
        # Before we actually start a game, we will need to set up a few things.

        self.drawGrid(settings.GRID_SIZE, settings.BLACK)

        # Create a property that will contain all of the sprites
        self.allSprites = pg.sprite.Group()

        # 1. Add Player Sprites
        # 2. Add Enemy Sprites
        # 3. Add any other sprites

        # Start running the game
        self.run()

    def run(self):
        # Game Loop Code
        # Set the isPlaying flag to indicate that the game is being played
        self.isPlaying = True

        # Loop indefinitely until the isPlaying is set to false.
        # This means that the loop will only exit when the game is no longer being played.
        while self.isPlaying:
            # Set the frames per second
            self.clock.tick(settings.FPS)
            pg.time.delay(100)

            # Capture the player input events
            # i.e. keyboard, mouse, game pad/controller or joystick
            self.events()

            # Update all of the sprites etc.
            # The updates are likely to be in response to the previous events that have been captured.
            # This should update things like sprites to position them accordingly.
            self.update()

            # Re-draw the screen so that the updated postions of spites etc. are reflected on screen.
            self.draw()

    def events(self):
        # Game Loop Events handler
        # Loop through each of the captured events.
        # We likely won't respond to ALL events, but we will check fo specific events and respond accordingly.
        for event in pg.event.get():
            # NOTE:
            # For debuging purposes we will display the event information within the console.
            # This will only be output if the game is currently in debug mode (i.e. DEBUG_MODE = True)
            if settings.DEBUG_MODE == True:
                print (event)

            # Check for closing the window.
            # If the player has clicked the close window button then we will stop playing and running the game.
            if event.type == pg.QUIT:
                self.isPlaying = False
                self.isRunning = False

        # Check for the input action trigger.
        # This is only for testing at the moment. 
        # We will add more complexity to this to make progressing to the next level a bit mor challenging.
        # For now, when the user triggers the input action, move to the next level
        keys = pg.key.get_pressed()
        if keys[settings.INPUT_USER_TRIGGER]:
            self.level += 1

    def update(self):
        # Game Loop Update handler
        # This will update all of the neccesary game assets (i.e. sprites and backgrounds etc.)

        # Update all of the sprites
        self.allSprites.update()

        if(self.level <= settings.MAX_LEVEL):
            # Game is still in progress
            self.drawCharacterBoxes(self.level, self.lives)
        else:
            # The game was WON!
            # Stop the game loop and display the winner screen.
            self.isPlaying = False

    def draw(self):
        # Game Loop draw handler
        # This will re-draw the screen to update it to reflect any changes/updates made in response to input events.
        
        #self.screen.fill(settings.BLACK)
        self.allSprites.draw(self.screen)

        # After redrawing the screen, flip it!
        pg.display.flip()

    def displayStartScreen(self):
        # Show the start screen of the game
        self.screen.fill(settings.YELLOW)
        pg.display.update()

    def displayGameOverScreen(self):
        # Show the Game over screen
        self.screen.fill(settings.RED)
        pg.display.update()

    def drawGrid(self, blockSize, backgrondColor):
        # Set the background to the specified color
        self.screen.fill(backgrondColor)

        # Generate a grid and display it on screen
        for x in range(settings.SCREEN_WIDTH):
            for y in range(settings.SCREEN_HEIGHT):
                if y <= 1:
                    color = settings.RED
                elif y <= 3:
                    color = settings.ORANGE
                elif y <= 5:
                    color = settings.YELLOW
                elif y <= 7:
                    color = settings.GREEN
                else:
                    color = settings.WHITE

                posX = x * blockSize
                posY = y * blockSize

                rect = pg.Rect(posX, posY, blockSize, blockSize)
                pg.draw.rect(self.screen, color, rect, 1)

    def drawCharacterBoxes(self, level, lives):
        # Reduce the lives of the user as they progress through the levels
        # This will make it more challenging to complete as they will have less chances to get it right on the later levels
        if (self.level == 3 or self.level == 4) and self.lives > 4:
            self.lives = 4

        elif (self.level == 5 or self.level == 6) and self.lives > 3:
            self.lives = 3

        elif (self.level == 7 or self.level == 8) and self.lives > 2:
            self.lives = 2

        elif (self.level == 9 or self.level == 10) and self.lives > 1:
            self.lives = 1

        # The border variable will pad the boxes abit to fit nicely within the grid squares
        border = 1

        # The number of lives determine how many active boxes are to be displayed
        # So, we want to create a box for each life the user currently has.
        for i in range(self.lives):
            # Determine where the current box should be placed
            posX = border + (i * settings.GRID_SIZE)
            posY = settings.SCREEN_HEIGHT - settings.GRID_SIZE + border - ((self.level - 1) * settings.GRID_SIZE)

            # Draw the current box on the screen
            rect = pg.Rect((posX, posY), (settings.GRID_SIZE - (2 * border), settings.GRID_SIZE - (2 * border)))
            pg.draw.rect(self.screen, settings.BOX_ACTIVE_COLOR, rect)