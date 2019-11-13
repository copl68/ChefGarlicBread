import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60


class ChefGarlicBread(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.frog1 = None
        self.frog2 = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.frog1 = arcade.Sprite('images/frog1.png')
        self.frog2 = arcade.Sprite('images/frog2.png')
        self.frog2.postion = (200, 200)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.frog2.draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""


def main():
    window = ChefGarlicBread()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
