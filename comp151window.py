import arcade

class Comp151Window(arcade.Window):
    def __int__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.player = None
        self.targets = arcade.SpriteList()
        self.score = 0

    def setup(self):
        self.player = arcade.Sprite("f1-ship1-6.png")
        rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
        self.targets.append(rock)
    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()

        arcade.finish_render()
