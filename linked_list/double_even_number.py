class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def doubleEvenNumber(head):
    current = head
    count = 0
    #ポインターのつなぎを忘れないように
    while current is not None:
        if count % 2 == 0:
            original_next = current.next
            duble = current.data * 2
            current.next = SinglyLinkedListNode(duble)
            current.next.next = original_next
            current = original_next
            count += 1
        else:
            current = current.next
            count += 1
    return head
        


