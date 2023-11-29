class Phone:
    def __init__(self, ram) -> None:
        self.ram = ram

class PhoneFactory:
    def __init__(self) -> None:
        pass

    def get4gbRamPhone(self):
        return Phone('4gb')
    
    def get8GbRamPhone(self):
        return Phone('8gb')

phoneFactory = PhoneFactory()
phone1 = phoneFactory.get4gbRamPhone()
phone2 = phoneFactory.get8GbRamPhone()
