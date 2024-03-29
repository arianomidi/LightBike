from utils.Util import *
from game.Game import Game
from game.gui.Menu import Menu

import pygame


class LightBike(object):
    def __init__(self):
        pygame.init()

        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Light Bike")
        pygame.mouse.set_visible(True)

        # Create our objects and set the data
        self.done = False
        self.clock = pygame.time.Clock()

        self.game = None
        self.menu = Menu()


    def run(self):
        # Main game loop
        while not self.done:

            if not self.menu.game_started:
                # Process events (keystrokes, mouse clicks, etc)
                self.done = self.menu.process_events()

                # Draw the current frame
                self.menu.display_frame(self.screen)
            else:
                if self.game == None:
                    self.game = Game(self.menu.player_attributes)

                # Process events (keystrokes, mouse clicks, etc)
                self.done = self.game.process_events()

                # If game is over and players select to go to menu
                if self.game.menu_selected:
                    self.game = None
                    self.menu.return_to_player_selection()
                    continue

                # # Update object positions, check for collisions
                self.game.run_logic()

                # Draw the current frame
                self.game.display_frame(self.screen)

            # Pause for the next frame
            self.clock.tick(FPS)


        # Close window and exit
        pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    LightBike().run()
