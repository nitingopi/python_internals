# % strong-type (py)                     weak-type (js, c++)
# % static-type (c, c++)                    dynamic-type (py, js)


# * strong vs weak (strong means can not mix different types)
a = 1
b = "abc"
# c = a + int(b) #! can't do it
c = str(a) + b  # ! it works, typecastes to string
# c = a + b #! gives error
print(c)


#! static vs dynamic (Dynamic means ref can change to another type)
name = 1
name = "nitin"
print(name)
