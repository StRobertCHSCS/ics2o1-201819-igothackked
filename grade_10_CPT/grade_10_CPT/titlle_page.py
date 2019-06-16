import arcade

WIDTH = 500
HEIGHT = 500

current_screen = 0

def on_update(delta_time):
 pass

def on_draw():
    global current_screen

    arcade.start_render()

    if current_screen == 0:
        start_screen()

    if current_screen == 1:
        game_play_screen()

    if current_screen == 2:
        how_to_play()


def on_mouse_press(x, y, button, modifiers):

    if (x > 165 and x < 335 and y > 165 and y < 335):
        current_screen = 1
        print("ELCIKEd")

def start_screen():

    arcade.draw_line(165, 0, 165, 500, arcade.color.BLACK, 5)
    arcade.draw_line(335, 0, 335, 500, arcade.color.BLACK, 5)
    arcade.draw_line(0, 165, 500, 165, arcade.color.BLACK, 5)
    arcade.draw_line(0, 335, 500, 335, arcade.color.BLACK, 5)
    arcade.draw_text("TIC", 20, 380, arcade.color.BLACK, 65)
    arcade.draw_text("TAC", 170, 380, arcade.color.BLACK, 65)
    arcade.draw_text("TOE", 340, 380, arcade.color.BLACK, 65)
    arcade.draw_text("START", 170, 190, arcade.color.BLACK, 40)
    arcade.draw_text("How to play", 350, 50, arcade.color.BLACK, 20)
    arcade.draw_text("Created by Justin Cho", 15, 15, arcade.color.BLACK, 20)

def game_play_screen():
    arcade.draw_text("YAY", 100, 100, arcade.color.BLACK, 40)

def how_to_play():
    pass

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_mouse_press = on_mouse_press
    window.start_screen = start_screen

    arcade.run()


if __name__ == '__main__':
    setup()
