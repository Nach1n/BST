class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.inser(value)
