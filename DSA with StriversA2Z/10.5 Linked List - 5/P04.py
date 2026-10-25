class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(second)

    return merge(left, right)


def merge(list1, list2):
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next

    cur.next = list1 if list1 else list2

    return dummy.next


head = ListNode(5)
head.next = ListNode(6)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

head = sortList(head)

cur = head
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next

print("None")
