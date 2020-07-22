def minimumBribes(q):
    arr = q
    n = len(arr)
    count = 0

    for i in range(n-1,-1,-1):
        if arr[i] != i+1:
            if arr[i-1] == i+1:
                arr[i],arr[i-1] = arr[i-1],arr[i]
                count += 1
            elif arr[i-2] == i+1:
                arr[i-1],arr[i-2] = arr[i-2],arr[i-1]
                arr[i-1],arr[i] = arr[i],arr[i-1]
                count += 2
            else:
                return 'Too chaotic'
        else:
            continue
    
    return count



