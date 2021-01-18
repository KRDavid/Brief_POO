import abc

class Vegetable(abc.ABC):

    @abc.abstractmethod
    def grow(self):
        pass
