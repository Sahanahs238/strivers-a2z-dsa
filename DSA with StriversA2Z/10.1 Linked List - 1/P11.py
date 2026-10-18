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
def insertAtTail(head, X):
    newnode = node(X)
    if head is None:
        return newnode
    cur = head 
    while cur.next is not None:
        cur = cur.next
    cur.next = newnode
    return head 
result = insertAtTail(head, 0)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")
