import keyboard

import mp.VideoCap


OUTPUT_FRAME = (800, 450)
line_height = 4
line_count = 4


def set_line_count_up():
    global line_count
    if line_count < 30:
        line_count += 1
    print(f'line count set to {line_count}')


def set_line_count_down():
    global line_count
    if line_count > 1:
        line_count -= 1
    print(f'line count set to {line_count}')


def set_line_height_up():
    global line_height
    if line_height < 30:
        line_height += 1
    print(f'line height set to {line_height}')


def set_line_height_down():
    global line_height
    if line_height > 1:
        line_height -= 1
    print(f'line height set to {line_height}')


def init():
    keyboard.add_hotkey('num_7', set_line_count_up)
    keyboard.add_hotkey('num_4', set_line_count_down)
    keyboard.add_hotkey('num_9', set_line_height_up)
    keyboard.add_hotkey('num_6', set_line_height_down)
    keyboard.add_hotkey('num_1', mp.VideoCap.change_mode)
