def add(a, b):
    return a + b 


class Person:
    pass


p = Person() 


print("type of p", type(p))
p.id = 1
p.name = "Guido"
p.plus = add

print(p.id, p.name)
result = p.plus(5, 7)
print(result)