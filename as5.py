class Shape:
	def area(self,area=0):
		self.area=area
		print(self.area)	
class Square(Shape):
	def __init__(self,leng):
		self.leng=leng
	def area(self):
		self.area=self.leng**2
		print(self.area)
sh=Shape()
sh.area(5)
sq=Square(int(input("length: ")))
sq.area()