#binary tree implementation

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def __str__(self):
        return f"< Node data : {self.data}>" 

if __name__=="__main__":
    node3=Node(3)
    node2=Node(2)
    node1=Node(1)
    print(node2.__str__())