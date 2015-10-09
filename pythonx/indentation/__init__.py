import _vim


def go_down(count):
    return _go(1, count)


def go_up(count):
    return _go(-1, count)


def _go(direction, count):
    line_level = get_next_line_level(direction, count)
    if line_level is None:
        return

    line, level = line_level
    _vim.goto(line, level)


def get_next_line_level(direction, count):
    current_line = _vim.line_number()
    current_level = get_level(current_line)

    next_line = current_line
    levels = 0
    while True:
        next_line += direction

        if direction == 1 and next_line >= len(_vim.buffer()):
            return None

        if direction == -1 and next_line <= 0:
            return None

        next_level = get_level(next_line)
        if next_level != current_level:
            levels += 1

        if levels > count:
            return (next_line, next_level)


def get_level(line_number):
    line = _vim.buffer()[line_number]

    column = 0
    for symbol in line:
        if symbol == "\t" or symbol == " ":
            column += 1
        else:
            break

    return column
