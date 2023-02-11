class BroadcastChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.send_notification(self.name, event)

