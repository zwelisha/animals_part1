from animal import Animal
class Cat(Animal):

    def __init__(self, cat_name='Storm'):
        super().__init__(cat_name)

    def sound(self):
        print('Cat meows')

    def eat(self):
        print(self.name + 'y' +' eats')




def main():
    cat = Cat()
    cat.eat()
    cat.sound()

if __name__ == '__main__':
    main()
