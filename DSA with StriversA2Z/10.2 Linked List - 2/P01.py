class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
def convertArrToLL(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1,len(arr)):
        newnode = ListNode(arr[i])
        cur.next = newnode
        newnode.prev=cur
        cur = newnode
    return head
arr = [1, 2, 3, 4]
res = convertArrToLL(arr)

cur = res
while cur is not None:
    print(cur.data, end=" ")
    cur = cur.next