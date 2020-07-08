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

