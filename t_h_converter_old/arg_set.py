line_resized = False
line_height = 8
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