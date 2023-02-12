class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2

    def push_back(self, n):
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def resize(self):
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def pop_back(self):
        if self.length > 0:
            self.length -= 1
