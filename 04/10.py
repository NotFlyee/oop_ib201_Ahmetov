class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self) -> int | float:
        return self.a + self.b + self.c 
    
class EquilateralTriangle(Triangle):
    def __init__(self, side_len: int):
        super().__init__(side_len, side_len, side_len)
