from animal import Animal
class Cat(Animal):

    def __init__(self, cat_name="Stormy"):
        super().__init__(cat_name)

    def sound(self):
        return self.name

def main():
    a = Cat()
    print(a.sound())
if __name__ == '__main__':
    main()
