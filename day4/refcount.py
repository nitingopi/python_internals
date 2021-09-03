import sys

x = 5 

print("value", x)
print("type", type(x))
print("id", id(x))
print("refcount", sys.getrefcount(x))
y = 5 
print("refcount", sys.getrefcount(x))
y = None
print("refcount", sys.getrefcount(x))
