import arcade
from arcade.geometry import check_for_collision_with_list
from arcade.geometry import check_for_collision
from arcade.sprite import Sprite
from arcade.buffered_draw_commands import ShapeElementList

# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1 / 60
PLAYER_SPEED = 5


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


class GroceryStore(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.frog = frog
        self.background = arcade.load_texture("images/floor1.jpg")
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.frog)
        self.player_list.rescale(.2)
        self.shelves = arcade.ShapeElementList()
        self.shelves.append(arcade.create_rectangle_filled(100, 100, 50, 50, arcade.color.BLACK))
        self.physics_engine = PhysicsEngineSimple_shapes(self.frog, self.shelves)


    def on_show(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.shelves.draw()
        '''
        arcade.draw_lrtb_rectangle_filled(20, 60, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(80, 120, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(140, 180, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(200, 240, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(260, 340, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(360, 400, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(420, 460, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(480, 520, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(540, 580, 360, 200, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(20, 200, 180, 140, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(220, 380, 180, 140, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(400, 580, 180, 140, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(20, 200, 120, 80, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(220, 380, 120, 80, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(400, 580, 120, 80, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(20, 200, 60, 20, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(220, 380, 60, 20, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(400, 580, 60, 20, arcade.color.BLACK)
        self.frog.draw()
'''
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_list[0].change_y = PLAYER_SPEED
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

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

class PhysicsEngineSimple_shapes:
    """
    This class will move everything, and take care of collisions.
    """

    def __init__(self, player_sprite: Sprite, walls: ShapeElementList):
        """
        Constructor.
        """
        assert(isinstance(player_sprite, Sprite))
        assert(isinstance(walls, ShapeElementList))
        self.player_sprite = player_sprite
        self.walls = walls

    def update(self):
        """
        Move everything and resolve collisions.
        """
        # --- Move in the x direction
        self.player_sprite.center_x += self.player_sprite.change_x

        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            if self.player_sprite.change_x > 0:
                for item in hit_list:
                    self.player_sprite.right = min(item.left,
                                                   self.player_sprite.right)
            elif self.player_sprite.change_x < 0:
                for item in hit_list:
                    self.player_sprite.left = max(item.right,
                                                  self.player_sprite.left)
            else:
                print("Error, collision while player wasn't moving.")

        # --- Move in the y direction
        self.player_sprite.center_y += self.player_sprite.change_y

        # Check for wall hit
        hit_list = \
            check_for_collision_with_list(self.player_sprite,
                                          self.walls)

        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            if self.player_sprite.change_y > 0:
                for item in hit_list:
                    self.player_sprite.top = min(item.bottom,
                                                 self.player_sprite.top)
            elif self.player_sprite.change_y < 0:
                for item in hit_list:
                    self.player_sprite.bottom = max(item.top,
                                                    self.player_sprite.bottom)
            else:
                print("Error, collision while player wasn't moving.")

if __name__ == "__main__":
    main()
