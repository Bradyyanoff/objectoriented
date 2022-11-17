import arcade
import random
class ShipGoldWindow(arcade.Window):
    def __init__(self):
        super().__init__(1200, 700, "Collect the Gold")
        self.ship = None
        self.goals = arcade.SpriteList()
        self.score = 0
        self.sound = None

    def setup(self):
        self.ship = arcade.Sprite("pirate-galleon.png")
        self.sound = arcade.load_sound(":resources:sounds/coin2.wav")
        for number in range(7):
            gold = arcade.Sprite("gold-coins-large.png")
            gold.center_x = random.randint(30, 1170)
            gold.center_y = random.randint(30, 670)
            self.goals.append(gold)

    def on_update(self, delta_time):
        gold_piles_collected = arcade.check_for_collision_with_list(self.ship, self.goals)
        if gold_piles_collected:
            arcade.play_sound(self.sound)
            self.score += len(gold_piles_collected)
            for gold in gold_piles_collected:
                self.goals.remove(gold)
    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        self.goals.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y
