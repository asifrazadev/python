# Object-Oriented Programming (OOP) in Python
# Classes and Objects

class Human:
    # Constructor method to initialize attributes
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    # Instance method
    def do_work(self):
        if self.occupation == "actor":
            print(f"{self.name} shoots movies")
        elif self.occupation == "tennis player":
            print(f"{self.name} plays tennis")
        else:
            print(f"{self.name} does generic work")

    # Instance method
    def speaks(self):
        print(f"{self.name} says: How are you?")

# Creating instances (objects) of the Human class
tom = Human("Tom Cruise", "actor")
tom.do_work()
tom.speaks()

print("-" * 20)

maria = Human("Maria Sharapova", "tennis player")
maria.do_work()
maria.speaks()
