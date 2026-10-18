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
def insertAtKthPosition(head, X, k):
    newnode = node(X)
    if head is None:
        return newnode
    if k==1:
        newnode.next=head
        head = newnode
        return head
    cur = head 
    for i in range(k-2):
        cur = cur.next
    newnode.next = cur.next 
    cur.next = newnode
    return head
result = insertAtKthPosition(head,0,5)

while result:
    print(result.data, end=" → ")
    result = result.next

print("None")
