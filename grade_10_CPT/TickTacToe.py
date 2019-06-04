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

#winners
o_win_x = 1000
o_win_y = 1000

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
#circle 2
    arcade.draw_circle_outline(circle_2_x, circle_2_y, 35, arcade.color.BLACK, 5)
#cross 2
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_2_x, x_2_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
#circle 3
    arcade.draw_circle_outline(circle_3_x, circle_3_y, 35, arcade.color.BLACK, 5)
#cross 3
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_3_x, x_3_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
#circle 4
    arcade.draw_circle_outline(circle_4_x, circle_4_y, 35, arcade.color.BLACK, 5)
#cross 4
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_4_x, x_4_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
#circle 5
    arcade.draw_circle_outline(circle_5_x, circle_5_y, 35, arcade.color.BLACK, 5)

#winner
    arcade.draw_text("Player O is the winner!!!", o_win_x, o_win_y, arcade.color.BLACK, 50)




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):

    global counter, circle_1_x, circle_1_y, circle_2_x, circle_2_y, circle_3_x, circle_3_y, circle_4_x, circle_4_y, \
        circle_5_x, circle_5_y, x_1_x, x_1_y, x_2_x, x_2_y, x_3_x, x_3_y, x_4_x, x_4_y, o_win

#first circle
    if counter == 0:
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
#first X
    elif counter == 1:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            x_1_x = 150
            x_1_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            x_1_x = 250
            x_1_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            x_1_x = 350
            x_1_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            x_1_x = 150
            x_1_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            x_1_x = 250
            x_1_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            x_1_x = 350
            x_1_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            x_1_x = 150
            x_1_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            x_1_x = 250
            x_1_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            x_1_x = 350
            x_1_y = 150
            counter = counter + 1
#second circle
    elif counter == 2:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            circle_2_x = 150
            circle_2_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            circle_2_x = 250
            circle_2_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            circle_2_x = 350
            circle_2_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            circle_2_x = 150
            circle_2_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            circle_2_x = 250
            circle_2_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            circle_2_x = 350
            circle_2_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            circle_2_x = 150
            circle_2_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            circle_2_x = 250
            circle_2_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            circle_2_x = 350
            circle_2_y = 150
            counter = counter + 1
#second X
    elif counter == 3:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            x_2_x = 150
            x_2_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            x_2_x = 250
            x_2_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            x_2_x = 350
            x_2_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            x_2_x = 150
            x_2_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            x_2_x = 250
            x_2_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            x_2_x = 350
            x_2_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            x_2_x = 150
            x_2_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            x_2_x = 250
            x_2_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            x_2_x = 350
            x_2_y = 150
            counter = counter + 1
#third circle
    elif counter == 4:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            circle_3_x = 150
            circle_3_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            circle_3_x = 250
            circle_3_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            circle_3_x = 350
            circle_3_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            circle_3_x = 150
            circle_3_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            circle_3_x = 250
            circle_3_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            circle_3_x = 350
            circle_3_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            circle_3_x = 150
            circle_3_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            circle_3_x = 250
            circle_3_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            circle_3_x = 350
            circle_3_y = 150
            counter = counter + 1
#third X
    elif counter == 5:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            x_3_x = 150
            x_3_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            x_3_x = 250
            x_3_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            x_3_x = 350
            x_3_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            x_3_x = 150
            x_3_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            x_3_x = 250
            x_3_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            x_3_x = 350
            x_3_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            x_3_x = 150
            x_3_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            x_3_x = 250
            x_3_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            x_3_x = 350
            x_3_y = 150
            counter = counter + 1
#fourth circle
    elif counter == 6:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            circle_4_x = 150
            circle_4_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            circle_4_x = 250
            circle_4_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            circle_4_x = 350
            circle_4_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            circle_4_x = 150
            circle_4_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            circle_4_x = 250
            circle_4_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            circle_4_x = 350
            circle_4_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            circle_4_x = 150
            circle_4_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            circle_4_x = 250
            circle_4_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            circle_4_x = 350
            circle_4_y = 150
            counter = counter + 1
#fourth X
    elif counter == 7:
        if (x > 101 and x < 199 and y > 301 and y < 400):
                x_4_x = 150
                x_4_y = 350
                counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
                x_4_x = 250
                x_4_y = 350
                counter = counter + 1
        elif (x > 301 and x < 399 and y > 301 and y < 400):
                x_4_x = 350
                x_4_y = 350
                counter = counter + 1
        elif (x > 101 and x < 199 and y > 201 and y < 300):
                x_4_x = 150
                x_4_y = 250
                counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
                x_4_x = 250
                x_4_y = 250
                counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
                x_4_x = 350
                x_4_y = 250
                counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
                x_4_x = 150
                x_4_y = 150
                counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
                x_4_x = 250
                x_4_y = 150
                counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
                x_4_x = 350
                x_4_y = 150
                counter = counter + 1
#fifth circle
    elif counter == 8:
        if (x > 101 and x < 199 and y > 301 and y < 400):
            circle_5_x = 150
            circle_5_y = 350
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 301 and y < 400):
            circle_5_x = 250
            circle_5_y = 350
            counter = counter + 1
        elif (x > 301 and x < 399 and y  > 301 and y < 400):
            circle_5_x = 350
            circle_5_y = 350
            counter = counter + 1
        elif (x > 101 and x <199 and y >201 and y < 300):
            circle_5_x = 150
            circle_5_y = 250
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 201 and y < 300):
            circle_5_x = 250
            circle_5_y = 250
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 201 and y < 300):
            circle_5_x = 350
            circle_5_y = 250
            counter = counter + 1
        elif (x > 101 and x < 199 and y > 101 and y < 200):
            circle_5_x = 150
            circle_5_y = 150
            counter = counter + 1
        elif (x > 201 and x < 299 and y > 101 and y < 200):
            circle_5_x = 250
            circle_5_y = 150
            counter = counter + 1
        elif (x > 301 and x < 399 and y > 101 and y < 200):
            circle_5_x = 350
            circle_5_y = 150
            counter = counter + 1

#finding the winner
    if circle_1_x or circle_2_x  or circle_3_x or circle_4_x or circle_5_x == 150 and circle_1_y or circle_2_y or circle_3_y or circle_4_y or circle_5_y == 350 and circle_1_x or circle_2_x  or circle_3_x or circle_4_x or circle_5_x == 250 and circle_1_y or circle_2_y or circle_3_y or circle_4_y or circle_5_y == 350 and circle_1_x or circle_2_x  or circle_3_x or circle_4_x or circle_5_x == 350 and circle_1_y or circle_2_y or circle_3_y or circle_4_y or circle_5_y == 350:
        o_win_x = 100
        o_win_y = 415

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
