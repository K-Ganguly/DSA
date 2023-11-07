# LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # Initialize an empty list to store the serialized tree
        serialized_tree = list()

        def preorder_traversal(root):
            if not root:
                # If the current node is None, add "N" to indicate a null node
                serialized_tree.append("N")
                return None
            # Add the value of the current node to the serialized tree
            serialized_tree.append(str(root.val))
            # Recursively traverse the left and right subtrees
            preorder_traversal(root.left)
            preorder_traversal(root.right)
            return None

        # Start the preorder traversal from the root
        preorder_traversal(root)

        # Join the serialized elements with commas to create the final serialized tree
        serialized_tree = ",".join(serialized_tree)

        # Return the serialized tree as a string
        return serialized_tree

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Initialize an index to keep track of the current position in the data
        self.i = 0
        # Split the data string into a list of elements
        nodes = data.split(",")

        def preorder_traversal():
            if nodes[self.i] == "N":
                # If the current element is "N," it represents a null node, so return None
                self.i += 1
                return None
            # Create a new node with the current element as its value
            node_val = nodes[self.i]
            node = TreeNode(node_val)
            self.i += 1
            # Recursively build the left and right subtrees
            node.left = preorder_traversal()
            node.right = preorder_traversal()
            return node

        # Start the preorder traversal to reconstruct the tree
        root = preorder_traversal()

        # Return the root of the reconstructed tree
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
