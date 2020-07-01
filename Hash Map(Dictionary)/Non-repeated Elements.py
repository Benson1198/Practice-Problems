def printNonRepeated(arr,n):
    dict1 = {}
    
    res = []
    
    for i in arr:
        dict1[str(i)] = 0
    
    for i in arr:
        if str(i) in dict1:
            dict1[str(i)] += 1
    
    for i in arr:
        if dict1[str(i)] == 1:
            res.append(i)
    
    return res