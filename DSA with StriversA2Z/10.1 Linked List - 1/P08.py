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
def deleteKthNode(head,k):
    if head is None:
        return None
    if k==1:
        return head.next
    cur = head
    for i in range(k-2):
        cur = cur.next
    cur.next=cur.next.next
    return head
result = deleteKthNode(head, 2)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")