class LinkedListNode:
    def __init__(self, val = None):
        """
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.val = val
        self.next = None

    def __le__(self, other):
        '''
        :param other: Linked list node
        :return: boolean value of less than equal to other
        '''
        if isinstance(other, LinkedListNode):
            return self.val <= other.val





class LinkedList:
    def __init__(self):
        """
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None

    def __repr__(self):
        '''
        :param: none
        :return: string representation of linked list
        '''
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def append(self, data):
        '''
        :param data:  val for new node to be added to Linked list
        :return: None
        '''
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



def DivideLists(head):
    slow = head
    fast = head.next if head else head
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid



def MergeLists(L1, L2):
    curr = None
    if not L1:
        return L2
    if not L2:
        return L1
    if L1 <= L2:
        curr = L1
        curr.next = MergeLists(L1.next, L2)
    else:
        curr = L2
        curr.next = MergeLists(L1, L2.next)
    return curr



def MergeSort(head):
    '''
    :param head: Linked List node that is the start of Linked List
    :return: Head of the now sorted linked list
    '''
    if not head or not head.next:
        return head
    L1,L2 = DivideLists(head)
    L1 = MergeSort(L1)
    L2 = MergeSort(L2)
    head = MergeLists(L1, L2)
    return head




