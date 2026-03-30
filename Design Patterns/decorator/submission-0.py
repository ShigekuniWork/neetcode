class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, Coffee):
        super().__init__(coffee)
        self.milkCost = 0.5
    
    def getCost(self):
        return super().getCost() + self.milkCost

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.sugarCost = 0.2
    
    def getCost(self):
        return super().getCost() + self.sugarCost

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.creamCost = 0.7
    
    def getCost(self):
        return super().getCost() + self.creamCost

