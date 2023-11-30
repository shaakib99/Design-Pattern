class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class List:
    def __init__(self, head) -> None:
        self.head = head
        self.curr = self.head
    
    def __iter__(self):
        self.curr = self.head
        return self
    
    def __next__(self):
        if self.curr:
            val = self.curr.val
            self.curr = self.curr.next
            return val
        raise StopIteration

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

lnums = List(head)

for num in lnums:
    print(num)