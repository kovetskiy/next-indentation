import _vim

def go_next(line_direction, level_direction, count):
    line_level = get_next_line_level(line_direction, level_direction, count)
    if line_level is None:
        return

    line, level = line_level
    _vim.goto(line, level)


def go_same(line_direction, count):
    line_level = get_same_line_level(line_direction, count)
    if line_level is None:
        return

    line, level = line_level
    _vim.goto(line, level)


def get_next_line_level(line_direction, level_direction, count):
    current_line = _vim.line_number()
    current_level = get_level(current_line)

    next_line = current_line
    next_level = None

    levels = 0
    while True:
        if line_direction == "down":
            next_line += 1
            if next_line >= len(_vim.buffer()):
                if levels > 0:
                    return (next_line, next_level)
                return None

        if line_direction == "up":
            next_line -= 1
            if next_line <= 0:
                if levels > 0:
                    return (next_line, next_level)
                return None

        next_level = get_level(next_line)
        if level_direction == "deeper" and next_level > current_level:
            levels += 1

        if level_direction == "shallower" and next_level < current_level:
            levels += 1

        if levels >= count:
            return (next_line, next_level)

def get_same_line_level(line_direction, count):
    if count == 0:
        count = 1

    current_line = _vim.line_number()
    current_level = get_level(current_line)

    next_line = current_line
    jumps = 0
    while True:
        possible_next_line = next_line
        if line_direction == "down":
            possible_next_line += 1

        if line_direction == "up":
            possible_next_line -= 1

        if possible_next_line >= len(_vim.buffer()) or possible_next_line <= 0:
            if possible_next_line == current_line:
                return None

            return (next_line, current_level)

        next_line = possible_next_line

        if _vim.buffer()[next_line] == "":
            continue

        next_level = get_level(next_line)

        if next_level == current_level:
            jumps = jumps + 1
            if jumps == count:
                return (next_line, current_level)


def get_level(line_number):
    line = _vim.buffer()[line_number]

    column = 0
    for symbol in line:
        if symbol == "\t" or symbol == " ":
            column += 1
        else:
            break

    return column
