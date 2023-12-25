from binary_tree import TreeNode


class DepthFirst:
    def inorder(self, root):
        # left - root - right
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        # root - left - right
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        # left - right - parent
        if not root:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print(root.val)
