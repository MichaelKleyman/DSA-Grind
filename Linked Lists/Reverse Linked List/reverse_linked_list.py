
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TIME COMPLEXITY: 0(n) Linear time complexity because we're iterating through the list only once
# SPACE COMPLEXITY: 0(1) Constant time complexity because the variable size doesnt grow with the input size

def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:

    prev = None
    cur = head

    while cur != None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev

head = [1,2,3,4,5]
print(reverseLinkedList(head))