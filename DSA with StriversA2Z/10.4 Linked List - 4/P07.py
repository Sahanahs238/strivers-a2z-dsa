class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findLengthOfLoop(self, head: ListNode) -> int:
        fast = head 
        slow = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                count = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next 
                    count += 1
                return count
        return 0

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
    print(solver.findLengthOfLoop(head))
