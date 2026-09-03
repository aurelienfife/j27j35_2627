# Car - demonstrating encapsulation
# Adding type hints, example of practice
class Car:
    def __init__(self, make: str, model: str):
        self.make: str = make
        self.model: str = model

        # Speed is a private attribute (integer)
        self.__speed: int = 0

    # 'getter' function (read_only access to speed)
    def getSpeed(self):
        return self.__speed

    # Accelerate, by default 10 MPH
    def accelerate(self, extra_mph: int = 10):
        self.__speed += extra_mph

    def slow_down(self, less_mph: int = 10):
        self.__speed -= less_mph
        # Ternary operator
        self.__speed = self.__speed if self.__speed > 0 else 0

    def stop(self):
        self.__speed = 0

    

def main():
    c = Car("Renault", "Clio")
    print(c.getSpeed())

    c.accelerate()
    print(c.getSpeed())

    c.accelerate(15)
    print(c.getSpeed())

    c.slow_down()
    print(c.getSpeed())

    c.stop()
    print(c.getSpeed())



if __name__ == "__main__":
    main()
