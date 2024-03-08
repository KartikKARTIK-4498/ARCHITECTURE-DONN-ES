class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order_traversal(node):
    """Prints elements of a binary tree in pre-order traversal."""
    if node is not None:
        print(node.value, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


if __name__ == '__main__':
    try:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        print("Pre-order Traversal:")
        pre_order_traversal(root)

    except Exception as e:
        print(f"Error: {e}. Please enter valid input.")
