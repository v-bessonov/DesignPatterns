from abc import abstractmethod, ABC


class Subscriber(ABC):
    @abstractmethod
    def send_notification(self, event):
        pass
