import arcade
import random
class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.targets = arcade.SpriteList()
        self.player = None
        self.score = 0

    def setup(self):
        self.player = arcade.Sprite("f1-ship1-6.png")
        for number in range(5):
            rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.targets.append(rock)
            rock.center_y = random.randint(16, 484)
            rock.center_x = random.randint(16, 484)
        self.player.center_x = 250
        self.player.center_y = 250
    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()
