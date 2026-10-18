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
def deleteTail(head):
    if head is None or head.next is None :
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head
result = deleteTail(head)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")