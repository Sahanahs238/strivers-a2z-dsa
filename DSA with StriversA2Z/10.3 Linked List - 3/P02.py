class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head


# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Run the solution
sol = Solution()
result = sol.oddEvenList(head)

# Print the result
while result:
    print(result.data, end=" -> ")
    result = result.next

print("None")