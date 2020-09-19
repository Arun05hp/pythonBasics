class Point:
    default_color = "red"           # This is a class level attributes that is shared accross all objects
    def __init__(self,x,y):    #constructor 
        self.x = x                                # self is ref to the current obj
        self.y = y                                 # x and y are  instance attributes       
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(type(point))
print(isinstance(point,Point))
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3,4)
another.draw()
print(another.default_color)