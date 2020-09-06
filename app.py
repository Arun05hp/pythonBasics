# print("Hello World")
# print("*" * 10);
#
# price= 10
# boolean = 0
# print(boolean)
# name = input("Enter Name: ")
# color = input("What is your favorite Color: ")
# print(name+ ' Likes ' + color)

# birth_year = input('Birth year :  ')
# age = 2020 - int(birth_year)
# print(age)

# weight_lbs = input("Weight lbs: ")
# w_kg =int(weight_lbs) * 0.45
# print(w_kg)

name = "Arun"
print(name[1:-1])

def fizz_buzz(input):
    if input % 3==0 and input %5 ==0:
        print("fizzbuzz")
    if input % 5 ==0:
        print("Buzz")
    if input %3==0:
        print("fizz")
    print(input)


fizz_buzz(5)