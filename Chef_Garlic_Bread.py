import random

import arcade


# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.EMINENCE
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60


class ChefGarlicBread(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.frog1 = None
        self.frog2 = None
        self.frog3 = None
        self.frog4 = None
        self.frog5 = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.frogs = arcade.SpriteList()
        self.frog1 = arcade.Sprite('images/frog1.png', .4)
        self.frog1.position = (100, 400)
        self.frogs.append(self.frog1)
        self.frog2 = arcade.Sprite('images/frog2.png', .4)
        self.frog2.position = (200, 400)
        self.frogs.append(self.frog2)
        self.frog3 = arcade.Sprite('images/frog3.png', .4)
        self.frog3.position = (300, 400)
        self.frogs.append(self.frog3)
        self.frog4 = arcade.Sprite('images/frog4.png', .4)
        self.frog4.position = (400, 400)
        self.frog5 = arcade.Sprite('images/frog5.png', .4)
        self.frog5.position = (500, 400)
        self.frogs.append(self.frog5)


    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.frogs.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""


def main():
    window = ChefGarlicBread()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
