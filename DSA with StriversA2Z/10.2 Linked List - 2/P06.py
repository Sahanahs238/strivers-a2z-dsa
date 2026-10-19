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
def deleteGivenNode(node: Node,current_head: Node):
    if node is None:
        return current_head
    if node == current_head:
        current_head = node.next
    if node.next is not None:
        node.next.prev = node.prev
    if node.prev is not None:
        node.prev.next =node.next
    node.next=None
    node.prev=None
    return current_head
res = deleteGivenNode(first,head)

# Print the remaining list
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next