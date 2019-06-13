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

balls_x = [ball1_x, ball2_x, ball3_x, ball4_x]
balls_y = [ball1_y, ball2_y, ball3_y, ball4_y]

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
    global player_x, player_y, up_pressed, down_pressed, left_pressed
    global right_pressed, ball1_x, ball2_x, ball3_x, ball4_x, balls_x
    if up_pressed:
        player_y += 2
    elif down_pressed:
        player_y -= 2
    if left_pressed:
        player_x -= 2
    elif right_pressed:
        player_x += 2

    speed = 4
    ball1_x += speed
    ball2_x += speed
    ball3_x -= speed
    ball4_x -= speed
    if ball1_x > WIDTH/2 + 3 * a:
            ball1_x = WIDTH/2 - 3 * a
    if ball2_x > WIDTH/2 + 3 * a:
            ball2_x = WIDTH/2 - 3 * a
    if ball3_x < WIDTH/2 - 3 * a:
        ball3_x = WIDTH/2 + 3 * a
    if ball4_x < WIDTH/2 - 3 * a:
            ball4_x = WIDTH/2 + 3 * a

    i = 0
    while i < 4:
        if player_x > balls_x[i] - 12.5 and player_x < balls_x[i] + 12.5 and player_y > balls_y[i] - 12.5 and player_y < balls_y[i] + 12.5:
            current_screen = "game_over"
            break
        i += 1


def on_draw():
    global current_screen, balls_x, balls_y
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()
    elif current_screen == "game_over":
        draw_game_over()
    elif current_screen =="game_win":
        draw_game_win()


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="left")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="left")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2-90,
                     arcade.color.BLACK, font_size=20, anchor_x="left")


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


def draw_game_over():
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_text("Game Over", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=48, anchor_x="center")
    arcade.draw_text("Press R to Restart", WIDTH/2, HEIGHT/2 - 60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_game_win():
    arcade.set_background_color(arcade.color.PURPLE_MOUNTAIN_MAJESTY)
    arcade.draw_text("Congratulations!", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=48, anchor_x="center")
    arcade.draw_text("Press R to Resatrt", WIDTH/2, HEIGHT/2 - 60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def on_key_press(key, modifiers):
    global current_screen, player_x, player_y, balls_x, balls_y, ball4_y
    global ball1_x, ball1_y, ball2_x, ball2_y, ball3_x, ball3_y, ball4_x

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
        if player_x > WIDTH/2 + 4.5 * a:
            current_screen = "game_win"

        i = 0
        while i < 4:
            if balls_x[i] - 12.5 < player_x < balls_x[i] + 12.5 and balls_y[i] - 12.5 < player_y < balls_y[i] + 12.5:
                current_screen = "game_over"
                break
            i += 1

    elif current_screen == "game_over" or current_screen == "game_win":
        if key == arcade.key.R:
            current_screen = "play"


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
    elif 165 < player_x < 169 and player_y >= HEIGHT/2 - 2 * b - 7.5:
        left_pressed = False
    elif 405 < player_x < 409 and player_y >= HEIGHT/2 + 2 * b - 7.5:
        left_pressed = False
    elif 485 < player_x < 489 and player_y <= HEIGHT/2 + 2 * b + 7.5:
        left_pressed = False

    if 111 < player_x < 115 and player_y >= HEIGHT/2 - 2 * b - 7.5:
        right_pressed = False
    elif 191 < player_x < 195 and player_y <= HEIGHT/2 - 2 * b + 7.5:
        right_pressed = False
    elif 431 < player_x < 435 and player_y <= HEIGHT/2 + 2 * b + 7.5:
        right_pressed = False
    elif 551 < player_x < 555:
        right_pressed = False

    if 40 < player_x < 120 and 241 < player_y < 245:
        up_pressed = False
    elif 120 < player_x < 160 and 171 < player_y < 175:
        up_pressed = False
    elif 160 < player_x < 400 and 311 < player_y < 315:
        up_pressed = False
    elif 400 < player_x < 560 and 345 < player_y < 349:
        up_pressed = False

    if 40 < player_x < 200 and 151 < player_y < 155:
        down_pressed = False
    elif 200 < player_x < 440 and 185 < player_y < 189:
        down_pressed = False
    elif 440 < player_x < 480 and 325 < player_y < 329:
        down_pressed = False
    elif 480 < player_x < 560 and 255 < player_y < 259:
        down_pressed = False


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
    if current_screen == "game_over":
        if x > button1[0] - 100 and x < button1[0] + 100 and y < button1[1] + 50 and y > button1[1] - 50:
            current_screen = "play"
            player_x = WIDTH/2 - 5.5 * a
            player_y = HEIGHT/2 - 1.5 * b


if __name__ == '__main__':
    setup()

