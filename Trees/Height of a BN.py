def heightUtil(root,h):
    if not root:
        return 
    
    if root.left:
        if root.right:
            h -= 1
        h += 1
        heightUtil(root.left,h)

    if root.right:
        h += 1
    
    return h
    
def heightBN(root):
    h = 0
    return heightUtil(root,h)
