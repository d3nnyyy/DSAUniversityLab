from is_tree_balanced.src.binary_tree import BinaryTree


def get_height(node: BinaryTree) -> int:
    if node is None:
        return 0

    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    return 1 + max(left_tree_height, right_tree_height)


def is_tree_balanced(node: BinaryTree) -> bool:
    left_tree_height = get_height(node.left)
    right_tree_height = get_height(node.right)

    return abs(left_tree_height - right_tree_height) <= 1
