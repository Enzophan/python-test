from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file("ContextManagers/function_notes.txt") as f:
    f.write("Function context ...")
