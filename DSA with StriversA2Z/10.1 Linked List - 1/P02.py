class node:
    def __init__(self,data):
        self.data=data
        self.next = None
first = node(4)
second = node(3)
third = node(2)
fourth = node(1)
head = first 
first.next = second
second.next=third
third.next=fourth
def LLDeletion3(head):
    first.next =third
    res = []
    current = head 
    while current is not None:
        res.append(current.data)
        current = current.next
    return res
print(LLDeletion3(head))