# Simple Binary Tree Implementation

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

#            1 
#        /       \ 
#       2          3 
#     /   \       /  \ 
#    4    None  None  None 
#   /  \ 
# None None


# Binary Tree Insertion Methods

class newNode:

    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

# Inorder traversal of Binary Tree
def inorder(temp):
    if(not temp):
        return
    
    inorder(temp.left)
    print(temp.key,end = ' ')
    inorder(temp.right)

# Function to insert element in Binary Tree 

def insert(temp,key):
    q = []
    q.append(temp)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if(not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

# Function to delete deepest given node in Binary Tree

def deleteDeepest(root,d_node):
    q = []
    q.append(root)
    
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


# Function to delete element in Binary Tree

def deletion(root,key):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    
    key_node = None
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.key == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        
    if key_node:
        x = key_node
        deleteDeepest(root,temp)
        key_node.key = x
    return root


# Method to find Lowest Common Ancestor

def findLCAUtil(root,n1,n2,v):
    if root is None:
        return None
    
    if root.key == n1:
        v[0] = True
        return root
    
    if root.key == n2:
        v[1] = True
        return root
    
    left_lca = findLCAUtil(root.left,n1,n2,v)
    right_lca = findLCAUtil(root.right,n1,n2,v)

    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca is not None else right_lca


def find(root,k):
    if root is None:
        return False
    
    if (root.key == k or find(root.left,k) or find(root.right,k)):
        return True
    
    return False

def findLCA(root,n1,n2):
    v = [False,False]

    lca = findLCAUtil(root,n1,n2,v)

    if (v[0] and v[1] or v[0] and find(lca,n2) or v[1] and find(lca,n1)):
        return lca

    return None


# Method to find the diameter of Binary Tree

# Height Object

class Height:
    def __init__(self):
        self.h = 0

# Optimised Recursive function to find the diameter

def 


    
    
