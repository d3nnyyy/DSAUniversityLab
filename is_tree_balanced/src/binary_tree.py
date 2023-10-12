"""
Binary tree node implementation.
"""


class BinaryTree:
    """
    Initialize a new binary tree node.

    Args:
        value: The value to store in the node.
        left: The left child node.
        right: The right child node.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
