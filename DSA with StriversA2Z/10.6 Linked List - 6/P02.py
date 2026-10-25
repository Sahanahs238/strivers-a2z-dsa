class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def removeDuplicates(head):
    cur = head

    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next

            if cur.next:
                cur.next.prev = cur
        else:
            cur = cur.next

    return head
head = Node(1)
head.next = Node(1)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(3)
head.next.next.next.next.prev = head.next.next.next
head = removeDuplicates(head)
cur = head
while cur:
    print(cur.val, end=" <-> ")
    cur = cur.next

print("None")