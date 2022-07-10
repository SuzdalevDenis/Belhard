class Rectangle:
    def __init__(self, x: tuple[int], y: tuple[int]):
        self.x = x
        self.y = y

    def __length(self):
        length = abs(self.x[0]) + abs(self.y[0])
        height = abs(self.x[1]) + abs(self.y[1])
        return length, height


    def perimeter(self) -> int:
        length = self.__length()
        return sum(length) * 2

    def area(self):
        length = self.__length()
        return length[0] * length[1]


