def countDistinct(arr, N, K):
    res = [] 
    if N > K:
        for i in range(N-K+1):
            res.append(len(set(arr[i:i+K])))
    
    else:
        res.append(len(set(arr)))
    
    return res