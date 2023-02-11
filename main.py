from Builder.BurgerBuilder import BurgerBuilder
from Factory.BurgerFactory import BurgerFactory
from Singleton.ApplicationState import ApplicationState


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


def singleton():
    app_state1 = ApplicationState.get_app_state()
    app_state2 = ApplicationState.get_app_state()
    print(app_state1)
    print(app_state2)


# Design pattern test
if __name__ == '__main__':
    factory()
    builder()
    singleton()
