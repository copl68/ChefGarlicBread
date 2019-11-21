import arcade

# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1 / 60
PLAYER_SPEED = 5
SHELF_COLOR = arcade.color.BLACK
SHELF_COORDS = [[40, 280, 40, 160],
                 [100, 280, 40, 160],
                 [160, 280, 40, 160],
                 [220, 280, 40, 160],
                 [300, 280, 80, 160],
                 [380, 280, 40, 160],
                 [440, 280, 40, 160],
                 [500, 280, 40, 160],
                 [560, 280, 40, 160],
                 [110, 160, 180, 40],
                 [110, 100, 180, 40],
                 [110, 40, 180, 40],
                 [300, 160, 160, 40],
                 [300, 100, 160, 40],
                 [300, 40, 60, 40],
                 [490, 160, 180, 40],
                 [490, 100, 180, 40],
                 [490, 40, 180, 40]]

class TitleLogo(arcade.Sprite):
    def __init__(self):
        super().__init__('images/chefgarlicbread.PNG', .6)
        self.center_x = WINDOW_WIDTH / 2
        self.top = 485

class StartView(arcade.View):
    def __init__(self):
        """ Initialize variables """
        super().__init__()
        self.frogs = None
        self.frog1 = None
        self.frog2 = None
        self.frog3 = None
        self.frog4 = None
        self.frog5 = None
        self.title = None
        self.current_page = None
        self.pages = None
        self.chosenFrog = None
        self.window = None

    def on_show(self):
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
        arcade.draw_text("~ Choose your player ~", WINDOW_WIDTH / 2, 370, arcade.color.WHITE, 25, font_name="impact",
                         anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.frogs[0].collides_with_point([x, y]):
            self.chosenFrog = self.frogs[0]
        elif self.frogs[1].collides_with_point([x, y]):
            self.chosenFrog = self.frogs[1]
        elif self.frogs[2].collides_with_point([x, y]):
            self.chosenFrog = self.frogs[2]
        elif self.frogs[3].collides_with_point([x, y]):
            self.chosenFrog = self.frogs[3]
        elif self.frogs[4].collides_with_point([x, y]):
            self.chosenFrog = self.frogs[4]

        store = GroceryStore(self.chosenFrog)
        self.window.show_view(store)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

class Shelf(arcade.Sprite):
    def __init__(self, x_center, y_center, width, height):
        super().__init__()
        self.texture = arcade.create_rectangle_filled(x_center, y_center, width, height, SHELF_COLOR)

class GroceryStore(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.frog = frog
        self.frog.center_x = 300
        self.frog.center_y = 450
        self.background = arcade.load_texture("images/floor1.jpg")
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.frog)
        self.player_list.rescale(.2)
        self.shelves = arcade.SpriteList()
        #self.physics_engine = arcade.PhysicsEngineSimple(self.frog, self.shelves)

    def on_show(self):
        for shelf in SHELF_COORDS:
            self.shelves.append(Shelf(shelf[0], shelf[1], shelf[2], shelf[3]))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.shelves.draw()
        self.frog.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.frog.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.frog.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.frog.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog.change_y = 0
        elif key == arcade.key.DOWN:
            self.frog.change_y = 0
        elif key == arcade.key.LEFT:
            self.frog.change_x = 0
        elif key == arcade.key.RIGHT:
            self.frog.change_x = 0

    def on_update(self, delta_time):
        pass
        #self.physics_engine.update()

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
