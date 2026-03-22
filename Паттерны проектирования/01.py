from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> None:
        pass

class Lion(Animal):
    def make_sound(self) -> None:
        print('Рычание!')

class Monkey(Animal):
    def make_sound(self) -> None:
        print('Визг!')

class Elephant(Animal):
    def make_sound(self) -> None:
        print('Трубление!')

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()
    
def interact_with_animal(factory: AnimalFactory) -> None:
    animal = factory.create_animal()
    animal.make_sound()
