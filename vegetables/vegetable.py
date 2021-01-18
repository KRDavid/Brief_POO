import abc

class Vegetable(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def grow(self):
        pass

    @abc.abstractmethod
    def getSeedNumber(self):
        pass