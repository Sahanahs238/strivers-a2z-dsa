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
def FindLen(head):
    cur = head 
    count =0
    while cur is not None :
        count +=1
        cur = cur.next
    return count
print(FindLen(head))
        