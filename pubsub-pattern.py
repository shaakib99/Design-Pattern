class Subscriber:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def sendNotification(msg):
        print(msg)

class Channel:
    def __init__(self) -> None:
        self.subscribers = []
    
    def addSubs(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
    
    def publish(self):
        for subsc in self.subscribers:
            subsc.sendNotification('Sending notification')
    
c = Channel()
c.addSubs(Subscriber())
c.addSubs(Subscriber())
c.addSubs(Subscriber())

c.publish()
