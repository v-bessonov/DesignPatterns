from Observer.Subscriber import Subscriber


class BroadcastSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def send_notification(self, channel, event):
        print(f'User {self.name} received notification from {channel}: {event}')
