class CommonPhone:
    instance = None
    def __init__(self) -> None:
        self.inuse = False
    
    @staticmethod
    def getPhone():
        if not CommonPhone.instance:
            CommonPhone.instance = CommonPhone()
        return CommonPhone.instance

user1 = CommonPhone.getPhone()
user1.inuse = True
user2 = CommonPhone.getPhone()

print(user2.inuse)