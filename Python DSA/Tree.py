from queue import Queue


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.data = item


class BinaryTree(Node):
    def __init__(self):
        self.root=None
    
    def insertNode(self,val):
        self.root=self._insert(self.root,val)
    
    def _insert(self, root, val):
        if root is None:
            return Node(val)
        if val < root.data:
            root.left = self._insert(root.left, val)
        elif val > root.data:
            root.right = self._insert(root.right, val)
        return root

    def inorder(self,root):

        if root:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.data) + " --> ", end='')
            # Traverse right
            self.inorder(root.right)

    def bfs(self,root):
        queue=Queue()
        queue.put(root)
        while not queue.empty():
            node=queue.get()
            print(node.data,end=" --> ")
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)


    def postorder(self,root):

        if root:
            # Traverse left
            self.postorder(root.left)
            # Traverse right
            self.postorder(root.right)
            # Traverse root
            print(str(root.data) + " --> ", end='')


    def preorder(self,root):

        if root:
            # Traverse root
            print(str(root.data) + " --> ", end='')
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self.preorder(root.right)


if __name__=="__main__":
    bt=BinaryTree()
    bt.insertNode(1)
    bt.insertNode(2)
    bt.insertNode(3)
    bt.insertNode(4)
    bt.insertNode(5)
    bt.insertNode(6)
    bt.insertNode(7)
    print("Inorder Traversal")
    bt.inorder(bt.root)
    print("\nPreorder Traversal")
    bt.preorder(bt.root)
    print("\nPostorder Traversal")
    bt.postorder(bt.root)
    print("\nBreadth first search ")
    bt.bfs(bt.root)







'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
'''