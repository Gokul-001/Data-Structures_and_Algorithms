class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        return "Head Node : %s" % (self.val)


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or self.head == None or index > self.size:
            return -1
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.head = node
            self.size += 1
            return
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head == None:
            self.addAtHead(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if self.head == None:
            self.head = node
            self.size += 1
            return
        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return
        current = self.head
        next_node = None
        count = 0
        while current:
            if count == index-1:
                next_node = current.next
                current.next = node
                node.next = next_node
                self.size += 1
                return
            count += 1
            current = current.next

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head == None or index > self.size:

            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current:
            if count == index-1:
                prev = current.next
                current.next = prev.next
                self.size -= 1
                return
            count += 1
            current = current.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("Null\n------")
        print(self.head)
        print("Size:", self.size)

"""
Optimized Linked list  


class ListNode: 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode(-1)  # dummy node
        self.tail = self.head
        self.size = 0

    def get(self, index):
        # handling edge case
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        # addAtIndex(self.size, val) was taking O(n)
        # Optimization: adding at tail is now O(1)
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index, val):
        # tail = when the index is equal to the size, we can add to tail
        # but can not add when the index is more than the last or you can call it size
        if index > self.size:
            return

        # pointing to the dummy node
        # because to insert a new node, we need to stop at the predecessor node
        # basically, [prev -> next] will be [prev -> new_node -> the old next of prev]
        prev = self.head  # the dummy head
        for _ in range(index):
            prev = prev.next

        new_node = ListNode(val, prev.next)
        prev.next = new_node

        # eventually if the new node has no next node
        # we can call it tail of the linkedlist
        if not new_node.next:
            self.tail = new_node

        self.size += 1

    def deleteAtHead(self):
        self.deleteAtIndex(0)

    def deleteAtTail(self):
        # can not optimize this without double linked list.
        # because in single linked list it takes O(n) time
        # to reach the predecessor node of the tail
        self.deleteAtIndex(self.size - 1)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        # same as insertion
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node_to_delete = prev.next
        # in case we want to delete the tail where (index = size -1)
        if self.tail == node_to_delete:
            self.tail = prev

        # at this point the pred will be hopped wil to the next.next
        prev.next = prev.next.next
        self.size -= 1
        """
if __name__ == "__main__":
    l = MyLinkedList()
    l.addAtHead(1)
    l.addAtTail(3)
    l.addAtTail(4)
    l.addAtTail(6)
    l.display()
    l.addAtIndex(1, 2)
    l.display()
    l.deleteAtIndex(2)
    print(l.get(1))
    l.deleteAtIndex(0)
    l.display()
    print(l.get(0))
    l.display()
