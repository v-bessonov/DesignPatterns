from Adapter.UsbCable import UsbCable


class MicroToUsbAdapter(UsbCable):
    def __init__(self, micro_usb_cable):
        self.micro_usb_cable = micro_usb_cable
        self.micro_usb_cable.plug_micro_usb()


