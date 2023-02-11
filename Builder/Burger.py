class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def set_buns(self, buns_style):
        self.buns = buns_style

    def set_patty(self, patty_style):
        self.patty = patty_style

    def set_cheese(self, cheese_style):
        self.cheese = cheese_style

    def __str__(self):
        return f'buns: {self.buns}; patty: {self.patty}; cheese: {self.cheese};'
