class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

if __name__ == "__main__":
    intersect = ListNode(8)
    intersect.next = ListNode(4)
    intersect.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect

    sol = Solution()
    result = sol.getIntersectionNode(headA, headB)

    if result:
        print(f"Intersected at node with value: {result.val}")
    else:
        print("No intersection found")
