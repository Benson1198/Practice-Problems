def lca(root, n1, n2):
    if (not root):
        return
    
    if root.data == n1:
        return root
    elif root.data == n2:
        return root

    left = lca(root.left, n1, n2)
    
    right = lca(root.right, n1, n2)
    
    if left and right:
        return root
        
    return left if left is not None else right