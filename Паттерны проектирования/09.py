class Coffee:
    def get_cost(self):
        return 5

    def get_description(self):
        return "Basic Coffee"
    
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def get_cost(self):
        return self._coffee.get_cost()
    
    def get_description(self):
        return self._coffee.get_description()

class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 1
    
    def get_description(self):
        return f"{self._coffee.get_description()}, Milk"

class ChocolateDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 2
    
    def get_description(self):
        return f"{self._coffee.get_description()}, Chocolate"

class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 3
    
    def get_description(self):
        return f"{self._coffee.get_description()}, Caramel"
