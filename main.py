from Builder.BurgerBuilder import BurgerBuilder
from Factory.BurgerFactory import BurgerFactory


def factory():
    burger_factory = BurgerFactory()
    burger_factory.create_cheese_burger().print()
    burger_factory.create_deluxe_cheese_burger().print()
    burger_factory.create_vegan_burger().print()


def builder():
    burger = BurgerBuilder() \
        .add_buns("sesame") \
        .add_patty("fish-patty") \
        .add_cheese("swiss cheese") \
        .build()
    print(burger)


# Design pattern test
if __name__ == '__main__':
    factory()
    builder()
