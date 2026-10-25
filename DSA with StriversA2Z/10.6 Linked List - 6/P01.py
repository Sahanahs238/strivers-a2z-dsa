class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head, target):
    cur = head

    while cur:
        if cur.val == target:
            if cur.prev:
                cur.prev.next = cur.next
            else:
                head = cur.next

            if cur.next:
                cur.next.prev = cur.prev

        cur = cur.next

    return head


head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(1)
fifth = ListNode(4)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

head = deleteAllOccurrences(head, 1)

cur = head
while cur:
    print(cur.val, end=" <-> ")
    cur = cur.next

print("None")
