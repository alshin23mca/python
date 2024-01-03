
from graphics.figure import square,triangle
#using square module
s=int(input("Enter the length: "))
print("Area of a square: ",square.sarea(s))
print("Perimeter of a rectangle: ",square.perimeter(s))

#using triangle module
b=int(input("Enter base: "))
h=int(input("Enter the width: "))
print("Area of a triangle: ",triangle.sarea(b,h))

