class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


def addTwoNumbers(l1,l2):
    return_list = ListNode(0)
    head = return_list
    carry =0 
    while l1 or l2 or carry:
        cur_sum =0
        if l1:
            cur_sum+=l1.val
            l1=l1.next
        if l2:
            cur_sum+=l2.val
            l2=l2.next
        cur_sum += carry 
        digit = cur_sum%10
        carry = cur_sum//10
        return_list.next=ListNode(digit)
        return_list = return_list.next
    return head.next
l1 =ListNode(2,ListNode(4,ListNode(3)))
l2 =ListNode(5,ListNode(6,ListNode(4)))
result = addTwoNumbers(l1,l2)
while result:
    print(result.val, end=" ")
    result=result.next