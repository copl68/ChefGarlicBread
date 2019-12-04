import arcade
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1 / 60
PLAYER_SPEED = 4.5
SCROLLING_MARGIN = 100
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
NOT_FOUND_INGREDIENTS = INGREDIENT_LIST.copy()

'''Creates and positions the title of the game'''
class TitleLogo(arcade.Sprite):
    def __init__(self):
        super().__init__('images/chefgarlicbread.PNG', .6)
        self.center_x = WINDOW_WIDTH / 2
        self.top = 485

'''The intro and player selection screen'''
class StartView(arcade.View):
    def __init__(self):
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

    '''Creates background color and calls functions to create sprites'''
    def on_show(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.create_frogs()
        self.title = TitleLogo()

    '''The player sprites and brief instructions'''
    def on_draw(self):
        arcade.start_render()
        self.frogs.draw()
        self.title.draw()
        arcade.draw_text("~ Choose your player ~", WINDOW_WIDTH / 2, 370, arcade.color.WHITE, 25, font_name="impact",
                         anchor_x="center")

    '''
    Determines which frog the player selects and saves it for later. 
    It then continues to the next view, which is the instructions for the grocery store.
    '''
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

        store = GroceryStoreInstructions(self.chosenFrog)
        self.window.show_view(store)

    '''Creates and positions all of the frog sprites'''
    def create_frogs(self):
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

'''The view for the instructions of what to do in the grocery store view'''
class GroceryStoreInstructions(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.background_color = arcade.color.APRICOT
        self.frog = frog

    '''Sets the color of the background'''
    def on_show(self):
        arcade.set_background_color(self.background_color)

    '''Draws the instructions on the screen'''
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Use the arrow keys to \n search the grocery store for \n the needed ingredients", WINDOW_WIDTH/2,
                         300, arcade.color.BLACK, 40, anchor_x="center", anchor_y="center", align="center", font_name="impact")
        arcade.draw_text("Press <ENTER> to start", WINDOW_WIDTH/2, 150, arcade.color.RED, 25, anchor_x="center", font_name="impact")

    '''Moves onto the next view once the player hits the "Enter" key'''
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            store = GroceryStore(self.frog)
            self.window.show_view(store)

'''The grocery store, where the player will search for ingredients to make garlic bread'''
class GroceryStore(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.frog = frog
        self.frog.center_x = 300
        self.frog.center_y = 200
        self.frog.width = 16
        self.frog.height = 37
        self.frog.boundary_left = 0
        self.frog.boundary_right = WINDOW_WIDTH
        self.frog.boundary_top = 400
        self.frog.boundary_bottom = 0
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
        self.NOT_FOUND_INGREDIENTS_COPY = NOT_FOUND_INGREDIENTS.copy()

    '''
    On the first call, it will call a function to setup sprites and foods in the store. 
    Continues onto the next view once all foods are found
    '''
    def on_show(self):
        if len(self.collected_foods) == 5:
            next_view = Assemble(self.frog)
            self.window.show_view(next_view)
        if self.FirstSetup:
            self.shelf_and_food_setup()

    '''Creates the shelves and food sprites. Determines that the first iteration of the on_show function has ended. '''
    def shelf_and_food_setup(self):
        for shelf in SHELF_COORDS:
            self.shelf_img = arcade.Sprite('images/black.jpg')
            self.shelf_img.center_x = shelf[0]
            self.shelf_img.center_y = shelf[1]
            self.shelf_img.width = shelf[2]
            self.shelf_img.height = shelf[3]
            self.shelves.append(self.shelf_img)

        self.assign_food_locations()

        self.food_sprites = arcade.SpriteList()
        self.garlic = arcade.Sprite("images/garlic.png", .2)
        self.garlic.center_x = (WINDOW_WIDTH / 10) * 1
        self.garlic.center_y = 435
        self.food_sprites.append(self.garlic)
        self.bread = arcade.Sprite("images/bread.png", .15)
        self.bread.center_x = (WINDOW_WIDTH / 10) * 3
        self.bread.center_y = 435
        self.food_sprites.append(self.bread)
        self.butter = arcade.Sprite("images/butter.png", .35)
        self.butter.center_x = (WINDOW_WIDTH / 10) * 5
        self.butter.center_y = 435
        self.food_sprites.append(self.butter)
        self.parsley = arcade.Sprite("images/parsley.png", .17)
        self.parsley.center_x = (WINDOW_WIDTH / 10) * 7
        self.parsley.center_y = 443
        self.food_sprites.append(self.parsley)
        self.parmesan = arcade.Sprite("images/parmesan.png", .17)
        self.parmesan.center_x = (WINDOW_WIDTH / 10) * 9
        self.parmesan.center_y = 435
        self.food_sprites.append(self.parmesan)

        self.FirstSetup = False

    '''Selects the coordinates with will later be assigned to foods'''
    def assign_food_locations(self):
        self.ingredient_coord_location = random.sample(range(0, 19), 5)
        for x in self.ingredient_coord_location:
            self.ingredient_coords.append(POSSIBLE_INGREDIENT_LOCATION[x])
        self.matched_ingredient_coords = self.place_foods(self.ingredient_coords)

    '''Assigns the needed foods to the previously selected coordinates in the grocery store'''
    def place_foods(self, ingredient_coords):
        matched_ingredient_coords = {}
        i = 0
        for x in INGREDIENT_LIST:
            matched_ingredient_coords["{}".format(x)] = ingredient_coords[i]
            i += 1
        return matched_ingredient_coords

    "Draws the shelves, character, and bar of collected foods to the screen"
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT, self.background)
        self.shelves.draw()
        self.frog.draw()
        arcade.draw_rectangle_filled(300, 450, WINDOW_WIDTH, 100, arcade.color.APRICOT)
        arcade.draw_text("Foods Collected:", 20, 485, arcade.color.BLACK, 20, font_name="impact", anchor_x="left", anchor_y="center")
        self.collected_foods.draw()

    '''Used for movement of character based off of input from the arrow keys'''
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.frog.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.frog.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.frog.change_x = PLAYER_SPEED

    '''Stops moving the character once the arrow keys are released'''
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.frog.change_y = 0
        elif key == arcade.key.DOWN:
            self.frog.change_y = 0
        elif key == arcade.key.LEFT:
            self.frog.change_x = 0
        elif key == arcade.key.RIGHT:
            self.frog.change_x = 0

    '''
    Sets up the physics engine that will handle the collisions with the shelves.
    Makes sure that the player cannot move off the screen. 
    '''
    def on_update(self, delta_time):
        self.physics_engine.update()
        if self.frog.left < self.frog.boundary_left:
            self.frog.change_x = 0
            self.frog.left = self.frog.boundary_left
        if self.frog.bottom < self.frog.boundary_bottom:
            self.frog.change_y = 0
            self.frog.bottom = self.frog.boundary_bottom
        if self.frog.right > self.frog.boundary_right:
            self.frog.change_x = 0
            self.frog.right = self.frog.boundary_right
        if self.frog.top > self.frog.boundary_top:
            self.frog.change_y = 0
            self.frog.top = self.frog.boundary_top

        self.update_found_foods()

    '''
    Checks to see if the player has collided with the coordinate of a food. 
    If they have, add it to the list of foods that have been found. 
    '''
    def update_found_foods(self):
        for food in self.NOT_FOUND_INGREDIENTS_COPY:
            if self.frog.collides_with_point(self.matched_ingredient_coords[food]):
                self.frog.change_x = 0
                self.frog.change_y = 0
                self.NOT_FOUND_INGREDIENTS_COPY.remove(food)
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

'''THe view which tells the player the food they have found in the grocery store'''
class Found_Food(arcade.View):
    def __init__(self, game_view, food):
        super().__init__()
        self.game_view = game_view
        self.food = food

    '''Creates a popup window and sprite of the food that was found'''
    def on_show(self):
        self.box = arcade.create_rectangle_filled(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH - 200,
                                                  WINDOW_HEIGHT - 200, arcade.color.WHITE)
        self.food_img = arcade.Sprite("images/{}.png".format(self.food), .3)
        self.food_img.center_x = WINDOW_WIDTH/2
        self.food_img.center_y = WINDOW_HEIGHT/2

    '''Draws the popup window and adds words describing what was found and how to move on'''
    def on_draw(self):
        self.box.draw()
        self.food_img.draw()
        arcade.draw_text("You found {}!".format(self.food), WINDOW_WIDTH/2, 350, arcade.color.BLACK, 25, font_name="impact",
                         anchor_x="center")
        arcade.draw_text("PRESS <ENTER> TO CONTINUE", WINDOW_WIDTH/2, 130, arcade.color.BLACK, 15,
                         font_name="impact", anchor_x="center")

    '''Progresses to the next view if the "Enter" key is pressed'''
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

'''The view where the player can assemble the garlic bread'''
class Assemble(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.shape_being_dragged = None
        self.last_mouse_position = None
        self.foi = None
        self.bread_to_draw = None
        self.mouse_released = None
        self.bread_x_pos = 400
        self.bread_y_pos = 90
        self.bread_scale = .25
        self.made = False
        self.frog = frog
        self.first_run = True
        self.collected_foods = arcade.SpriteList()

    '''
    Creates a plate and recipe sprite as well as creates a dictionary to make it easy to find which 
    bread sprite should be printed next
    '''
    def on_show(self):
        arcade.set_background_color(arcade.color.OLD_BURGUNDY)
        self.recipe = arcade.Sprite("images/Recipe.JPG", .5)
        self.recipe.center_x = 120
        self.recipe.center_y = 175
        self.recipe.height = 325
        self.plate = arcade.Sprite("images/plate.png", .5)
        self.plate.center_x = 400
        self.plate.center_y = 85
        self.create_ingredient_bar()
        self.create_breads()

        self.bread_progression = {None: self.bread1,
                                  self.bread1: self.bread2,
                                  self.bread2: self.bread3,
                                  self.bread3: self.bread4,
                                  self.bread4: self.bread5,
                                  self.bread5: self.bread5}
        self.first_run = False

    '''Draws the title bar and ingredients to use in the recipe. If there is a bread to draw, it is drawn'''
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(WINDOW_WIDTH/2, 425, WINDOW_WIDTH, 150, arcade.color.APRICOT)
        self.recipe.draw()
        self.collected_foods.draw()
        arcade.draw_text("Following the recipe, click and drag items into \nthe box to assemble the garlic bread", 300, 447, arcade.color.BLACK, 20,
                         anchor_x="center", align="center", font_name="impact")
        self.plate.draw()
        self.create_input_box()

        if self.bread_to_draw:
            self.bread_to_draw.draw()

    '''
    Keeps track of which food was clicked on if one was clicked in the first place. Progresses to the next view
    if the bread is completely made
    '''
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_released = False
            for food in self.collected_foods:
                if food.collides_with_point([x, y]):
                    self.shape_being_dragged = food
                    break

            if self.made and (300<x<500 and 200<y<330):
                eat_view = Eat(self.frog)
                self.window.show_view(eat_view)

    '''When the mouse is released, the food that was previously being dragged is no longer being dragged'''
    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_released = True
            self.shape_being_dragged = None

    '''When the mouse moves, the food being dragged will move with it'''
    def on_mouse_motion(self, x, y, dx, dy):
        if self.shape_being_dragged is not None:
            center_x = self.shape_being_dragged.center_x
            center_y = self.shape_being_dragged.center_y
            self.shape_being_dragged.center_x = center_x + dx
            self.shape_being_dragged.center_y = center_y + dy

    '''
    Checks to make sure that the correct food is dragged into the given area. If it is, the bread that
    should be drawn is updated. If there are no foods left, the garlic is designated "made"
    '''
    def on_update(self, delta_time):
        #foi stands for "food of interest"
        if self.collected_foods:
            self.foi = self.collected_foods[0]
            if self.mouse_released == True:
                if self.foi.left >= 300 and self.foi.right <= 500 and self.foi.top < 320 and self.foi.bottom > 200:
                    self.bread_to_draw = self.bread_progression[self.bread_to_draw]
                    self.collected_foods.remove(self.foi)
                else:
                    self.create_ingredient_bar()
        elif not self.collected_foods:
            self.made = True

    '''Creates the area for where the foods should be dragged. Turns into a button once the garlic bread is made'''
    def create_input_box(self):
        if not self.made:
            arcade.draw_lrtb_rectangle_outline(300, 500, 330, 200, arcade.color.WHITE, 3)
        elif self.made:
            arcade.draw_lrtb_rectangle_filled(300, 500, 330, 200, arcade.color.WHITE)
            arcade.draw_text("EAT!", 400, 260, arcade.color.CANDY_APPLE_RED, 50, anchor_x="center", anchor_y="center", font_name="impact")
            arcade.draw_text("Click to", 400, 305, arcade.color.BLACK, 12, anchor_x="center", anchor_y="center", font_name="impact")

    '''Creates the sprites for the garlic bread being made'''
    def create_breads(self):
        self.bread1 = arcade.Sprite("images/bread1.png", self.bread_scale, center_x=self.bread_x_pos,
                                    center_y=self.bread_y_pos)
        self.bread2 = arcade.Sprite("images/bread2.png", self.bread_scale, center_x=self.bread_x_pos,
                                    center_y=self.bread_y_pos)
        self.bread3 = arcade.Sprite("images/bread3.png", self.bread_scale, center_x=399, center_y=self.bread_y_pos)
        self.bread4 = arcade.Sprite("images/bread4.png", self.bread_scale, center_x=self.bread_x_pos,
                                    center_y=self.bread_y_pos)
        self.bread5 = arcade.Sprite("images/bread5.png", self.bread_scale, center_x=self.bread_x_pos,
                                    center_y=self.bread_y_pos)

    '''This creates the food sprites'''
    def create_ingredient_bar(self):
        if self.first_run == True:
            self.garlic = arcade.Sprite("images/garlic.png", .2)
            self.bread = arcade.Sprite("images/bread.png", .15)
            self.butter = arcade.Sprite("images/butter.png", .35)
            self.parsley = arcade.Sprite("images/parsley.png", .17)
            self.parmesan = arcade.Sprite("images/parmesan.png", .17)
            self.collected_foods.append(self.bread)
            self.collected_foods.append(self.butter)
            self.collected_foods.append(self.garlic)
            self.collected_foods.append(self.parsley)
            self.collected_foods.append(self.parmesan)
        self.include_only_remaining()

    '''
    This positions and puts the remaining foods in the tool bar at the top depending on which foods have
    been used already
    '''
    def include_only_remaining(self):
        if len(self.collected_foods) >= 1:
            self.parmesan.center_x = (WINDOW_WIDTH / 10) * 9
            self.parmesan.center_y = 400
            if len(self.collected_foods) >= 2:
                self.parsley.center_x = (WINDOW_WIDTH / 10) * 7
                self.parsley.center_y = 408
                if len(self.collected_foods) >= 3:
                    self.garlic.center_x = (WINDOW_WIDTH / 10) * 1
                    self.garlic.center_y = 400
                    if len(self.collected_foods) >= 4:
                        self.butter.center_x = (WINDOW_WIDTH / 10) * 5
                        self.butter.center_y = 400
                        if len(self.collected_foods) >= 5:
                            self.bread.center_x = (WINDOW_WIDTH / 10) * 3
                            self.bread.center_y = 400
        self.collected_foods.center_y = 420

'''This is the view where the player can eat the garlic bread they just made'''
class Eat(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.title = TitleLogo()
        self.frog = frog
        self.frog.height = 250
        self.frog.width = 150
        self.frog.center_x = 500
        self.frog.center_y = 140
        self.bread_x_pos = 225
        self.bread_y_pos = 130
        self.bread_scale = .3
        self.bread_index_to_draw = 0

    '''This sets the background color and creates and positions a speech bubble and plate sprite'''
    def on_show(self):
        arcade.set_background_color(arcade.color.OLD_BURGUNDY)
        self.speech_bubble = arcade.Sprite("images/speech_bubble.png")
        self.speech_bubble.height = 120
        self.speech_bubble.width = 500
        self.speech_bubble.center_x = 300
        self.speech_bubble.center_y = 335

        self.plate = arcade.Sprite("images/plate.png", .5)
        self.plate.center_x = 215
        self.plate.center_y = 100

        self.create_breads()

    '''This draws all the sprites and makes a "play again" box appear once the bread is gone'''
    def on_draw(self):
        arcade.start_render()
        self.title.draw()
        self.frog.draw()
        self.speech_bubble.draw()
        arcade.draw_text("Press <SPACE> to eat the garlic bread", 300, 335, arcade.color.BLACK, 20, anchor_x="center",
                         font_name="impact")
        self.plate.draw()
        if self.bread_index_to_draw <= 5:
            self.eaten_bread[self.bread_index_to_draw].draw()
        elif self.bread_index_to_draw >= 6:
            arcade.draw_lrtb_rectangle_filled(110, 320, 275, 215, arcade.color.CHARTREUSE)
            arcade.draw_text("Play Again", 215, 245, arcade.color.BLACK, 20, anchor_x="center",
                             anchor_y="center", font_name="impact")

    '''
    When the space key is hit, the variable increments by one and is used to find the index of the 
    correct bread to print
    '''
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.bread_index_to_draw += 1

    '''Once the bread is gone and the player clicks on the "play again" button, the game restarts'''
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.bread_index_to_draw >= 6 and 110<x<320 and 215<y<275:
                restart = StartView()
                self.window.show_view(restart)

    '''This creates the sprites of bread with bites taken'''
    def create_breads(self):
        self.eaten_bread = arcade.SpriteList()
        self.bread1 = arcade.Sprite("images/bread5.png", self.bread_scale)
        self.bread1.center_x = self.bread_x_pos
        self.bread1.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread1)
        self.bread2 = arcade.Sprite("images/bread_eat1.png", self.bread_scale)
        self.bread2.center_x = self.bread_x_pos
        self.bread2.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread2)
        self.bread3 = arcade.Sprite("images/bread_eat2.png", self.bread_scale)
        self.bread3.center_x = self.bread_x_pos
        self.bread3.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread3)
        self.bread4 = arcade.Sprite("images/bread_eat3.png", self.bread_scale)
        self.bread4.center_x = self.bread_x_pos
        self.bread4.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread4)
        self.bread5 = arcade.Sprite("images/bread_eat4.png", self.bread_scale)
        self.bread5.center_x = self.bread_x_pos
        self.bread5.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread5)
        self.bread6 = arcade.Sprite("images/bread_eat5.png", self.bread_scale)
        self.bread6.center_x = self.bread_x_pos
        self.bread6.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread6)

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
