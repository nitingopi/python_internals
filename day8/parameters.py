
#! Formal params (arguments)
def add(a, b):
    return a + b 

def long_fun(w,h,t,l):
    print(f"w={w} h={h} t={t} l={l}")

long_fun(1,2,3,4)
# named parameters (keyword argument)
long_fun(w=1, h=2, t=3, l=4)
long_fun(h=2, t=3, l=4, w=1)

#*    Actual params (arguments)
result = add( 5, 7)


print(1,2,3,sep=">>>>>",end="\n")

# before / we can't give named param
def funfunfun(p1, /, p2):
    print(p1, p2, end="\t")


funfunfun(5,6)    

# after * we should add named params
def doublefun(p1, /, p2, *, p3):
    print(p1, p2, p3)


doublefun(1,2,p3=3)


#% varargs ( variable arguments )
def sum(*args):
    print(args)

sum(1,2,3,4,5)    