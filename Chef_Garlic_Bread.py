from tkinter import *

import arcade


# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1/60

class TitleLogo(arcade.Sprite):
    def __init__(self):
        super().__init__('images/chefgarlicbread.PNG', .6)
        self.center_x = WINDOW_WIDTH/2
        self.top = 485

class SelectPlayer(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.frog1 = None
        self.frog2 = None
        self.frog3 = None
        self.frog4 = None
        self.frog5 = None
        self.title = None
        self.current_page = None
        self.pages = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.frogs = arcade.SpriteList()
        self.frog1 = arcade.Sprite('images/frog1.png', .4)
        self.frog1.top = 350
        self.frog1.center_x = 100
        self.frogs.append(self.frog1)
        self.frog2 = arcade.Sprite('images/frog2.png', .4)
        self.frog2.top = 350
        self.frog2.center_x = 300
        self.frogs.append(self.frog2)
        self.frog3 = arcade.Sprite('images/frog3.png', .4)
        self.frog3.top = 350
        self.frog3.center_x = 500
        self.frogs.append(self.frog3)
        self.frog4 = arcade.Sprite('images/frog4.png', .4)
        self.frog4.top = 200
        self.frog4.center_x = 200
        self.frogs.append(self.frog4)
        self.frog5 = arcade.Sprite('images/frog5.png', .4)
        self.frog5.top = 200
        self.frog5.center_x = 400
        self.frogs.append(self.frog5)
        self.title = TitleLogo()

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.frogs.draw()
        self.title.draw()
        arcade.draw_text("~ Choose your player ~", WINDOW_WIDTH/2, 370, arcade.color.WHITE, 25, font_name="impact", anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if:
            pass
        elif:
            pass
        elif:
            pass
        elif:
            pass
        elif:
            pass

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

def main():
    window = SelectPlayer()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
