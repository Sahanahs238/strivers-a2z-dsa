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
def insertBeforeX(head, X, val):
    newnode = node(val)
    if head is None:
        return newnode
    if head.data ==X:
        newnode.next = head
        head = newnode
        return head
    cur = head
    while cur.next is not None and cur.next.data != X:
        cur = cur.next

    if cur.next is None:
        return head

    newnode.next = cur.next
    cur.next = newnode
    return head
result = insertBeforeX(head,1,5)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")
