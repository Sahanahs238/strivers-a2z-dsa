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
def insertBeforeKthPosition(head,X,K):
    newnode = Node(X)
    if head is None:
        return newnode
    if K==1:
        newnode.next=head
        head.prev=newnode
        return newnode
    cur = head
    for i in range(K-1):
        if cur.next is None:
            break
        cur=cur.next
    cur.prev.next=newnode
    newnode.prev = cur.prev
    newnode.next=cur
    cur.prev=newnode
    return head
res = insertBeforeKthPosition(head,7,2)

# Print the remaining list
cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next
