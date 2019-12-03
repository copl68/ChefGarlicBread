import arcade
import random

# Define constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.OLD_BURGUNDY
GAME_TITLE = "Chef Garlic Bread"
GAME_SPEED = 1 / 60
PLAYER_SPEED = 4
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

        '''
        view = Eat(self.chosenFrog)
        self.window.show_view(view)
        '''
        store = GroceryStoreInstructions(self.chosenFrog)
        self.window.show_view(store)


    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

class GroceryStoreInstructions(arcade.View):
    def __init__(self, frog):
        super().__init__()
        self.background_color = arcade.color.APRICOT
        self.frog = frog

    def on_show(self):
        arcade.set_background_color(self.background_color)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Use the arrow keys to \n search the grocery store for \n the needed ingredients", WINDOW_WIDTH/2,
                         300, arcade.color.BLACK, 40, anchor_x="center", anchor_y="center", align="center", font_name="impact")
        arcade.draw_text("Press <ENTER> to start", WINDOW_WIDTH/2, 150, arcade.color.RED, 25, anchor_x="center", font_name="impact")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            store = GroceryStore(self.frog)
            self.window.show_view(store)

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
        self.view_left = 0
        self.view_bottom = 0
        self.NOT_FOUND_INGREDIENTS_COPY = NOT_FOUND_INGREDIENTS

    def on_show(self):
        if len(self.collected_foods) == 5:
            next_view = Assemble(self.frog)
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

        '''
        window_left = self.frog.center_x - 100
        window_right = self.frog.center_x + 100
        window_bottom = self.frog.center_y - 100
        window_top = self.frog.center_y + 100
        left = 0
        right = 0
        bottom = 0
        top = 0
        if window_left > 0 and window_right < WINDOW_WIDTH and window_bottom > 0 and window_top < WINDOW_HEIGHT:
            arcade.set_viewport(window_left, window_right, window_bottom, window_top)
        else:
            if window_left < 0:
                left = 0
                right = 200
                #arcade.set_viewport(0, 200, window_bottom, window_top)
            elif window_right > WINDOW_WIDTH:
                left = WINDOW_WIDTH - 200
                right = WINDOW_WIDTH
                #arcade.set_viewport(WINDOW_WIDTH - 200, WINDOW_WIDTH, window_bottom, window_top)
            if window_bottom < 0:
                bottom = 0
                top = 200
                #arcade.set_viewport(window_right, window_left, 0, 200)
            elif window_top > WINDOW_HEIGHT:
                bottom = WINDOW_HEIGHT - 200
                top = WINDOW_HEIGHT
                #arcade.set_viewport(window_right, window_left, WINDOW_HEIGHT - 200, WINDOW_HEIGHT)
            arcade.set_viewport(left, right, bottom, top)

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        changed = False

        left_boundary = self.view_left + SCROLLING_MARGIN
        if self.frog.left < left_boundary:
            self.view_left -= left_boundary - self.frog.left
            changed = True

        right_boundary = self.view_left + WINDOW_WIDTH - SCROLLING_MARGIN
        if self.frog.right > right_boundary:
            self.view_left += self.frog.right - right_boundary
            changed = True

        top_boundary = self.view_bottom + WINDOW_HEIGHT - SCROLLING_MARGIN
        if self.frog.top > top_boundary:
            self.view_bottom += self.frog.top - top_boundary
            changed = True

        bottom_boundary = self.view_bottom + SCROLLING_MARGIN
        if self.frog.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.frog.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        
        if changed:
            arcade.set_viewport(self.view_left,
                                WINDOW_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                WINDOW_HEIGHT + self.view_bottom - 1)
        '''

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
    def __init__(self, frog):
        super().__init__()
        # Used for dragging shapes around with the mouse
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

    def on_show(self):
        arcade.set_background_color(arcade.color.OLD_BURGUNDY)
        self.recipe = arcade.Sprite("images/Recipe.JPG", .5)
        self.recipe.center_x = 120
        self.recipe.center_y = 175
        self.recipe.height = 325

        self.create_ingredient_bar()

        self.plate = arcade.Sprite("images/plate.png", .5)
        self.plate.center_x = 400
        self.plate.center_y = 85

        self.bread1 = arcade.Sprite("images/bread1.png", self.bread_scale, center_x=self.bread_x_pos, center_y=self.bread_y_pos)
        self.bread2 = arcade.Sprite("images/bread2.png", self.bread_scale, center_x=self.bread_x_pos, center_y=self.bread_y_pos)
        self.bread3 = arcade.Sprite("images/bread3.png", self.bread_scale, center_x=399, center_y=self.bread_y_pos)
        self.bread4 = arcade.Sprite("images/bread4.png", self.bread_scale, center_x=self.bread_x_pos, center_y=self.bread_y_pos)
        self.bread5 = arcade.Sprite("images/bread5.png", self.bread_scale, center_x=self.bread_x_pos, center_y=self.bread_y_pos)

        self.bread_progression = {None: self.bread1,
                                  self.bread1: self.bread2,
                                  self.bread2: self.bread3,
                                  self.bread3: self.bread4,
                                  self.bread4: self.bread5,
                                  self.bread5: self.bread5}
        self.first_run = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(WINDOW_WIDTH/2, 425, WINDOW_WIDTH, 150, arcade.color.APRICOT)
        self.recipe.draw()
        self.collected_foods.draw()
        arcade.draw_text("Following the recipe, click and drag items into \nthe box to assemble the garlic bread", 300, 447, arcade.color.BLACK, 20,
                         anchor_x="center", align="center", font_name="impact")
        self.plate.draw()
        if not self.made:
            arcade.draw_lrtb_rectangle_outline(300, 500, 330, 200, arcade.color.WHITE, 3)
        elif self.made:
            arcade.draw_lrtb_rectangle_filled(300, 500, 330, 200, arcade.color.WHITE)
            arcade.draw_text("EAT!", 400, 260, arcade.color.CANDY_APPLE_RED, 50, anchor_x="center", anchor_y="center", font_name="impact")
            arcade.draw_text("Click to", 400, 305, arcade.color.BLACK, 12, anchor_x="center", anchor_y="center", font_name="impact")
        if self.bread_to_draw:
            self.bread_to_draw.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # See if we clicked on anything
            self.mouse_released = False
            for food in self.collected_foods:
                if food.collides_with_point([x, y]):
                    self.shape_being_dragged = food
                    break

            if self.made and (300<x<500 and 200<y<330):
                eat_view = Eat(self.frog)
                self.window.show_view(eat_view)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_released = True
            # Release the item we are holding (if any)
            self.shape_being_dragged = None

    def on_mouse_motion(self, x, y, dx, dy):
        if self.shape_being_dragged is not None:
            # If we are holding an object, move it with the mouse
            center_x = self.shape_being_dragged.center_x
            center_y = self.shape_being_dragged.center_y
            self.shape_being_dragged.center_x = center_x + dx
            self.shape_being_dragged.center_y = center_y + dy

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

        self.eaten_bread = arcade.SpriteList()
        self.bread1 = arcade.Sprite("images/bread5.png", self.bread_scale)
        self.bread1.center_x = self.bread_x_pos
        self.bread1.center_y = self.bread_y_pos
        self.eaten_bread.append(self.bread1)
        self.bread2  = arcade.Sprite("images/bread_eat1.png", self.bread_scale)
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

        if self.bread_index_to_draw == 5:
            pass


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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.bread_index_to_draw += 1

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.bread_index_to_draw >= 6 and 110<x<320 and 215<y<275:
                restart = StartView()
                self.window.show_view(restart)

    def on_update(self, delta_time):
        pass

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
