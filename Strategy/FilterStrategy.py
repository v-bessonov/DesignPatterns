from abc import ABC, abstractmethod


class FilterStrategy(ABC):

    @abstractmethod
    def remove_values(self, val):
        pass
