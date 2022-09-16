# with open('ContextManagers/notes.txt', 'w') as file:
#     file.write('Some todo ...')


# file = open('notes.txt', 'w')
# try:
#     file.write('some todo ...')
# finally:
#     file.close()


# from threading import Lock
# lock = Lock()
# lock.acquire()
# #...
# lock.release()

# with lock:
#     #...


class ManagedFile:
    def __init__(self, filename):
        print("Init")
        self.filename = filename

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        print("Exit")
        return True

with ManagedFile("ContextManagers/class_notes.txt") as file:
    print("do some stuff ...")
    file.write("Class writing ...")
    file.somemethod()

print("Continuing")
