"""
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree
in which the left and right subtrees of every node
differ in height by no more than one.

Example 1:

    10
   / \
  5   20
 / \
1   8

The above binary tree is height-balanced because
the left subtree's height is 2 and the right subtree's height is 1,
so the difference is 1 which is less than or equal to 1.

Example 2:

        10
       /  \
      5    20
     / \
    3   8
   /     \
  1       9

The above binary tree is not height-balanced because
the left subtree's height is 3 and the right subtree's height is 1,
so the difference is 2 which is greater than 1.
"""

from is_tree_balanced.src.binary_tree import BinaryTree


def get_height(node: BinaryTree) -> int:
    """
    Recursively calculate the height of the binary tree rooted at the given node.

    :param node: The root node of the binary tree
    :return: The height of the binary tree rooted at the given node
    """

    # If the node is None, then the height is 0.
    if node is None:
        return 0

    # Calculate the height of the left and right subtrees.
    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    # Return the maximum height plus 1, representing the height of the current node.
    return 1 + max(left_tree_height, right_tree_height)


def is_tree_balanced(node: BinaryTree) -> bool:
    """
    Determine if the binary tree rooted at the given node is height-balanced.

    :param node: The root node of the binary tree
    :return: True if the binary tree is height-balanced, otherwise False
    """

    # If the node is None, then the tree is balanced.
    if node is None:
        return True

    # Calculate the height of the left and right subtrees.
    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    # Check if the absolute difference in heights is at most 1, indicating a balanced tree.
    return abs(left_tree_height - right_tree_height) <= 1
