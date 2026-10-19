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
def insertBeforeGivenNode(node,X):
    if not node:
        return
    newnode = Node(X)
    newnode.next=node
    newnode.prev=node.prev
    if node.prev:
        node.prev.next=newnode
    node.prev=newnode
insertBeforeGivenNode(third, 7)
cur = head
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next