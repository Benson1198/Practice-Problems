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

