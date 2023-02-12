from Adapter.MicroToUsbAdapter import MicroToUsbAdapter
from Adapter.MicroUsbCable import MicroUsbCable
from Adapter.UsbCable import UsbCable
from Adapter.UsbPort import UsbPort
from Builder.BurgerBuilder import BurgerBuilder
from Factory.BurgerFactory import BurgerFactory
from Iterator.LinkedList import LinkedList
from Iterator.ListNode import ListNode
from Observer.BroadcastChannel import BroadcastChannel
from Observer.BroadcastSubscriber import BroadcastSubscriber
from Singleton.ApplicationState import ApplicationState
from Strategy.RemoveNegativeStrategy import RemoveNegativeStrategy
from Strategy.RemoveOddStrategy import RemoveOddStrategy
from Strategy.Values import Values


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


def observer():
    channel = BroadcastChannel("FM 101.1")
    channel.subscribe(BroadcastSubscriber("user1"))
    channel.subscribe(BroadcastSubscriber("user2"))
    channel.subscribe(BroadcastSubscriber("user3"))
    channel.notify("New song have released")


def iterator():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    linked_list = LinkedList(head)

    # Iterate through list
    for n in linked_list:
        print(n)


def strategy():
    values = Values([-7, -4, -1, 0, 2, 6, 9])
    print(values.filter(RemoveNegativeStrategy()))
    print(values.filter(RemoveOddStrategy()))


def adapter():
    usb_cable = UsbCable()
    usb_port1 = UsbPort()
    usb_port1.plug_usb(usb_cable)

    micro_to_usb_adapter = MicroToUsbAdapter(MicroUsbCable())
    usb_port2 = UsbPort()
    usb_port2.plug_usb(micro_to_usb_adapter)


# Design pattern test
if __name__ == '__main__':
    factory()
    builder()
    singleton()
    observer()
    iterator()
    strategy()
    adapter()
