try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)

#### handling multiple exceptions ####
try:
    age = int(input("Age: "))
    x = 10/age
except (ValueError,ZeroDivisionError):
    print("You didn't enter a valid age")
   

try: 
    file = open("../app.py")
    num=int(input("Enter number: "))
except ValueError:
    print("Not valid number")
finally:     #this final clause is always executed.
    file.close()

    
try: 
    with open("../app.py") as file:
        print("File opened")
    num=int(input("Enter number: "))
except FileNotFoundError:
     print("Not valid number")
