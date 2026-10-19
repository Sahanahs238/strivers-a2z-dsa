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
def deleteKthElement(head,k):
    if head is None:
        return None
    if k==1:
        newhead = head.next
        if newhead is not None:
            newhead.prev = None
        return newhead
    cur = head 
    count = 1
    while cur is not None and count <k:
        cur=cur.next
        count+=1
    if cur is None:
        return head
    if cur.prev is not None:
        cur.prev.next=cur.next
    if cur.next is not None:
        cur.next.prev=cur.prev
    return head
res = deleteKthElement(head,1)

# Print the remaining list
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next