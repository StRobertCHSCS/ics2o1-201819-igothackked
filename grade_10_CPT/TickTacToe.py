import arcade



WIDTH = 500
HEIGHT = 500

counter = 0

#circles
circle_1_x = 1000
circle_1_y = 1000
circle_2_x = 1000
circle_2_y = 1000
circle_3_x = 1000
circle_3_y = 1000
circle_4_x = 1000
circle_4_y = 1000
circle_5_x = 1000
circle_5_y = 1000

#the lines to make X's

x_1_x = 1000
x_1_y = 1000
x_2_x = 1000
x_2_y = 1000
x_3_x = 1000
x_3_y = 1000
x_4_x = 1000
x_4_y = 1000

#the buttons
button_1 = [150, 350, 98, 98]

def on_update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    #lines vertical
    arcade.draw_line(200, 100, 200, 400, arcade.color.BLACK, 4)
    arcade.draw_line(300, 100, 300, 400, arcade.color.BLACK, 4)
    #horizontal lines
    arcade.draw_line(100, 200, 400, 200, arcade.color.BLACK, 4)
    arcade.draw_line(100, 300, 400, 300, arcade.color.BLACK, 4)

#circle_1
    arcade.draw_circle_outline(circle_1_x, circle_1_y, 35, arcade.color.BLACK, 5)
#cross_1
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_1_x, x_1_y, scale * texture.width,
                                  scale * texture.height, texture, 0)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):

    global counter, circle_1_x, circle_1_y, circle_2_x, circle_2_y, circle_3_x, circle_3_y, circle_4_x, circle_4_y, \
        circle_5_x, circle_5_y, x_1_x, x_1_y, x_2_x, x_2_y, x_3_x, x_3_y, x_4_x, x_4_y


    if counter == 0:
        # first circle horizontal 1
        if (x > 101 and x < 199 and y > 301 and y < 400):
            circle_1_x = 150
            circle_1_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            circle_1_x = 250
            circle_1_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            circle_1_x = 350
            circle_1_y = 350
            counter = counter + 1
        # first circle horizontal 2
        elif (x > 101 and x <199 and y >201 and y < 300):
            circle_1_x = 150
            circle_1_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            circle_1_x = 250
            circle_1_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            circle_1_x = 350
            circle_1_y = 250
            counter = counter + 1
        # first circle horizontal 3
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            circle_1_x = 150
            circle_1_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            circle_1_x = 250
            circle_1_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            circle_1_x = 350
            circle_1_y = 150
            counter = counter + 1
    if counter == 1:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            x_1_x = 150
            x_1_y = 350
            counter = counter + 1
            print("Clicked!!!")
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            x_1_x = 250
            x_1_y = 350
            counter = counter + 1




def setup():
    arcade.open_window(WIDTH, HEIGHT, "Justin's Tick Tack Toe")
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
