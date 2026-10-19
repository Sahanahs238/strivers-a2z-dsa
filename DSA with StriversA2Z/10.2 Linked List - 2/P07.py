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
def insertBeforeTail(head,X):
    newnode = Node(X)
    if head is None:
        return newnode
    cur = head 
    while cur.next is not None:
        cur=cur.next
    if cur.prev is None:
        newnode.next=cur
        cur.prev=newnode
        return newnode
    cur.prev.next=newnode
    newnode.prev=cur.prev
    newnode.next=cur
    cur.prev = newnode 
    return head
res = insertBeforeTail(head,0)

# Print the remaining list
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next