class UsbCable:
    def __init__(self) -> None:
        pass

    def plugToUsb(self):
        pass

class UsbPort:
    def __init__(self) -> None:
        pass

    def plugCable(self, usbCable:UsbCable):
        usbCable.plugToUsb()

class MicroUsbCable:
    def __init__(self) -> None:
        pass

    def plugToMicroUsb(self):
        pass

class MicroUsbToUsbAdapter(UsbCable):
    def __init__(self, microsUsbCable: MicroUsbCable) -> None:
        self.microsUsbCable = microsUsbCable
        self.microsUsbCable.plugToMicroUsb()
    def plugToUsb(self):
        return print('plug to micro usb to usb port done')


usbPort = UsbPort()
usbPort.plugCable(UsbCable())
adapter = MicroUsbToUsbAdapter(MicroUsbCable())
usbPort.plugCable(adapter)
