class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
r=float(input("Enter the radius :"))
NewCircle = Circle(r)
print(NewCircle.area())
