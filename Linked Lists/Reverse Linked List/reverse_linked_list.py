
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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