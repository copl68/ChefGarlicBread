import arcade
import random
import pymunk

# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1 / 60
PLAYER_SPEED = 4
SHELF_COLOR = arcade.color.BLACK
SHELF_COORDS = [[40, 290, 40, 140],
                 [100, 290, 40, 140],
                 [160, 290, 40, 140],
                 [220, 290, 40, 140],
                 [300, 290, 80, 140],
                 [380, 290, 40, 140],
                 [440, 290, 40, 140],
                 [500, 290, 40, 140],
                 [560, 290, 40, 140],
                 [110, 170, 180, 20],
                 [110, 110, 180, 20],
                 [110, 50, 180, 20],
                 [300, 170, 160, 20],
                 [300, 110, 160, 20],
                 [300, 50, 160, 20],
                 [490, 170, 180, 20],
                 [490, 110, 180, 20],
                 [490, 50, 180, 20]]
POSSIBLE_INGREDIENT_LOCATION = [[10, 300],
                       [70, 300],
                       [130, 300],
                       [190, 300],
                       [250, 300],
                       [350, 300],
                       [410, 300],
                       [470, 300],
                       [530, 300],
                       [590, 300],
                       [120, 140],
                       [120, 80],
                       [120, 20],
                       [300, 140],
                       [300, 80],
                       [300, 20],
                       [480, 140],
                       [480, 80],
                       [480, 20]]
INGREDIENT_LIST = ["garlic", "bread", "butter", "parsley", "parmesan"]
NOT_FOUND_INGREDIENTS = INGREDIENT_LIST

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

        view = Assemble()
        self.window.show_view(view)
        '''
        store = GroceryStore(self.chosenFrog)
        self.window.show_view(store)
        '''

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

class GroceryStore(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.frog = frog
        self.frog.center_x = 300
        self.frog.center_y = 200
        self.frog.width = 17
        self.frog.height = 37
        self.background = arcade.load_texture("images/floor1.jpg")
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.frog)
        self.shelves = arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEngineSimple(self.frog, self.shelves)
        self.ingredient_coords = []
        self.ingredient_coord_location = []
        self.matched_ingredient_coords = {}
        self.FirstSetup = True
        self.collected_foods = arcade.SpriteList()
        self.stuff = arcade.SpriteList()

    def on_show(self):
        if len(self.collected_foods) == 5:
            next_view = Assemble()
            self.window.show_view(next_view)
        if self.FirstSetup:
            for shelf in SHELF_COORDS:
                self.shelf_img = arcade.Sprite('images/black.jpg')
                self.shelf_img.center_x = shelf[0]
                self.shelf_img.center_y = shelf[1]
                self.shelf_img.width = shelf[2]
                self.shelf_img.height = shelf[3]
                self.shelves.append(self.shelf_img)
            self.ingredient_coord_location = random.sample(range(0, 19), 5)
            for x in self.ingredient_coord_location:
                self.ingredient_coords.append(POSSIBLE_INGREDIENT_LOCATION[x])

            self.matched_ingredient_coords = self.place_foods(self.ingredient_coords)

            self.food_sprites = arcade.SpriteList()
            self.garlic = arcade.Sprite("images/garlic.png", .2)
            self.garlic.center_x = (WINDOW_WIDTH/10)*1
            self.garlic.center_y = 435
            self.food_sprites.append(self.garlic)
            self.bread = arcade.Sprite("images/bread.png", .15)
            self.bread.center_x = (WINDOW_WIDTH/10)*3
            self.bread.center_y = 435
            self.food_sprites.append(self.bread)
            self.butter = arcade.Sprite("images/butter.png", .35)
            self.butter.center_x = (WINDOW_WIDTH/10)*5
            self.butter.center_y = 435
            self.food_sprites.append(self.butter)
            self.parsley = arcade.Sprite("images/parsley.png", .17)
            self.parsley.center_x = (WINDOW_WIDTH/10)*7
            self.parsley.center_y = 443
            self.food_sprites.append(self.parsley)
            self.parmesan = arcade.Sprite("images/parmesan.png", .17)
            self.parmesan.center_x = (WINDOW_WIDTH/10)*9
            self.parmesan.center_y = 435
            self.food_sprites.append(self.parmesan)
            self.FirstSetup = False

    def place_foods(self, ingredient_coords):
        matched_ingredient_coords = {}
        i = 0
        for x in INGREDIENT_LIST:
            matched_ingredient_coords["{}".format(x)] = ingredient_coords[i]
            i += 1
        return matched_ingredient_coords

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.shelves.draw()
        self.frog.draw()
        self.stuff.draw()
        arcade.draw_rectangle_filled(300, 450, WINDOW_WIDTH, 100, arcade.color.APRICOT)
        arcade.draw_text("Foods Collected:", 20, 485, arcade.color.BLACK, 20, font_name="impact", anchor_x="left", anchor_y="center")
        self.collected_foods.draw()

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
        self.physics_engine.update()
        if self.frog.left < 0:
            self.frog.change_x = 0
        if self.frog.bottom < 0:
            self.frog.change_y = 0
        if self.frog.right > WINDOW_WIDTH:
            self.frog.change_x = 0
        if self.frog.top > WINDOW_HEIGHT - 100:
            self.frog.change_y = 0
        for food in NOT_FOUND_INGREDIENTS:
            if self.frog.collides_with_point(self.matched_ingredient_coords[food]):
                self.frog.change_x = 0
                self.frog.change_y = 0
                NOT_FOUND_INGREDIENTS.remove(food)
                del self.matched_ingredient_coords[food]
                popup_view = Found_Food(self, food)
                self.window.show_view(popup_view)
                if food == "garlic":
                    self.collected_foods.append(self.garlic)
                elif food == "bread":
                    self.collected_foods.append(self.bread)
                elif food == "butter":
                    self.collected_foods.append(self.butter)
                elif food == "parsley":
                    self.collected_foods.append(self.parsley)
                elif food == "parmesan":
                    self.collected_foods.append(self.parmesan)

