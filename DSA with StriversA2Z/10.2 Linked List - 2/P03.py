class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
first = Node(1)
second = Node(2)
third = Node(3)
Fourth = Node(4)
head = first 
first.next =second
second.prev=first
second.next=third
third.prev=second
third.next=Fourth
Fourth.prev=third
tail = Fourth
def deletehead(head):
    if head is None or head.next is None:
        return None
    head = head.next 
    head.prev = None
    return head
res = deletehead(head)

# Print the remaining list
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next
