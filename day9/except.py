def a():
    raise Exception("this is an exception")
    print("I am A")

def b():
    a()
    print("I am B")

def c():
    b()
    print("I am C") 

def d():
    try:
        c()
    except Exception as e:
        print(e.args[0])   
    print("I am D") 

d()           