class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.data = item


class BinaryTree(Node):
    def __init__(self):
        self.root=None
    
    def insertNode(self,val):
        node=Node(val)
        if self.root == None :
            self.root=node
        else:
            self.insertRecursive(self.root,val)
    
    def insertRecursive(self,node,val):
        if node.data > val:
            if node.left != None:
                self.insertRecursive(node.left,val)
            else:
                node.left = Node(val)
        else:
            if node.right !=None:
                self.insertRecursive(node.right,val)
            else:
                node.right=Node(val)

    def inorder(self,root):

        if root:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.data) + " --> ", end='')
            # Traverse right
            self.inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end=' ')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


if __name__=="__main__":
    bt=BinaryTree()
    bt.insertNode(1)
    bt.insertNode(2)
    bt.insertNode(3)
    bt.inorder(bt.root)







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