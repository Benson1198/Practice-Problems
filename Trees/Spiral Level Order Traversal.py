def printSpiral(root): 
    if (root == None): 
        return 

    sRL = []

    sLR = [] 
            
    sRL.append(root)  
  
    while not len(sRL) == 0 or not len(sLR) == 0: 
 
        while not len(sRL) == 0: 
            temp = sRL[-1]  
            sRL.pop()  
            print(temp.data, end = " ")  
 
            if (temp.right):  
                sLR.append(temp.right)  
            if (temp.left): 
                sLR.append(temp.left) 
  
 
        while (not len(sLR) == 0): 
            temp = sLR[-1]  
            sLR.pop()  
            print(temp.data, end = " ")  
  
            if (temp.left): 
                sRL.append(temp.left)  
            if (temp.right):  
                sRL.append(temp.right)