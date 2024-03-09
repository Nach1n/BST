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

    def find(self, value) -> bool:
        if value < self.value:
            if not self.left:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if not self.right:
                return None
            else:
                return self.right.find(value)
        else:
            return self


tree = TreeNode(5)
tree.insert(4)
tree.insert(6)
tree.insert(7, {"data": "My data:)"})
tree.insert(2)
tree.insert(1)
tree.insert(15)

print(tree.find(7).content)
print(tree.find(7).content["data"])
