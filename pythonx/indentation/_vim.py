import vim

def goto(line, level):
    vim.current.window.cursor = (line+1, level)


def cursor():
    cursor = vim.current.window.cursor
    return (cursor[0] - 1, cursor[1] + 1)


def buffer():
    return vim.current.window.buffer


def line_number():
    number, _ = cursor()
    return number
