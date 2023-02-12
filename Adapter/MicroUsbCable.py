class MicroUsbCable:
    def __init__(self):
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True
        print('MicroUsbCable plugged')

