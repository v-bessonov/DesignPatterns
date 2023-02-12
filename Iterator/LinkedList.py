class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            val = self.current.val
            self.current = self.current.next
            return val
        else:
            raise StopIteration
        