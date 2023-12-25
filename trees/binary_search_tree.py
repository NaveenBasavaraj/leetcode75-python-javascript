from trees.binary_tree import TreeNode


class BST:
    def search(self, root, target):
        if not root:
            # if we reached a point there is no more node to
            # traverse, then the target value does not exist
            # in the tree
            return False

        if target > root.val:
            # values greater than root, are found on the right sub-tree
            return self.search(root.right, target)
        elif target < root.val:
            # values greater than root, are found on the left sub-tree
            return self.search(root.left, target)
        else:
            return True

    def insert(self, root, val):
        if not root:
            # if there are not more nodes to validate
            # then we reached the point of insert
            return TreeNode(val)

        if val > root.val:
            # values greater than root, should be inserted to right sub-tree
            root.right = self.insert(root.right, val)
        elif val < root.val:
            # values greater than root, should be inserted to left sub-tre
            root.left = self.insert(root.left, val)
        return root

    def remove(self, root, val):
        # remove a node and return its roots
        def minValueNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None

        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            # when we finally find the node to remove
            if not root.left:
                # if no left child, then right child becomes the new root
                return root.right
            elif not root.right:
                # if no right child, then left child becomes the new root
                return root.left
            else:
                minNode = minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)
        return root
