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
def reverseDLL(head):
    cur = head 
    while cur:
        cur.prev,cur.next=cur.next,cur.prev
        head=cur
        cur = cur.prev
    return head
res = reverseDLL(head)
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next