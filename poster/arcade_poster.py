import arcade


WIDTH = 480
HEIGHT = 640


def on_update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(240, 0, 350, arcade.color.COCOA_BROWN)
    arcade.draw_circle_filled(240, 440, 50, arcade.color.PEACH_YELLOW)
    arcade.draw_rectangle_filled(240, 370, 150, 100, arcade.color.ASH_GREY )
    arcade.draw_rectangle_filled(240, 320, 40, 75, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text("DONT BE MEAN",110, 220, arcade.color.BLACK, 30)
    arcade.draw_text("BEHIND THE SCREEN", 75, 180, arcade.color.BLACK, 30)
    arcade.draw_text("YOU have the", 80, 110, arcade.color.BLACK, 30)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

    arcade.run()

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Justin's Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()

if __name__ == '__main__':
    setup()
