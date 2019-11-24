 '''
        for x in NOT_FOUND_INGREDIENTS:
            if self.frog.collides_with_point(self.matched_ingredient_coords["{}".format(x)]) and self.food_deleted == False:
                self.frog.change_x = 0
                self.frog.change_y = 0
                NOT_FOUND_INGREDIENTS.remove("{}".format(x))
                del self.matched_ingredient_coords["{}".format(x)]
                popup_view = Found_Food(self, self.matched_ingredient_coords)
                self.window.show_view(popup_view)
                self.food_deleted = True

class Found_Food(arcade.View):
    def __init__(self, game_view, UGH):
        super().__init__()
        self.game_view = game_view
        self.UGH = UGH

    def on_show(self):
        self.box = arcade.create_rectangle_filled(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH-200, WINDOW_HEIGHT-200, arcade.color.WHITE)

    def on_draw(self):
        self.box.draw()
        arcade.draw_text(str(self.UGH), 50, 220, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(self.game_view)

    def on_update(self, delta_time):
        pass
'''