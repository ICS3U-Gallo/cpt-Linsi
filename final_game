#
import arcade


WIDTH = 600
HEIGHT = 500
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
    arcade.set_background_color(arcade.color.GRAY_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    global player_x, player_y, up_pressed, down_pressed, left_pressed, right_pressed, ball1_x, ball2_x, ball3_x, ball4_x
    if up_pressed:
        player_y += 3
    elif down_pressed:
        player_y -= 3
    if left_pressed:
        player_x -= 3
    elif right_pressed:
        player_x += 3



def on_draw():
    arcade.start_render()
    # Draw in here...
    global player_x, player_y, ball1_x, ball1_y, ball2_x, ball2_y, ball3_x, ball3_y, ball4_x, ball4_y

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
    global up_pressed, down_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_pressed = True
    elif key == arcade.key.DOWN:
        down_pressed = True
    elif key == arcade.key.LEFT:
        left_pressed = True
    elif key == arcade.key.RIGHT:
        right_pressed = True


def on_key_release(key, modifiers):
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
