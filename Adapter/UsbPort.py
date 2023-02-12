class UsbPort:
    def __init__(self):
        self.port_available = True

    def plug_usb(self, usb):
        if self.port_available:
            usb.plug_usb()
            self.port_available = False
