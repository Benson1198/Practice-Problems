def isSumTree(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    if root.data == isSumTree(root.left) + isSumTree(root.right):
        return 2 * root.data

    return False