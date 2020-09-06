# x = input("X: ")
#
# y = int(x) + 1
#
# print(y)
# print(f"x: {x}, y: {y} ")
# X: 12
# 13
# x: 12, y: 13

###  Falsy Value

# ""
# 0
# None

print(bool(""))
# False

print(bool(-1))
#  True

print(bool("False"))
# True

print(bool(None))
# False

count=0
for number in  range (1,10):
    if number % 2 == 0:
        print(number)
        count +=1
else:
    print(f"We have {count} even numbers")