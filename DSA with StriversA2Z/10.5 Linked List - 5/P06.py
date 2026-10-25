class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        cur = head

        while cur:
            copy_node = Node(cur.val)
            copy_node.next = cur.next
            cur.next = copy_node
            cur = cur.next.next

        cur = head

        while cur:
            copy_node = cur.next

            if cur.random:
                copy_node.random = cur.random.next

            cur = cur.next.next

        dummy_node = Node(0)
        res = dummy_node
        cur = head

        while cur:
            res.next = cur.next
            cur.next = cur.next.next
            res = res.next
            cur = cur.next

        return dummy_node.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.random = head.next.next
head.next.random = head
head.next.next.random = head.next

solution = Solution()
copy_head = solution.copyRandomList(head)

cur = copy_head

while cur:
    random_val = cur.random.val if cur.random else -1
    print(f"Value: {cur.val}, Random: {random_val}")
    cur = cur.next