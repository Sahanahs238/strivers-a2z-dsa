class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# Create linked list: 1 -> 2 -> 3 -> 4 -> None
values = [1, 2, 3, 4]

head = ListNode(values[0])
temp = head

for value in values[1:]:
    temp.next = ListNode(value)
    temp = temp.next

# Reverse the linked list
sol = Solution()
head = sol.reverseList(head)

# Print the reversed linked list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")