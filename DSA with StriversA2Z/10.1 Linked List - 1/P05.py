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
def findTarget(head,target):
    cur = head
    while cur is not None:
        if cur.data == target:
            return True
        cur = cur.next
    return False
print(findTarget(head,3))