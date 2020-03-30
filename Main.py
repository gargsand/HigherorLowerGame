import sys

# 1 - Import packages
import pygame
import pygwidgets
from Constants import *
from Game import *
from pygame.locals import *

# 3 - Initialize the world
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sounds,  etc.
backgroundImage = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)
oGame = Game(window)

while True:
    try:
        # Handle Event
        for event in pygame.event.get():
            if ((event.type == QUIT) or
                    ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
                    (quitButton.handleEvent(event))):
                pygame.quit()
                sys.exit()

            if newGameButton.handleEvent(event):
                oGame.reset()
                lowerButton.enable()
                higherButton.enable()

            if higherButton.handleEvent(event):
                gameOver = oGame.hitHigherOrLower(HIGHER)
                if gameOver:
                    higherButton.disable()
                    lowerButton.disable()

            if lowerButton.handleEvent(event):
                gameOver = oGame.hitHigherOrLower(LOWER)
                if gameOver:
                    higherButton.disable()
                    lowerButton.disable()

        # Clear the screen before drawing it again
        backgroundImage.draw()

        # Draw the screen elements
        # Tell the game to draw itself
        oGame.draw()
        # draw remaining user interface components
        newGameButton.draw()
        higherButton.draw()
        lowerButton.draw()
        quitButton.draw()

        # 11 - Update the screen
        pygame.display.update()

        # 12 - Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)
    except Exception:
        raise Exception(" Unexpected Exception")
