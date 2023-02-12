class Values:
    def __init__(self, values):
        self.values = values

    def filter(self, strategy):
        res = []
        for n in self.values:
            if not strategy.remove_values(n):
                res.append(n)
        return res
