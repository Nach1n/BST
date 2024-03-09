class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value == self.value:
            # Avoiding repeated values in the nodes
            return
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value < self.value:
            if not self.left:
                return False
            else:
                self.left.find(value)
        elif value > self.value:
            if not self.right:
                return False
            else:
                self.right.find(value)
        else:
            return True


tree = TreeNode(5)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(2)
tree.insert(1)
tree.insert(15)

print(tree.left.left.left.value)
