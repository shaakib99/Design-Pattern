from abc import ABC, abstractmethod
class Strategy:
    def __init__(self,values) -> None:
        self.values = values

    def remove(self, strategy):
        res = []
        for num in self.values:
            if not strategy.filter(num): res.append(num)
        return res

class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, value):
        pass
    
class RemovePostivieStrategy(FilterStrategy):
    def filter(self, value):
        return value > -1
    
class RemoveNegativeStrategy:
    def filter(self, value):
        return value < 0

l = [-1, 0,1,2,3]

strategy = Strategy(l)
print(strategy.remove(RemoveNegativeStrategy()))
print(strategy.remove(RemovePostivieStrategy()))



