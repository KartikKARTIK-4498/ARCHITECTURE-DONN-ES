from activity.activity22 import TreeNode, pre_order_traversal

def test_pre_order_traversal(capsys):
    # Create a binary tree:      1
    #                          /   \
    #                         2     3
    #                        / \   / \
    #                       4   5 6   7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    pre_order_traversal(root)

    captured = capsys.readouterr()
    expected_output = "1 2 4 5 3 6 7 "
    assert captured.out == expected_output
