class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def findPairsWithGivenSum(target, head):
    ans = []

    if not head:
        return ans

    left = head
    right = head

    while right.next:
        right = right.next

    while left != right and left.prev != right:
        total = left.val + right.val

        if total == target:
            ans.append([left.val, right.val])
            left = left.next
            right = right.prev

        elif total < target:
            left = left.next

        else:
            right = right.prev

    return ans


values = [1, 2, 4, 5, 6, 8, 9]

head = Node(values[0])
cur = head

for val in values[1:]:
    new_node = Node(val)
    cur.next = new_node
    new_node.prev = cur
    cur = new_node

target = 7
print(findPairsWithGivenSum(target, head))
