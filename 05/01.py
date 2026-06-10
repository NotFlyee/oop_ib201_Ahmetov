old_print = print
def print(*args):
    old_print(*[str(arg).upper() for arg in args])
