def show():
    print("showing nothing")

class Person:
    def __init__(this,i, n):
        this.id = i
        this.name = n
        this.show = show

    # def __init__(self):
    #     pass    
    
    def printPerson(me):
        print(me.id, me.name, me.show())
        


    def __del__(self):
        print("deleting", self.id, self.name)


p1 = Person(1, "Guido")
p1.printPerson()

p2 = Person(2, "Rossum")
p2.printPerson()

# print = 4
print("hello")

myprint = print
myprint("hello world")
