class Node:
    """Class Node 
    It is the obj to store the node information
    2-Attributes : Data and Next  """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "< Node: %s >" % self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def appendNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        temp = self.head
        while temp.next:
            temp = temp.next  # temp +=1
        temp.next = node  # tail.next -> new node
        self.tail = node
        self.size += 1

    def prependNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
        # tail update
        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp

    def insertIndex(self, data, index):
        node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("Index out of bounds")
        if index == 0:
            self.prependNode(data)
            return
        temp = self.head
        itr = 0
        while temp:
            if itr == index-1:
                dummy = temp.next
                temp.next = node
                node.next = dummy
                self.size += 1
            itr += 1
            temp = temp.next

    def findMiddle(self):
        slow=fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null\n------")
        print("Head:", self.head)
        print("Tail:", self.tail)
        print("Size:", self.size)

    def deleteValue_GPT(self, value):
        print("Tail node is not updated in this method")
        current = self.head
        # head node to be deleted
        if current and current.data == value:
            self.head = current.next
            current = None  # free the node
            return " Head Node [%s] deleted" % value

        # Rest of the case :
        prev = None
        while current and current.data != value:
            # search for node
            prev = current
            current = current.next
        # if not found
        if not current:
            return "Node not found"
        prev.next = current.next
        current = None  # free node

    def hasCycle(self):
        Hashset = set()
        temp = self.head
        while temp:
            if temp in Hashset:
                return True
            Hashset.add(temp)
            temp = temp.next
        return False

    # need to rectify it
    def deleteValue(self, value):
        current = self.head
        prev = None
        found = False
        while current and not found:
            if self.head == value and current.data == value:
                self.head = current.next
                found = True
                return "Node removed :%s" % value
            elif current.data == value:
                prev = current
                prev.next = current.next
                current = None
                found = True
                # return current
                return "Node removed :%s" % value
            else:
                prev = current
                current = current.next
        return "Node not found"

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next

                return current
            elif current.data == key:
                found = True
                previous.next = current.next

                return current
            else:
                previous = current
                current = current.next

        return None

    def reverse(self):
        current = self.head
        prev = None  # Initialize prev to None to signify the end of the reversed list

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


if __name__ == "__main__":
    l = LinkedList()
    l.appendNode(1)
    l.appendNode(2)
    l.appendNode(3)
    # l.head.next.next.next=l.head
    # print(l.hasCycle())
    # print(l.deleteValue_GPT(3))
    # print(l.deleteValue(31))
    # l.remove(3)
    l.display()
    l.reverse()
    l.display()
    print(l.head)
'''
    l2 = LinkedList()
    l2.prependNode(1)
    l2.prependNode(2)
    l2.prependNode(3)
    l2.prependNode(4)
    l2.prependNode(5)
    l2.insertIndex("X", 0)
    l2.display()
    print("Middle element of the ll: ", l2.findMiddle())
'''
