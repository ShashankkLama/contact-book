class Bird:
    def speak(self):
        print ("iam a bird")
        
class parrot (Bird):
    def speak(self):
        print("Hello iam a parrot")
    
b=Bird()
p=parrot()

b.speak()
p.speak()
