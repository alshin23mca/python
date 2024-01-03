from graphics import rectangle,circle
from graphics.threedgraphics import cuboid,sphere
#using rectangle module
l=int(input("Enter the length: "))
w=int(input("Enter the width: "))
print("Area of a rectangle: ",rectangle.area(l,w))
print("Perimeter of a rectangle: ",rectangle.perimeter(l,w))

#using circle module

r=float(input("Enter the radius: "))
print("Area of the circle: ",circle.area(r))
print("perimeter of the circle: ",circle.perimeter(r))

#using cuboid module

cl=float(input("Enter the c-length: "))
cw=float(input("Enter the c-width: "))
ch=float(input("Enter the c-height: "))
print("Surfacearea of the cuboid: ",cuboid.surfacearea(cl,cw,ch))
print("Volume of cuboid: ",cuboid.volume(cl,cw,ch))



