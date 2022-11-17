import arcade

from ShipGoldWindow import ShipGoldWindow


def main():
    seas_window = ShipGoldWindow()
    arcade.set_background_color(arcade.color.SEA_BLUE)
    seas_window.setup()
    arcade.run()


main()