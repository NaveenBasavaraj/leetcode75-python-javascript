class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
1. Root Node : 
* Highest node in a tree
* Has no parent node
* Ancestor to all node
* can be reached by all nodes

2. Leaf Node:
* Nodes without any children
* Nodes at last level (guaranteed)
* But can also be at other levels

3. Children:
* Left and Right Child

4. Height:
* Height of a binary tree is measured from the root node to the lowest leaf node
* Height of single node is 1 (if node itself is counted, else 0)
* Height is also counted by no of edges
    * using this method, height = n - 1
    * here n is the no of nodes

5. Depth:
* Measured from the node itself , all the way to the root.
* Depth of root is 1, increases by 1 as we go down for each node

6. Ancestor:
* A node connected to all the nodes below it is considered an ancestor to these nodes

7. Descendant:
* The descendant of a node is either child of the node or child of some other descendant node

'''