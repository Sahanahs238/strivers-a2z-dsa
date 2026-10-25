class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findStartingPoint(self, head: ListNode) -> ListNode:
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head 
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

def make_list(arr, pos):
    if not arr:
        return None
    nodes = [ListNode(x) for x in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes

if __name__ == "__main__":
    solver = Solution()
    head = make_list([3, 2, 0, -4], 1)
    result = solver.findStartingPoint(head)
    print(result.val if result else None)
