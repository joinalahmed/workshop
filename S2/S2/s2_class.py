class Myclass:
    def print_class(self):
        print("Hello")


X = Myclass()
X.print_class()

class Myclass_2(object):
    def __init__(self, a):
        self.a = a
        self.b = " World"
        self.c = ""
    def print_class(self):
        self.c = self.a + self.b
        print(self.c)

x_2 = Myclass_2("Hello")
x_2.print_class()






