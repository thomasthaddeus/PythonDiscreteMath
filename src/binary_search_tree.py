"""
Binary Search Tree operations in Python

This script implements the operations of a Binary Search Tree (BST) in Python.
It includes the following operations:
- Creating a node
- Inorder traversal
- Inserting a node
- Finding the inorder successor
- Deleting a node

"""

class Node:
    """Class representing a node in a binary search tree."""

    def __init__(self, key):
        """Initialize a new node with the given key.

        Args:
            key: The value of the node.
        """
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    """Perform inorder traversal of the binary search tree.

    Args:
        root: The root node of the binary search tree.

    Returns:
        None
    """
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=" ")
        inorder(root.right)


def insert(my_node, key):
    """Insert a node with the given key into the binary search tree.

    Args:
        node: The root node of the binary search tree.
        key: The value to be inserted.

    Returns:
        The updated root node of the binary search tree.
    """
    if my_node is None:
        return Node(key)

    if key < my_node.key:
        my_node.left = insert(my_node.left, key)
    else:
        my_node.right = insert(my_node.right, key)

    return my_node


def minValueNode(my_node):
    """Find the node with the minimum value in the binary search tree.

    Args:
        node: The root node of the binary search tree.

    Returns:
        The node with the minimum value.
    """
    current = my_node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):
    """Delete a node with the given key from the binary search tree.

    Args:
        root: The root node of the binary search tree.
        key: The value to be deleted.

    Returns:
        The updated root node of the binary search tree.
    """
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root


if __name__ == "__main__":
    my_root = None
    my_root = insert(my_root, 2)
    my_root = insert(my_root, 5)
    my_root = insert(my_root, 8)
    my_root = insert(my_root, 10)
    my_root = insert(my_root, 13)
    my_root = insert(my_root, 19)
    my_root = insert(my_root, 21)
    my_root = insert(my_root, 32)
    my_root = insert(my_root, 37)
    my_root = insert(my_root, 52)

    print("Inorder traversal:", end=" ")
    inorder(my_root)

    print("\nDelete 10")
    my_root = deleteNode(my_root, 10)
    print("Inorder traversal:", end=" ")
    inorder(my_root)
