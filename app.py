import math

from check import print_rectangle_properties

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_width(self: float):
        return self.width
    
    def get_height(self: float):
        return self.height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"
    
def main():
    rectangle = Rectangle(5, 10)
    print_rectangle_properties(rectangle)

    rectangle = Rectangle(3, 6)
    print_rectangle_properties(rectangle)


if __name__ == "__main__":
    main()
