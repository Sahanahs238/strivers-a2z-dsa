class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortList(self, head):
        zeroHead = zeroTail = None
        oneHead = oneTail = None
        twoHead = twoTail = None

        curr = head

        while curr:
            nxt = curr.next
            curr.next = None

            if curr.data == 0:
                if zeroHead is None:
                    zeroHead = zeroTail = curr
                else:
                    zeroTail.next = curr
                    zeroTail = curr

            elif curr.data == 1:
                if oneHead is None:
                    oneHead = oneTail = curr
                else:
                    oneTail.next = curr
                    oneTail = curr

            else:
                if twoHead is None:
                    twoHead = twoTail = curr
                else:
                    twoTail.next = curr
                    twoTail = curr

            curr = nxt

        if zeroHead:
            zeroTail.next = oneHead if oneHead else twoHead

        if oneHead:
            oneTail.next = twoHead

        if zeroHead:
            return zeroHead
        if oneHead:
            return oneHead
        return twoHead


# Create the linked list: 2 -> 0 -> 1 -> 2 -> 0
values = [2, 0, 1, 2, 0]

head = ListNode(values[0])
temp = head

for value in values[1:]:
    temp.next = ListNode(value)
    temp = temp.next

# Sort the linked list
sol = Solution()
head = sol.sortList(head)

# Print the sorted linked list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")