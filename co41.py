class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	
	def area(self):
		return self.length*self.breadth
	
	def perimeter(self):
		return 2*(self.length+self.breadth)
	
	def compare(self,other_rectangle):
		if self.area()>other_rectangle.area():
			print("first rect is largest")
		else:
			print("second rect is largest")
		
	
print("1st rectangle")
length=int(input("Enter the length: "))	
breadth=int(input("Enter the breadth: "))
rectangle1=Rectangle(length,breadth)
print("Area of rectangle 1: ",rectangle1.area())
print("perimeter of rectangle 1: ",rectangle1.perimeter())

print("\n\n2nd rectangle")
length=int(input("Enter the length: "))	
breadth=int(input("Enter the breadth: "))
rectangle2=Rectangle(length,breadth)
print("Area of rectangle 1: ",rectangle2.area())
print("perimeter of rectangle 1: ",rectangle2.perimeter())
rectangle1.compare(rectangle2)

