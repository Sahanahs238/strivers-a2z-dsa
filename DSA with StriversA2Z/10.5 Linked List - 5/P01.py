class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getkth(cur, k):
    while cur and k > 1:
        cur = cur.next
        k -= 1
    return cur


def reverse(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


def reverseKGroup(head, k):
    if not head or k <= 1:
        return head

    tail = None
    cur = head

    while cur:
        kth = getkth(cur, k)

        if not kth:
            if tail:
                tail.next = cur
            break

        next_group = kth.next
        kth.next = None

        reverse(cur)

        if tail:
            tail.next = kth
        else:
            head = kth

        tail = cur
        cur = next_group

    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
head = reverseKGroup(head, k)

while head:
    print(head.val, end=" -> ")
    head = head.next
print("None")