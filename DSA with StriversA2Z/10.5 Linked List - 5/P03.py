class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next


list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(7)
list1.next.next.next = ListNode(9)

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(5)
list2.next.next.next = ListNode(6)
head = mergeTwoLists(list1, list2)
curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next

print("None")