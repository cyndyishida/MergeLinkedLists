class LinkedListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def setVal(self, val):
        self.val = val

    def setNext(self, next):
        self.next = next




class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return "->".join(result)

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





def DivideLists(head):
    slow = head
    fast = head
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid



def MergeLists(L1, L2):
    temp = None
    if not L1:
        return L2
    if not L2:
        return L1
    if L1.val <= L2.val:
        temp = L1
        temp.next = MergeLists(L1.next, L2)
    else:
        temp = L2
        temp.next = MergeLists(L1, L2.next)
    return temp



def MergeSort(head):
    if not head or not head.next:
        return head
    L1,L2 = DivideLists(head)
    L1 = MergeSort(L1)
    L2 = MergeSort(L2)
    head = MergeLists(L1, L2)
    return head

