class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head
    tail.next = head
    steps = length - k - 1
    new_tail = head

    while steps > 0:
        new_tail = new_tail.next
        steps -= 1

    new_head = new_tail.next
    new_tail.next = None

    return new_head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
head = rotateRight(head, k)
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")