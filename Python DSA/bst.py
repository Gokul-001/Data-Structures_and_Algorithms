class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.data = item

class Queue:
    def __init__(self, size):
        self.front = self.rear = -1
        self.size = size
        self.Q = [None] * size

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue Full")
        else:
            self.rear += 1
            self.Q[self.rear] = x

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            self.front += 1
            x = self.Q[self.front]
            return x

    def is_empty(self):
        return self.front == self.rear

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if node.data > val:
            if node.left is not None:
                self._insert_recursive(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._insert_recursive(node.right, val)
            else:
                node.right = Node(val)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.data) + " --> ", end='')
            self.inorder(root.right)

    def create_tree(self):
        q = Queue(7)
        print("Enter root value: ", end="")
        x = int(input())
        self.root = Node(x)
        q.enqueue(self.root)
        while not q.is_empty():
            p = q.dequeue()
            print("Enter left child of", p.data, ": ", end="")
            x = int(input())
            if x != -1:
                t = Node(x)
                p.left = t
                q.enqueue(t)
            print("Enter right child of", p.data, ": ", end="")
            x = int(input())
            if x != -1:
                t = Node(x)
                p.right = t
                q.enqueue(t)

    def preorder(self, root):
        if root:
            print(str(root.data) + " --> ", end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.data) + " --> ", end='')

    def levelorder(self, root):
        q = Queue(100)
        print(root.data, end=" ")
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            if root.left:
                print(root.left.data, end=" ")
                q.enqueue(root.left)
            if root.right:
                print(root.right.data, end=" ")
                q.enqueue(root.right)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.create_tree()
    print("\nInorder Traversal")
    bt.inorder(bt.root)
    print("\nPreorder Traversal")
    bt.preorder(bt.root)
    print("\nPostorder Traversal")
    bt.postorder(bt.root)
    print("\nLevel Order Traversal")
    bt.levelorder(bt.root)
