class node:
    def __init__(self,data):
        self.data = data
        self.next = None
first = node(4)
second = node(2)
third = node(1)
head = first 
first.next = second
second.next = third
def LLInsertion(head):
    newnode = node(3)
    newnode.next=first.next
    first.next=newnode
    res = []
    current = head
    while current is not None:
        res.append(current.data)
        current = current.next
    return res
print(LLInsertion(head))