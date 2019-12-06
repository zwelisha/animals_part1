class Animal:
    def __init__(self, animal_name):
        self.__name = animal_name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name_value):
        self.__name = name_value
    def sound(self):
        print("the animal sounds")

    def eat(self):
        print(name + "eats")




def main():
    animal = Animal("cow")
    print(animal.name)
    animal.sound()
    animal.name = "kudu"
    print(animal.name)
if __name__ == '__main__':
    main()
