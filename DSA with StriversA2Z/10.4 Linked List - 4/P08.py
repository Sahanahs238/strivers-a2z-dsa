class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addOne(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        carry = 1
        head = prev 
        cur = head
        while cur:
            total = cur.val + carry 
            cur.val = total % 10
            carry = total // 10
            if not cur.next and carry:
                cur.next = ListNode(carry)
                carry = 0
            cur = cur.next
            
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

def make_list(arr):
    if not arr:
        return None
    nodes = [ListNode(x) for x in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("->".join(res))

if __name__ == "__main__":
    solver = Solution()
    head = make_list([4, 5, 9])
    res_head = solver.addOne(head)
    print_list(res_head)
