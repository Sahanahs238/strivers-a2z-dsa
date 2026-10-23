class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def make_list(arr, pos):
    if not arr:
        return None
    
    nodes = [ListNode(x) for x in arr]
    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        
    if pos != -1:
        nodes[-1].next = nodes[pos]
        
    return nodes[0]

if __name__ == "__main__":
    solver = Solution()
    
    # Case 1: Has a cycle (ends loops back to index 1)
    head1 = make_list([3, 2, 0, -4], 1)
    print("Test 1:", solver.hasCycle(head1))
    
    # Case 2: No cycle
    head2 = make_list([1, 2, 3], -1)
    print("Test 2:", solver.hasCycle(head2))
