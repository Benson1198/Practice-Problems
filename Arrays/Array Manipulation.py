def arrayManipulation(n, queries):
    arr = [0]*n
    max_sum = 0
    
    for q in queries:
        arr[q[0] - 1] += q[2]
        if arr[q[1]] <= n:
            arr[q[1]] -= q[2]
    
    for i in arr:
        temp = max_sum + i
        if temp >= max_sum:
            max_sum = temp

    return max_sum
