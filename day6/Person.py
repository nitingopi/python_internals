class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name


    def print(self):
        print(self.id, self.name) 


nitin = Person(1, "nitin")
nitin.print()           