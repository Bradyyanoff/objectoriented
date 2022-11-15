import arcade

from comp151window import Comp151Window

def main():
    our_window = Comp151Window(1000, 750)
    our_window.setup()
    arcade.run()


main()
