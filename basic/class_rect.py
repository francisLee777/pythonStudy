class Rect:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def detail(self, extra) -> None:
        print(self.length, self.width, extra)

    def culArea(self) -> int:
        return self.length * self.width


rect1 = Rect(2, 4)
rect1.detail("extra")
print(rect1.culArea())
