class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


class Solution:
    def flatten(self, head):
        if head is None or head.next is None:
            return head

        head.next = self.flatten(head.next)

        head = self.merge(head, head.next)

        return head

    def merge(self, a, b):
        if a is None:
            return b

        if b is None:
            return a

        if a.data <= b.data:
            a.child = self.merge(a.child, b)
            return a
        else:
            b.child = self.merge(a, b.child)
            return b


# Create the linked list:
#  5 -> 10 -> 19
#  |    |     |
#  7    20    22
#  |          |
#  8          50
#  |
#  30

head = Node(5)

head.next = Node(10)
head.next.next = Node(19)

head.child = Node(7)
head.child.child = Node(8)
head.child.child.child = Node(30)

head.next.child = Node(20)

head.next.next.child = Node(22)
head.next.next.child.child = Node(50)


# Flatten the linked list
solution = Solution()
head = solution.flatten(head)

# Print the flattened list using child pointers
curr = head
while curr:
    print(curr.data, end=" ")
    curr = curr.child