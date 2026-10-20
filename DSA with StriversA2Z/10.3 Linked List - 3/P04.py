class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):

        # Base case: empty list
        if head is None:
            return None

        slow = head
        fast = head

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # If fast becomes None, remove the head
        if fast is None:
            return head.next

        # Move both pointers together
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return head


# Create linked list: 9 -> 8 -> 7
values = [9, 8, 7]

head = ListNode(values[0])
temp = head

for value in values[1:]:
    temp.next = ListNode(value)
    temp = temp.next

n = 3

sol = Solution()
head = sol.removeNthFromEnd(head, n)

# Print the result
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")