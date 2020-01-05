import math

class GeometricObject:
	def __init__(self):
		pass
		
class Triangle(GeometricObject):
	def __init__(self, side1 = 1.0,  side2 = 1.0, side3 = 1.0):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
		GeometricObject.__init__(self)
		
	def getLengthA(self):
		return side1
	def getLengthB(self):
		return side2
	def getLengthC(self):
		return side3
	
	# setting perimeter
	def setPerimeter(self):
		self.perimeter = perimeter
		
	#getting perimeter
	def getPerimeter(self):
		perimeter = self.side1 + self.side2 + self.side3
		return perimeter
		
	#setting area
	def setArea(self):
		self.area = area
	
	#getting area
	def getArea(self):
		s = (self.side1 + self.side2 + self.side3)/2
		area = (s * ((s - self.side1)* (s - self.side2) * (s - self.side3)))**1/2
		return area
	
	def __str__(self):
		return "Triangle: Side1: " + (self.side1) + "Side2: " + (self.side2) + "Side3: " + (self.side3)
		
a = Triangle(int(input('enter the first side here: ')), int(input('enter the second side here: ')), int(input('enter the third side: ')))

print("The Area of the Triangle is", a.getArea())
print("The Perimeter of the Triangle is", a.getPerimeter())
	