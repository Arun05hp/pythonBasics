course = "    Python Programming"
print(course.upper())
# >>    PYTHON PROGRAMMING
course = "python programming"
print(course.title())
#>> Python Programming

course = "    Python Programming"
print(course.strip())  # lstip  and rstrip
# >> Python Programming

course = "    Python Programming"
print(course.find("Py"))    # return Index of word
# >> 4

print(course.find("py"))
# >> -1   return -1 when word not found Because Python is a case-sensitive language. so "py" != "Py"

print(course.replace("Python","Py"))
# >>    Py Programming

print("pro" in course)
# >>    False

print("pro" not in course)
# >>    True