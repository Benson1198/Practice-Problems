def maxDistance(arr, n):
    set1 = list(set(arr))

    dict1 = {}
    
    for i in range(n):
        dict1[str(arr[i])] = i
    
    for i in set1:
        ind = arr.index(i)
        dict1[str(i)] -= ind
    
    return max(list(dict1.values()))