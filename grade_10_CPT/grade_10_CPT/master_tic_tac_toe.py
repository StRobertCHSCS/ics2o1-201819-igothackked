import arcade

# dimensions of my code
WIDTH = 500
HEIGHT = 500

# counter
counter = 0

# x and y coordinates of the starting circles
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

# x and y coordinated of the lines to make X's

x_1_x = 1000
x_1_y = 1000
x_2_x = 1000
x_2_y = 1000
x_3_x = 1000
x_3_y = 1000
x_4_x = 1000
x_4_y = 1000

# screen changer counter
current_screen = 0

def on_update(delta_time):
 pass


def on_draw():
    # allow the variable current_screen to be used throughout the whole code
    global current_screen

    arcade.start_render()
    # screen changers
    if current_screen == 0:
        start_screen()

    if current_screen == 1:
        game_play_screen()

    if current_screen == 2:
        how_to_play()


def on_mouse_press(x, y, button, modifiers):
    # allows my variables to be used through out the whole code
    global counter, circle_1_x, circle_1_y, circle_2_x, circle_2_y, circle_3_x, circle_3_y, circle_4_x, circle_4_y, \
        circle_5_x, circle_5_y, x_1_x, x_1_y, x_2_x, x_2_y, x_3_x, x_3_y, x_4_x, x_4_y, current_screen

    if current_screen == 0:
        # button for start
        if(x > 165 and x < 335 and y > 165 and y < 335):
            current_screen = 1
            # resets the circles, X's and the counter to the start mode
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
            x_1_x = 1000
            x_1_y = 1000
            x_2_x = 1000
            x_2_y = 1000
            x_3_x = 1000
            x_3_y = 1000
            x_4_x = 1000
            x_4_y = 1000
            counter = 0

    if current_screen == 0:
        # button for the "how to play" screen
        if (x > 335 and x < 500 and y > 0 and y < 335):
            current_screen = 2

    # code for playing the game
    if current_screen == 1:
        # first circle
        if counter == 0:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                circle_1_x = 150
                circle_1_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                circle_1_x = 250
                circle_1_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                circle_1_x = 350
                circle_1_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # first X
        elif counter == 1:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                x_1_x = 150
                x_1_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                x_1_x = 250
                x_1_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                x_1_x = 350
                x_1_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # second circle
        elif counter == 2:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                circle_2_x = 150
                circle_2_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                circle_2_x = 250
                circle_2_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                circle_2_x = 350
                circle_2_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # second X
        elif counter == 3:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                x_2_x = 150
                x_2_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                x_2_x = 250
                x_2_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                x_2_x = 350
                x_2_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # third circle
        elif counter == 4:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                circle_3_x = 150
                circle_3_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                circle_3_x = 250
                circle_3_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                circle_3_x = 350
                circle_3_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # third X
        elif counter == 5:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                x_3_x = 150
                x_3_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                x_3_x = 250
                x_3_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                x_3_x = 350
                x_3_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # fourth circle
        elif counter == 6:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                circle_4_x = 150
                circle_4_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                circle_4_x = 250
                circle_4_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                circle_4_x = 350
                circle_4_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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
        # fourth X
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
        # fifth circle
        elif counter == 8:
            if (x > 101 and x < 199 and y > 301 and y < 400):
                circle_5_x = 150
                circle_5_y = 350
                counter = counter + 1
            elif (x > 201 and x < 299 and y > 301 and y < 400):
                circle_5_x = 250
                circle_5_y = 350
                counter = counter + 1
            elif (x > 301 and x < 399 and y > 301 and y < 400):
                circle_5_x = 350
                circle_5_y = 350
                counter = counter + 1
            elif (x > 101 and x < 199 and y > 201 and y < 300):
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

    if current_screen == 1:
        # back button for when you want to go back home from the game
        if(x > 30 and x < 130 and y < 475 and y > 425):
            # resets the circles, X's and the counter to the start mode
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
            x_1_x = 1000
            x_1_y = 1000
            x_2_x = 1000
            x_2_y = 1000
            x_3_x = 1000
            x_3_y = 1000
            x_4_x = 1000
            x_4_y = 1000
            counter = 0
            current_screen = 0

    if current_screen == 1:
        # new game button if you want to play again
        if (x > 305 and x < 495 and y < 475 and y > 425):
            # resets the circles, X's and the counter to the start mode
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
            x_1_x = 1000
            x_1_y = 1000
            x_2_x = 1000
            x_2_y = 1000
            x_3_x = 1000
            x_3_y = 1000
            x_4_x = 1000
            x_4_y = 1000
            counter = 0

    if current_screen == 2:
        # back to home screen button from the how to play
        if (x > 50 and x < 150 and y > 25 and y < 75):
            current_screen = 0
        # play game button from the how to play
        elif (x > 200 and x < 300 and y > 20 and y < 80):
            # resets the circles, X's and the counter to the start mode
            current_screen = 1
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
            x_1_x = 1000
            x_1_y = 1000
            x_2_x = 1000
            x_2_y = 1000
            x_3_x = 1000
            x_3_y = 1000
            x_4_x = 1000
            x_4_y = 1000
            counter = 0


