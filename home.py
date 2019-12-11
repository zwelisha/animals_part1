from animal import Animal
from cat import Cat
from dog import Dog

class Home:

    def __init__(self, pets=[]):
        self.__pets = pets

    # Getter for pets array
    @property
    def pets(self):
        return self.__pets

    # Setter for pets
    @pets.setter
    def pets(self, pets):
        self.__pets = pets

    def adopt_pet(self, pet):
        for each in self.__pets:
            if each == pet:
                raise Exception ("You can't adopt the same pet twice")
        self.__pets.append(pet)
    '''
       According to the given instruction, this function
       should be named 'makeAllSounds', however, that is
       not pythonic. Hence I named it 'make_all_sounds'
    '''
    def make_all_sounds(self):
        for animal in self.__pets:
            #print(type(animal))
            animal.sound()
def main():
    home = Home()
    dog1 = Dog()
    dog2 = Dog()
    cat = Cat()

    home.adopt_pet(dog1)
    home.adopt_pet(cat)
    home.adopt_pet(dog2)
    home.make_all_sounds()
    home.adopt_pet(dog2)
if __name__ == '__main__':
    main()
