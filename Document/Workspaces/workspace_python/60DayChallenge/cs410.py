class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = Point(.5,.7)
p4 = Point(.8,.9)

p5 = Point('str1','str2')
p6 = Point('str3','str4')


print(p1+p2)
print(p3+p4)
print(p5+p6)