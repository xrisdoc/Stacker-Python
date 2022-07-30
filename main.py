import pygame as pg
import settings
import game

# Create and initialise a new instance of the game
# This will initialise the PyGame engine and setup the all of the resources we need (i.e Screen and Clock etc.)
# This will start running the game (not playing the game)
g = game.Game()

# Display the startup screen
# On this screen we will wait for the player to confirm when they want to start playing the game.
# We could also provide the player with other option to select here that will take them to some other screens.
g.displayStartScreen()

# TODO: Do we really need isRunning?

# TODO: Maybe we can introduce the concept on an Application and the game runs within the application.
# This would maybe make it easier to include setup/info screens etc.
# So screen like startup and game over would not actaully be part of the game, but part of the applicaiton.

# Loop indefinitely until the game is WON or LOST (or the user Quits).
# The isRunning flag indicates that the game is running but does don necesarily indicate that the game is being played.
# i.e. when isRunning is equal to true, the player:
#  - may be on the game over screen
#  - or, may have paused the game
while g.isRunning:
    # Start a new game!
    # This will setup all of the assets to be displayed on screen ready for when the game starts.
    # i.e. Sprites, background images and music etc.
    g.start()

    # This point will only be reached when the player is no longer playing the game.
    # i.e. they won or lost the game.
    g.displayGameOverScreen()

# Terminate and quit PyGame.
pg.display.quit()
pg.quit()