def start_screen():

    # home screen layout
    arcade.draw_line(165, 0, 165, 500, arcade.color.BLACK, 5)
    arcade.draw_line(335, 0, 335, 500, arcade.color.BLACK, 5)
    arcade.draw_line(0, 165, 500, 165, arcade.color.BLACK, 5)
    arcade.draw_line(0, 335, 500, 335, arcade.color.BLACK, 5)
    # home screen texts
    arcade.draw_text("TIC", 20, 380, arcade.color.BLACK, 65)
    arcade.draw_text("TAC", 170, 380, arcade.color.BLACK, 65)
    arcade.draw_text("TOE", 340, 380, arcade.color.BLACK, 65)
    arcade.draw_text("START", 175, 225, arcade.color.BLACK, 40)
    arcade.draw_text("How to play", 355, 70, arcade.color.BLACK, 20)
    arcade.draw_text("Created by;", 15, 50, arcade.color.BLACK, 20)
    arcade.draw_text("Justin Cho", 15, 20, arcade.color.BLACK, 20)

def game_play_screen():

    # lines vertical
    arcade.draw_line(200, 100, 200, 400, arcade.color.BLACK, 4)
    arcade.draw_line(300, 100, 300, 400, arcade.color.BLACK, 4)
    # horizontal lines
    arcade.draw_line(100, 200, 400, 200, arcade.color.BLACK, 4)
    arcade.draw_line(100, 300, 400, 300, arcade.color.BLACK, 4)

    # drawing in the O's and X's when the buttons are pressed
    # circle_1
    arcade.draw_circle_outline(circle_1_x, circle_1_y, 35, arcade.color.BLACK, 5)
    # cross_1
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_1_x, x_1_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
    # circle 2
    arcade.draw_circle_outline(circle_2_x, circle_2_y, 35, arcade.color.BLACK, 5)
    # cross 2
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_2_x, x_2_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
    # circle 3
    arcade.draw_circle_outline(circle_3_x, circle_3_y, 35, arcade.color.BLACK, 5)
    # cross 3
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_3_x, x_3_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
    # circle 4
    arcade.draw_circle_outline(circle_4_x, circle_4_y, 35, arcade.color.BLACK, 5)
    # cross 4
    texture = arcade.load_texture("x marks the spot .png")
    scale = .35
    arcade.draw_texture_rectangle(x_4_x, x_4_y, scale * texture.width,
                                  scale * texture.height, texture, 0)
    # circle 5
    arcade.draw_circle_outline(circle_5_x, circle_5_y, 35, arcade.color.BLACK, 5)

    # go back button
    arcade.draw_rectangle_filled(80, 450, 100, 50, arcade.color.YELLOW_ROSE)
    arcade.draw_text("Back", 40, 435, arcade.color.BLACK, 30)
    # reset game button
    arcade.draw_rectangle_filled(400, 450, 190, 50, arcade.color.YELLOW_ROSE)
    arcade.draw_text("New Game", 310, 435, arcade.color.BLUE, 30)

def how_to_play():

    # instructions on how to play tic tac toe
    arcade.draw_text("How to play", 150, 430, arcade.color.BLACK, 30)
    arcade.draw_text("- Tic Tac Toe is a game played between two players", 15, 380, arcade.color.BLACK, 15)
    arcade.draw_text("- Both players will have their own symbol", 15, 355, arcade.color.BLACK, 15)
    arcade.draw_text("- As Player O will start, they will place their symbol on", 15, 330, arcade.color.BLACK, 15)
    arcade.draw_text("any of the 9 squares", 15, 310, arcade.color.BLACK, 15)
    arcade.draw_text("- After player O has gone, player X will place there", 15, 285, arcade.color.BLACK, 15)
    arcade.draw_text(" symbol down on an empty square", 15, 265, arcade.color.BLACK, 15)
    arcade.draw_text("- Both players will make their turns alternately", 15, 240, arcade.color.BLACK, 15)
    arcade.draw_text("on empty squares", 15, 220, arcade.color.BLACK, 15)
    arcade.draw_text("- If any player gets their symbols in a horizontal,", 15, 195, arcade.color.BLACK, 15)
    arcade.draw_text("vertical, or diagonal row they win the game", 15, 175, arcade.color.BLACK, 15)
    arcade.draw_text("-if there is no winner the game is called a 'cats scratch'", 15, 150, arcade.color.BLACK, 15)

    #back button
    arcade.draw_rectangle_filled(100, 50, 100, 50, arcade.color.BLUE_GREEN)
    arcade.draw_text("BACK", 60, 35, arcade.color.BLACK, 25)
    #play button
    arcade.draw_rectangle_filled(250, 50, 100, 50, arcade.color.BLUE_GREEN)
    arcade.draw_text("PLAY", 210, 35, arcade.color.BLACK, 25)

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