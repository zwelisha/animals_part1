import pytest
from home import Home
from cat import Cat
from dog import Dog

def test_dog_eats():
    dog = Dog()
    dog.eat()
    captured = capsys.readouterr()
    assert captured.out == "Rax eats"
