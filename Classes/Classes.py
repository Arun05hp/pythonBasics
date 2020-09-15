class Point:
    def __init__(self,x,y):    #constructor 
        self.x = x                                # self is ref to the current obj
        self.y = y
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(type(point))
print(isinstance(point,Point))
point.draw()