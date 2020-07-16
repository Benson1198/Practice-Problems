def rightViewUtil(root, level, max_level): 
    if root is None: 
        return
    
    if (max_level[0] < level):
        print(root.data,end = ' ') 
        max_level[0] = level


    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level)

def rightView(root):
    max_level = [0] 
    rightViewUtil(root, 1, max_level)