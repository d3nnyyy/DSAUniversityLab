"""
Unit tests for the is_tree_balanced.py module.
"""

import unittest

from is_tree_balanced.src.binary_tree import BinaryTree
from is_tree_balanced.src.is_tree_balanced import is_tree_balanced


def create_balanced_tree():
    """
    Create a balanced tree:

        10
       /  \
      5    20
     / \
    1   8

    :return: The root node of the tree
    """

    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(20)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(8)
    return root


def create_unbalanced_tree():
    """
    Create an unbalanced tree:

            10
          /   \
         5    20
        / \
       3   8
      /     \
     1       9

    :return: The root node of the tree
    """

    root = BinaryTree(10)
    root.left = BinaryTree(5)
    root.right = BinaryTree(20)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(8)
    root.left.left.left = BinaryTree(1)
    root.left.right.right = BinaryTree(9)
    return root


class TestIsTreeBalanced(unittest.TestCase):
    """
    Test class for the is_tree_balanced.py module.
    """

    def test_balanced_tree(self):
        """
        Test that a balanced tree is balanced.
        :return: None
        """
        root = create_balanced_tree()
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        """
        Test that an unbalanced tree is not balanced.
        :return: None
        """
        root = create_unbalanced_tree()
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        """
        Test that an empty tree is balanced.
        :return: None
        """
        self.assertTrue(is_tree_balanced(None))


if __name__ == '__main__':
    unittest.main()
