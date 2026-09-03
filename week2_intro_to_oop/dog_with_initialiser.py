# This is a simple demo of OOP
# Class is "dog"
# Dog has name, colour and can bark

# Simplest form of class
# This sets up default values, not exactly useful
class Dog:
    # Pass 'self' as paramater 1 so function knows 
    # how to 'find' the class
    def __init__(self, name, colour):
        # Here we create two variables embedded in the
        # class, so using self.--- syntax
        # That's why we needed "self" in the function args
        self.name = name
        self.colour = colour

    def bark(self):
        print(f"Wooof! I am {self.name} and my colour is {self.colour}!")
        print("Woof!")
    

def main():
    max = Dog("Max", "Golden Brown")
    hamish = Dog("Hamish", "Ginger")

    max.bark()
    hamish.bark()


if __name__ == "__main__":
    main()
