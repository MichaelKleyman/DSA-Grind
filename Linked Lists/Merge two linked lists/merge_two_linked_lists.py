from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TIME COMPLEXITY: 0(n) due to one while loop going through both of the linked lists
# SPACE COMPLEXITY: 0(1) due to size of the variables not increasing as the input size increases

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]):
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    
    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2

    return dummy.next
            