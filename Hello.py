x = 5
y = 7

def add(a, b):
    print("locals", locals())
    return a + b

print(add(x, y))    
print(add)
msg = "hello world"
print(msg)
