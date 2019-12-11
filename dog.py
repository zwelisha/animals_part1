from animal import Animal
class Dog(Animal):

    def __init__(self, dog_name='Rax'):
        super().__init__(dog_name)

    def sound(self):
        print('Dog barks')

    def eat(self):
        print(self.name + ' eats')
