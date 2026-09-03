# This is a simple demo of OOP
# Class is "dog"
# Dog has name, colour and can bark

# Simplest form of class
# This sets up default values, not exactly useful
class Dog:
    name = ""
    colour = ""

    def bark(self):
        print("Wooof!")


def main():
    max = Dog()
    max.name = "Max"
    max.colour = "Golden Brown"
    # test only
    print(max.name, " - ", max.colour)
    max.bark()


if __name__ == "__main__":
    main()
