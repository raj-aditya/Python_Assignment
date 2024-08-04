
class Shape():
    def area(self):
        return 0

class Sqaure(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

sq = Sqaure(5)

print(sq.area())
