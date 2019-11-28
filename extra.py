if self.FirstSetup:
    self.one = arcade.Sprite("images/black.jpg", .1)
    self.one.center_x = self.matched_ingredient_coords["garlic"][0]
    self.one.center_y = self.matched_ingredient_coords["garlic"][1]
    self.stuff.append(self.one)
    self.two = arcade.Sprite("images/black.jpg", .1)
    self.two.center_x = self.matched_ingredient_coords["butter"][0]
    self.two.center_y = self.matched_ingredient_coords["butter"][1]
    self.stuff.append(self.two)
    self.three = arcade.Sprite("images/black.jpg", .1)
    self.three.center_x = self.matched_ingredient_coords["bread"][0]
    self.three.center_y = self.matched_ingredient_coords["bread"][1]
    self.stuff.append(self.three)
    self.four = arcade.Sprite("images/black.jpg", .1)
    self.four.center_x = self.matched_ingredient_coords["parsley"][0]
    self.four.center_y = self.matched_ingredient_coords["parsley"][1]
    self.stuff.append(self.four)
    self.five = arcade.Sprite("images/black.jpg", .1)
    self.five.center_x = self.matched_ingredient_coords["parmesan"][0]
    self.five.center_y = self.matched_ingredient_coords["parmesan"][1]
    self.stuff.append(self.five)
self.FirstSetup = False
