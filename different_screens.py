import arcade

WIDTH = 600
HEIGHT = 500

current_screen = "menu"

a = 40
b = 35

player_x = WIDTH/2 - 5.5 * a
player_y = HEIGHT/2 - 1.5 * b

ball1_x = WIDTH/2 - 3 * a
ball1_y = HEIGHT/2 + 1.5 * b
ball2_x = WIDTH/2 - 3 * a
ball2_y = HEIGHT/2 - 0.5 * b
ball3_x = WIDTH/2 + 3 * a
ball3_y = HEIGHT/2 + 0.5 * b
ball4_x = WIDTH/2 + 3 * a
ball4_y = HEIGHT/2 - 1.5 * b

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    if current_screen == "play":
        moving()


def moving():
    global player_x, player_y, up_pressed, down_pressed, left_pressed, right_pressed, ball1_x, ball2_x, ball3_x, ball4_x
#   if (WIDTH/2 - 2.5 * a + 5 < player_x < WIDTH/2 + 2.5 * a - 5 and HEIGHT/2 - 2 * b + 5 < player_y < HEIGHT/2 + 2 * b - 5) or (WIDTH/2 + 2.5 * a + 5 < player_x < WIDTH/2 + 3.5 * a - 5 and HEIGHT/2 - 2 * b + 5 < player_y < HEIGHT/2 + 3 * b) - 5 or (WIDTH/2 - 3.5 * a + 5 < player_x - 5 < WIDTH/2 - 2.5 * a - 5 and HEIGHT/2 - 3 * b + 5 < player_y < HEIGHT/2 + 2 * b - 5) or (WIDTH/2 - 4.5 * a + 5 < player_x < WIDTH/2 - 3.5 * a - 5 and HEIGHT/2 - 3 * b + 5 < player_y < HEIGHT/2 - 2 * b - 5) or (WIDTH/2 + 3.5 * a + 5 < player_x < WIDTH/2 + 4.5 * a - 5 and HEIGHT/2 + 2 * b + 5 < player_y < HEIGHT/2 + 3 * b - 5) or (WIDTH/2 - 6.5 * a + 5 < player_x < WIDTH/2 - 4.5 * a - 5 and HEIGHT/2 - 3 * b + 5 < player_y < HEIGHT/2 - 5) or (WIDTH/2 + 4.5 * a + 5 < player_x < WIDTH/2 + 6.5 * a - 5 and HEIGHT/2 + 5 < player_y < HEIGHT/2 + 3 * b - 5):
    if up_pressed:
        player_y += 2
    elif down_pressed:
        player_y -= 2
    if left_pressed:
        player_x -= 2
    elif right_pressed:
        player_x += 2


def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2-90,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_instructions():
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_play():
    arcade.set_background_color(arcade.color.GRAY_BLUE)
    arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, 7 * a, 4 * b, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled(WIDTH/2 - 3.5 * a, HEIGHT/2 - 2.5 * b, 2 * a, b, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled(WIDTH/2 + 3.5 * a, HEIGHT/2 + 2.5 * b, 2 * a, b, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled(WIDTH/2 - 5.5 * a, HEIGHT/2 - 1.5 * b, 2 * a, 3 * b, arcade.color.GUPPIE_GREEN)
    arcade.draw_rectangle_filled(WIDTH/2 + 5.5 * a, HEIGHT/2 + 1.5 * b, 2 * a, 3 * b, arcade.color.GUPPIE_GREEN)
    arcade.draw_rectangle_filled(player_x, player_y, 15, 15, arcade.color.RED)

    arcade.draw_circle_filled(ball1_x, ball1_y, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(ball2_x, ball2_y, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(ball3_x, ball3_y, 10, arcade.color.BLUE)
    arcade.draw_circle_filled(ball4_x, ball4_y, 10, arcade.color.BLUE)


def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"
        elif key == arcade.key.ESCAPE:
            exit()
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
        key_press(key, modifiers)


def key_press(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True
    if key == arcade.key.LEFT:
        left_pressed = True
    if key == arcade.key.RIGHT:
        right_pressed = True

    if 45 < player_x < 49:
        left_pressed = False
    if 165 < player_x < 169 and player_y >= HEIGHT/2 - 2 * b - 7.5:
        left_pressed = False
    if 405 < player_x < 409 and player_y >= HEIGHT/2 + 2 * b - 7.5:
        left_pressed = False
    if 485 < player_x < 489 and player_y <= HEIGHT/2 + 2 * b + 7.5:
        left_pressed = False


def on_key_release(key, modifiers):
    if current_screen == "play":
        key_release(key, modifiers)


def key_release(key, modifiers):
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_pressed = False
    elif key == arcade.key.DOWN:
        down_pressed = False
    elif key == arcade.key.LEFT:
        left_pressed = False
    elif key == arcade.key.RIGHT:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
