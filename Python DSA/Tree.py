#binary tree implementation

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def __str__(self):
        return f"< Node data : {self.data}>" 
