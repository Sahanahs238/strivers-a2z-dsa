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
def DeleteHead(head):
    head = head.next
    res= []
    cur = head
    while cur is not None:
        res.append(cur.data)
        cur = cur.next
    return res
print(DeleteHead(head))