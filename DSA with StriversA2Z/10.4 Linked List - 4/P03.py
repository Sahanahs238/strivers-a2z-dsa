class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        new_head = self.reverse(slow.next)
        
        first = head
        second = new_head
        is_palindrome = True
        
        while second:
            if first.val != second.val:
                is_palindrome = False
                break
            first = first.next
            second = second.next
            
        slow.next = self.reverse(new_head)
        return is_palindrome


def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    sol = Solution()

    test_case_1 = build_linked_list([1, 2, 2, 1])
    result_1 = sol.isPalindrome(test_case_1)
    print(f"Input: [1, 2, 2, 1] -> Output: {result_1}")

    test_case_2 = build_linked_list([1, 2, 3])
    result_2 = sol.isPalindrome(test_case_2)
    print(f"Input: [1, 2, 3]    -> Output: {result_2}")
