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
                self.right.inser(value)

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
