from animal import Animal

class Dog(Animal):
    def breathe(self):
          super().breathe()
          print("Dogs love to breathe with their mouths open.")

    def walk(self):
        super().walk()
        print("Dogs love to run")
    
    def summary(self):
            print(
                "This is an instance of [" + type(self).__name__ + "]. It has ["
                + str(self.get_number_of_legs())
                + "] legs and ["
                + str(self.get_number_of_eyes()) + "] eyes."
            )



'''
class Spider(Animal): #just experimenting

    def __init__(self):
        super().__init__(8, 8)

    def breathe(self):
        print("Spiders breathe through their skin.")

    def walk(self):
        print("Spiders have 8 legs to walk with.")

    def summary(self):
            print(
                "This is an instance of [" + type(self).__name__ + "]. It has ["
                + str(self.get_number_of_legs())
                + "] legs and ["
                + str(self.get_number_of_eyes()) + "] eyes."
            )

print('\n')
spider = Spider()
spider.breathe()
spider.walk()
spider.summary()

'''