class LinkedListNode:
    def __init__(self, val = None):

        self.val = val
        self.next = None

    def __le__(self, other):

        if isinstance(other, LinkedListNode):
            return self.val <= other.val


class LinkedList:
    def __init__(self):

        self.head = None

    def __repr__(self):

        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def append(self, data):

        node = LinkedListNode(data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        else:
            self.head = node



'''
ANYTHING BEFORE THIS COMMENT SHOULDN'T BE MODIFIED IN ANYWAY!
----- START MODIFYING HERE ----
'''





def MergeSort(head):

    return head

