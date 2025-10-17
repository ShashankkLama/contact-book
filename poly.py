class Animal:
    def sound(self):
        print("some Sound")
        
class Dog(Animal):
    def sound(self):
        print("bark")
        
        
dog= Dog()
animal= Animal()

dog.sound()
animal.sound()