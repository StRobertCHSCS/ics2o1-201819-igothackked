import arcade


WIDTH = 480
HEIGHT = 640
x = 290
b = 1

def on_update(delta_time):
    global x,b

    x = x + b

    if x == 280:
        b = b * -1
    if x == 310:
        b = b * -1



my_button = [320, 100, 75, 50]  # x, y, width, height

def on_draw():
    arcade.start_render()
    # Draw in here...
    #Add image
    texture = arcade.load_texture("wig2.png")
    scale = 0.5
    arcade.draw_texture_rectangle(240, 420, scale * texture.width,
                                  scale * texture.height, texture, 0)
    #Shapes
    arcade.draw_circle_filled(240, 440, 50, arcade.color.PEACH_YELLOW)
    arcade.draw_circle_filled(240, 0, 350, arcade.color.COCOA_BROWN)
    arcade.draw_rectangle_filled(240, 370, 150, 100, arcade.color.ASH_GREY )
    arcade.draw_rectangle_filled(240, 320, 40, 75, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text("DON'T BE MEAN",110, 220, arcade.color.BLACK, 30)
    arcade.draw_text("BEHIND THE SCREEN", 75, 180, arcade.color.BLACK, 30)
    arcade.draw_text("YOU have the", 80, 110, arcade.color.BLACK, 30)
    #Eyes
    arcade.draw_line(200, 460, 220, 450, arcade.color.BLACK_LEATHER_JACKET, 4)
    arcade.draw_line(280, 460, 260, 450, arcade.color.BLACK_LEATHER_JACKET, 4)
    #Button
    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.WARM_BLACK)
    arcade.draw_text("Ctrl", 325, 110, arcade.color.WHITE_SMOKE, 20)
    #Add image
    texture = arcade.load_texture("computer_mouse.png")
    scale = .1
    arcade.draw_texture_rectangle(x, 300, scale * texture.width,
                                  scale * texture.height, texture, 130)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass
    # unpack the button list into readable? variables.
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        print("So Be Nice ;)")

    arcade.run()

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Justin's Arcade Game")
    arcade.set_background_color(arcade.color.DARK_BROWN)
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
