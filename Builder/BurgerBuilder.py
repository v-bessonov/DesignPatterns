from Builder.Burger import Burger


class BurgerBuilder:

    def __init__(self):
        self.burger = Burger()

    def add_buns(self, buns_style):
        self.burger.set_buns(buns_style)
        return self

    def add_patty(self, patty_style):
        self.burger.set_patty(patty_style)
        return self

    def add_cheese(self, cheese_style):
        self.burger.set_cheese(cheese_style)
        return self

    def build(self):
        return self.burger
