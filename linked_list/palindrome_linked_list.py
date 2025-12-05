class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def palindromeLinkedList(head):
    if head is None:
        return None
    fast = head
    slow = head
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        fast = fast.next.next
        slow = slow.next
   
    if fast is not None:
        slow = slow.next
    
    while stack:
        if stack[-1] != slow.data:
            return False
        stack.pop()
        slow = slow.next
    return True