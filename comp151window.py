import arcade
import random
class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.targets = arcade.SpriteList()
        self.player = None
        self.score = 0
        self.sound = None
        self.player_dx = 0
    def setup(self):
        self.sound = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite("f1-ship1-6.png")
        for number in range(5):
            rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.targets.append(rock)
            rock.center_y = random.randint(16, 724)
            rock.center_x = random.randint(16, 934)
        self.player.center_x = 500
        self.player.center_y = 375
    def on_update(self, delta_time):
        self.player.center_x += self.player_dx
        if self.player.center_x > 1000:
            self.player.center_x = 0
            arcade.play_sound(self.sound)
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player_dx += 3
        elif symbol == arcade.key.A:
            self.player_dx -= 3

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player_dx = 0
