def countLeaves(root):
    if root is None:
        return 0
    
    elif (root.left == None) and (root.right == None):
        return 1
        
    else:
        return countLeaves(root.left) + countLeaves(root.right)