# file = open("newfile.txt", 'x')

with open("newfile.txt", 'a') as f:
    print("File is opened" if not f.closed else "File is closed")
    print("It's mode: ", f.mode)
    print("It's name: ", f.name)
    for _ in range(100):
        f.write("Django" + '\n')

with open("newfile.txt", 'r') as f:
    print(f.tell())
    print(f.seek(10))
    print(f.read(5))
    print(f.tell())


class Class:
    @classmethod
    def fn(cls):
        print("awe")


Class.fn()
