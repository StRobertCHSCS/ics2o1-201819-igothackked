import arcade



WIDTH = 500
HEIGHT = 500

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

#the buttons
button_1 = [150, 350, 98, 98]
button_2 = [250, 350, 98, 98]
button_3 = [350, 350, 98, 98]
button_4 = [150, 250, 98, 98]
button_5 = [250, 250, 98, 98]
button_6 = [350, 250, 98, 98]
button_7 = [150, 150, 98, 98]
button_8 = [250, 150, 98, 98]
button_9 = [350, 150, 98, 98]



def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    #lines vertical
    arcade.draw_line(200, 100, 200, 400, arcade.color.BLACK, 4)
    arcade.draw_line(300, 100, 300, 400, arcade.color.BLACK, 4)
    #horizontal lines
    arcade.draw_line(100, 200, 400, 200, arcade.color.BLACK, 4)
    arcade.draw_line(100, 300, 400, 300, arcade.color.BLACK, 4)

    #box 1
    arcade.draw_rectangle_filled(button_1[0],
                                 button_1[1],
                                 button_1[2],
                                 button_1[3],
                                 arcade.color.WHITE)

    arcade.draw_circle_filled(circle_1_x, circle_1_y, 50, arcade.color.BLACK)
    #add the x

    #box 2
    arcade.draw_rectangle_filled(button_2[0],
                                 button_2[1],
                                 button_2[2],
                                 button_2[3],
                                 arcade.color.GREEN)

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):

    global circle_1_x, circle_1_y, circle_2_x, circle_2_y

    # first circle horizontal 1
    if (x > 101 and x < 199 and y > 301 and y < 400):
        circle_1_x = 150
        circle_1_y = 350
        print("clicked")
    elif (x > 201 and x < 299 and y > 301 and y < 400):
        circle_1_x = 250
        circle_1_y = 350
    elif (x > 301 and x < 399 and y  > 301 and y < 400):
        circle_1_x = 350
        circle_1_y = 350
    # first circle horizontal 2
    elif (x > 101 and x <199 and y >201 and y < 300):
        circle_1_x = 150
        circle_1_y = 250
    elif (x > 201 and x < 299 and y > 201 and y < 300):
        circle_1_x = 250
        circle_1_y = 250
    elif (x > 301 and x < 399 and y > 201 and y < 300):
        circle_1_x = 350
        circle_1_y = 250
    # first circle horizontal 3
    elif (x > 101 and x < 199 and y > 101 and y < 200):
        circle_1_x = 150
        circle_1_y = 150
    elif (x > 201 and x < 299 and y > 101 and y < 200):
        circle_1_x = 250
        circle_1_y = 150
    elif (x > 301 and x < 399 and y > 101 and y < 200):
        circle_1_x = 350
        circle_1_y = 150




def setup():
    arcade.open_window(WIDTH, HEIGHT, "Justin's Tick Tack Toe")
    arcade.set_background_color(arcade.color.RED)
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
