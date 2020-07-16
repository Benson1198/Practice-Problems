dia=0
def util(root):
    if root == None:
        return 0
    global dia
    l=util(root.left)
    r=util(root.right)
    dia=max(dia, l+r+1)
    return 1 + max(l, r)

    
def diameter(root):
    global dia
    dia=0
    util(root)
    return dia