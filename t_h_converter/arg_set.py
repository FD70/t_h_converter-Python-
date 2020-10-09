line_resized = False
line_height = 8


def set_line_height_up():
    global line_height
    if line_height < 30:
        line_height += 1
    print(f'line height set to {line_height}')


def set_line_height_down():
    global line_height
    if line_height > 8:
        line_height -= 1
    print(f'line height set to {line_height}')
