def areMirror(root1,root2):
    a = root1
    b = root2
    
    if a is None and b is None: 
        return True
      
    if a is None or b is None: 
        return False
        
        
    return (a.data == b.data and 
            areMirror(a.left, b.right) and 
            areMirror(a.right , b.left))
