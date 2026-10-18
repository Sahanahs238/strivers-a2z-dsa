class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
first = Node(5)
second = Node(4)
third = Node(3)
fourth = Node(2)
fifth = Node(1)
head = first 
first.next = second
second.next = third
third.next=fourth
fourth.next = fifth
def LLTraversal(head):
    res=[]
    current = head
    while current is not None:
        res.append(current.data)
        current = current.next
    return res
print(LLTraversal(head))