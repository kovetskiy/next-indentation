import _vim

def go_down():
    return _go(1)

def go_up():
    return _go(-1)

def _go(direction):
    line_level = get_next_line_level(direction)
    if line_level == None:
        return

    line, level = line_level
    _vim.goto(line, level)


def get_next_line_level(direction):
    current_line = _vim.line_number()
    current_level = get_level(current_line)

    next_line = current_line
    while True:
        next_line += direction

        if direction == 1 and next_line > len(_vim.buffer()):
            return None

        if direction == -1 and next_line <= 0:
            return None

        next_level = get_level(next_line)
        if next_level != current_level:
            return (next_line, next_level)


def get_level(line_number):
    line = _vim.buffer()[line_number]
    column = 0
    for symbol in line:
        if symbol == "\t":
            column += 1

    return column
