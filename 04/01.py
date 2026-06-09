from abc import ABC, abstractmethod

class BaseObject(ABC):
    def __init__(self, x, y, z):
        self.x = self.x
        self.y = self.y
        self.z = self.z

    @abstractmethod
    def get_coordinates(self):
        return self.x, self.y, self.z
    
class Block(BaseObject):
    def shatter(self) -> None:
        self.x = None 
        self.y = None 
        self.z = None 

class Entity(BaseObject):
    def move(self, x, y, z) -> None:
        self.x = x
        self.y = y 
        self.z = z

class Thing(BaseObject):
    pass
