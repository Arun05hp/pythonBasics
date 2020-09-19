####### class vs instance attributes ########

# class Point:
#     default_color = "red"           # This is a class level attributes that is shared accross all objects
#     def __init__(self,x,y):    #constructor 
#         self.x = x                                # self is ref to the current obj
#         self.y = y                                 # x and y are  instance attributes       
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# Point.default_color = "yellow"
# point = Point(1, 2)
# print(type(point))
# print(isinstance(point,Point))
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another = Point(3,4)
# another.draw()
# print(another.default_color)


###### class vs instance methods #######



# class Point:         
#     def __init__(self,x,y):    
#         self.x = x                              
#         self.y = y       

#     @classmethod        #to make class method we need decorator
#     def zero(cls):                # class method
#         return cls(0,0)             #This is same as calling Point(0,0)

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()
# point.draw()

######## Magic Methods ########

class Point:
    def __init__(self,x,y):    # __init__    magic method.on print this return __main__
        self.x = x
        self.y = y
    def __str__(self):           # __str__    magic method
        return f"({self.x},{self.y})"

    def draw(self):
        print(f" Point ({self.x} , {self.y})")

point = Point(1,2)
point.draw()
print(point)
print(str(point))
