class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert_node(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert_node(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def findval(self, val):
        if val < self.data:
            if self.left:
                return self.left.findval(val)
            else:
                return str(val) + "Not Found"
        elif val > self.data:
            if self.right:
                return self.right.findval(val)
            else:
                return str(val) + " Not Found"
        else:
            return str(val) + " Found "

# InOrder traversal
    def inorder(self):
       if self.left:
           self.left.inorder()
       print (self.data)
       if self.right:
           self.right.inorder()

# PreOrder Traversal
    def preorder(self):
        print (self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

# PostOrder Traversal
    def postorder(self):
       if self.left:
           self.left.postorder()
       if self.right:
           self.right.postorder()
       print (self.data)
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert_node(6)
root.insert_node(14)
root.insert_node(3)
# root.PrintTree()
# print(root.findval(14))
# print(root.findval(9))
# print(root.findval(12))

print (root.inorder())
print (root.preorder())
print (root.postorder())
