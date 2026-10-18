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
def deleteNodeWithValueX(head, X):
    if head is None:
        return None 
    if head.data == X:
        return head.next
    cur = head
    while cur.next is not None and cur.next.data!=X:
        cur = cur.next
    if cur.next is None:
        return head
    cur.next=cur.next.next
    return head
result = deleteNodeWithValueX(head, 2)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")