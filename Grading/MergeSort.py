class LinkedListNode:
    def __init__(self, val=None):
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

    def push_back(self, data):
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
'''


# --------- START MODIFYING HERE ---------


def MergeSort(head):
    if head.next is None:
        return head

    # Find the mid point of the list using a slow and fast pointer
    prev = slow = fast = head
    while slow and fast:
        prev = slow
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    # Detach the right half of the list
    right = slow
    prev.next = None

    left = MergeSort(head)
    right = MergeSort(right)

    return merge(left, right)


def merge(left, right):
    le = left
    r = right
    result = result_walk = None
    while le and r:
        is_left = le <= r
        node = le if is_left else r

        if result is None:
            result = result_walk = node
        else:
            result_walk.next = node
            result_walk = result_walk.next

        # "node" still contains connections to the rest of the list
        # we must detach after adding it to the result
        prev = node
        node = node.next
        prev.next = None

        # Determine which pointer node to update
        le = node if is_left else le
        r = node if not is_left else r

    # Attach the remainder of the list to the result
    if le:
        result_walk.next = le
    else:
        result_walk.next = r

    return result