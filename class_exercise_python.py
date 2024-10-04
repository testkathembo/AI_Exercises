#  Polymorphism

import random
import math

# Base class for shapes
class Shape:
    def computeArea(self):
        pass  # To be implemented by each specific shape class
    
    def __str__(self):
        return self.__class__.__name__  # Return the class name for representation

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def computeArea(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def computeArea(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

# Square class (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def __str__(self):
        return f"Square(side_length={self.width})"

# Create a list of 100 random shapes
def create_random_shapes(num_shapes=100):
    shapes = []
    for _ in range(num_shapes):
        shape_type = random.choice([Rectangle, Circle, Square])
        if shape_type == Rectangle:
            width = random.uniform(1, 10)
            height = random.uniform(1, 10)
            shapes.append(Rectangle(width, height))
        elif shape_type == Circle:
            radius = random.uniform(1, 10)
            shapes.append(Circle(radius))
        elif shape_type == Square:
            side_length = random.uniform(1, 10)
            shapes.append(Square(side_length))
    return shapes

# Calculate the sum of areas of the shapes
def compute_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.computeArea()
    return total_area

# Main program
random_shapes = create_random_shapes()
for shape in random_shapes:
    print(f"{shape}: Area = {shape.computeArea()}")

total_area = compute_total_area(random_shapes)
print(f"\nTotal area of all shapes: {total_area:.2f}")
