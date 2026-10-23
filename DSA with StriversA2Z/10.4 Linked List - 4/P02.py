# 1. Define the node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head 
    fast = fast.next.next  
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = slow.next.next  # Skip/delete the middle node
    return head

def printList(head):
    curr = head
    nodes = []
    while curr:
        nodes.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(nodes))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original list:")
printList(head)
new_head = deleteMiddle(head)
print("After deleting middle:")
printList(new_head)
