class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.content = None
        self.value = value

    def insert(self, value, content=None) -> None:
        if value == self.value:
            # Avoiding repeated values in the nodes
            return
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if not self.right:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if not self.left:
                return False, None
            else:
                return self.left.find(value)
        elif value > self.value:
            if not self.right:
                return False, None
            else:
                return self.right.find(value)
        else:
            return True, self


tree = TreeNode(5)
tree.insert(4)
tree.insert(6)
tree.insert(7, {"data": "My data:)"})
tree.insert(2)
tree.insert(1)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(9)
tree.insert(16)
tree.insert(5)

print("inorder_traversal")
tree.inorder_traversal()
print("***")
print("preorder_traversal")
tree.preorder_traversal()
print("***")
print("postorder_traversal")
tree.postorder_traversal()

print(tree.find(7)[1].content)
print(tree.find(7)[1].content["data"])
