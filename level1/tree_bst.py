from tree_node import Node

class BinarySearchTree:
    def insert(self, root, val):
        if not root:
            return Node(val)
        if val > root.val:
            root.right = self.insert(root.right)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            return root