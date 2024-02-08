class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return "< Head : %s>" % self.data


class DoublyLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prependNode(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return

    def appendNode(self, data):
        node = Node(data)
        if self.head == None:
            return self.prependNode(data)

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.prev = current
        self.size += 1
        return

    def insertNode(self, index, data):
        node = Node(data)
        if self.head == None:
            return self.prependNode(data)
        if index == 0:
            return self.prependNode(data)
        if index < 0 or index > self.size:
            return
        if index == self.size:
            current = self.head
            for _ in range(index-1):
                current = current.next

            prev_node = current.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = current
            self.size += 1
            return

        current = self.head
        for _ in range(index):
            current = current.next

        prev_node = current.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = current
        self.size += 1
        return
        '''
        next_node = current.next
        current.next = node
        node.prev = current
        node.next = next_node
        self.size += 1
        '''

    def __repr__(self) -> str:
        current = self.head
        str1 = ''
        print("Size:", self.size)
        while current:
            str1 += f"  <->  {current.data}"
            current = current.next
        return 'None'+str1+'  <->  None'

    def deleteFirst(self):
        if self.head == None:
            return "Empty"
        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        current = self.head.next
        current.prev = None
        self.head = current
        self.size -= 1
        return

    def deleteLast(self):
        if self.size == 1:
            self.deleteFirst()
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.size -= 1

    def deleteIndex(self, index):
        if index == 0:
            self.deleteFirst()
            return
        if index < 0 or index > self.size:
            raise Exception("index out of bounds")
            return
        current = self.head
        for _ in range(index-1):
            current = current.next
        current.next = current.next.next
        self.size -= 1
        return


if __name__ == "__main__":
    l = DoublyLL()
    l.appendNode(1)
    l.appendNode(2)
    l.appendNode(3)
    l.appendNode(4)
    l.appendNode(5)
    print(l.__repr__())
    l.deleteIndex(2)
    # l.deleteLast()
    print(l.__repr__())
