class Animal:
    def __init__(self, name):
        self.name= name
        
        
    def make_sound(self):
        print ("Some generic animal sound")
        
        
class Dog(Animal):
    def make_sound(self):
        print ("Bark, Bark")
        
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")

dog = Dog("buddy")
cat= Cat("Whisker")
animal= Animal("wow")

dog.make_sound() 
cat.make_sound()
animal.make_sound()