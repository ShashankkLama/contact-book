class Grandparent:
    def family_name(self):
        print("We are the Smiths")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.family_name() 