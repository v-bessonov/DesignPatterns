class UsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True
        print('UsbCable plugged')
