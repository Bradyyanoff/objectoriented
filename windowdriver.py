import arcade

from comp151window import Comp151Window

def main():
    our_window = Comp151Window(500, 500)
    our_window.setup()
    arcade.run()


main()