class Found_Food(arcade.View):
    def __init__(self, game_view, food):
        super().__init__()
        self.game_view = game_view
        self.food = food

    def on_show(self):
        self.box = arcade.create_rectangle_filled(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH - 200,
                                                  WINDOW_HEIGHT - 200, arcade.color.WHITE)
        self.food_img = arcade.Sprite("images/{}.png".format(self.food), .3)
        self.food_img.center_x = WINDOW_WIDTH/2
        self.food_img.center_y = WINDOW_HEIGHT/2

    def on_draw(self):
        self.box.draw()
        self.food_img.draw()
        arcade.draw_text("You found {}!".format(self.food), WINDOW_WIDTH/2, 350, arcade.color.BLACK, 25, font_name="impact",
                         anchor_x="center")
        arcade.draw_text("PRESS <ENTER> TO CONTINUE", WINDOW_WIDTH/2, 130, arcade.color.BLACK, 15,
                         font_name="impact", anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

    def on_update(self, delta_time):
        pass

class Assemble(arcade.View):
    def __init__(self):
        super().__init__()
        # Used for dragging shapes around with the mouse
        self.shape_being_dragged = None
        self.last_mouse_position = None

        self.draw_time = 0
        self.processing_time = 0

        # -- Pymunk
        self.space = pymunk.Space()
        self.space.iterations = 35
        self.space.gravity = (0.0, -900.0)

    def on_show(self):
        arcade.set_background_color(arcade.color.OLD_BURGUNDY)
        self.recipe = arcade.Sprite("images/Recipe.JPG", .5)
        self.recipe.center_x = 120
        self.recipe.center_y = 175
        self.recipe.height = 325

        self.collected_foods = arcade.SpriteList()
        self.garlic = arcade.Sprite("images/garlic.png", .2)
        self.garlic.center_x = (WINDOW_WIDTH / 10) * 1
        self.garlic.center_y = 400
        self.collected_foods.append(self.garlic)
        self.bread = arcade.Sprite("images/bread.png", .15)
        self.bread.center_x = (WINDOW_WIDTH / 10) * 3
        self.bread.center_y = 400
        self.collected_foods.append(self.bread)
        self.butter = arcade.Sprite("images/butter.png", .35)
        self.butter.center_x = (WINDOW_WIDTH / 10) * 5
        self.butter.center_y = 400
        self.collected_foods.append(self.butter)
        self.parsley = arcade.Sprite("images/parsley.png", .17)
        self.parsley.center_x = (WINDOW_WIDTH / 10) * 7
        self.parsley.center_y = 408
        self.collected_foods.append(self.parsley)
        self.parmesan = arcade.Sprite("images/parmesan.png", .17)
        self.parmesan.center_x = (WINDOW_WIDTH / 10) * 9
        self.parmesan.center_y = 400
        self.collected_foods.append(self.parmesan)
        self.collected_foods.center_y = 420

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(WINDOW_WIDTH/2, 425, WINDOW_WIDTH, 150, arcade.color.APRICOT)
        self.recipe.draw()
        self.collected_foods.draw()
        arcade.draw_text("Following the recipe, click and drag items into \nthe box to assemble the garlic bread", 300, 447, arcade.color.BLACK, 20,
                         anchor_x="center", align="center", font_name="impact")

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # See if we clicked on anything
            for food in self.collected_foods:
                if food.collides_with_point([x, y]):
                    self.shape_being_dragged = food
                    break
            '''
            # If we did, remember what we clicked on
            if len(shape_list) > 0:
                self.shape_being_dragged = shape_list[0]
            '''

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Release the item we are holding (if any)
            self.shape_being_dragged = None

    def on_mouse_motion(self, x, y, dx, dy):
        if self.shape_being_dragged is not None:
            # If we are holding an object, move it with the mouse
            #self.last_mouse_position = x, y
            center_x = self.shape_being_dragged.center_x
            center_y = self.shape_being_dragged.center_y
            self.shape_being_dragged.center_x = center_x + dx
            self.shape_being_dragged.center_y = center_y + dy
            #self.shape_being_dragged.shape.body.velocity = dx * 20, dy * 20

    def on_update(self, delta_time):
        '''
        if self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.position = self.last_mouse_position
            self.shape_being_dragged.shape.body.velocity = 0, 0
        '''

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
