class Phone:
    def __init__(self):
        pass

    def setRam(self, ram):
        self.ram = ram
        return self

    def setProcessor(self, processor):
        self.processor = processor
        return self

class PhoneBuilder:
    def __init__(self, phone):
        self.phone = phone
    
    def addRam(self, ram):
        self.phone.setRam(ram)
        return self

    def addProcessor(self, processor):
        self.phone.setProcessor(processor)
        return self

    def build(self):
        print(self.phone.ram)
        return self.phone


phone = PhoneBuilder(Phone()) \
            .addRam('8gb') \
            .addProcessor('i3') \
            .build()
